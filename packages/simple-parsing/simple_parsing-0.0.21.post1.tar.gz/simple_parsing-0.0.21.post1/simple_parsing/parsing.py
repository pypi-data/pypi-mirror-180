"""Simple, Elegant Argument parsing.
@author: Fabrice Normandin
"""
from __future__ import annotations

import argparse
import dataclasses
import shlex
import sys
from argparse import SUPPRESS, Action, HelpFormatter, Namespace, _, _HelpAction
from collections import defaultdict
from functools import partial
from logging import getLogger
from pathlib import Path
from typing import Any, Callable, Sequence, TypeVar, overload

from . import utils
from .conflicts import ConflictResolution, ConflictResolver
from .help_formatter import SimpleHelpFormatter
from .helpers.serialization.serializable import read_file
from .utils import Dataclass, dict_union
from .wrappers import DashVariant, DataclassWrapper, FieldWrapper
from .wrappers.field_wrapper import ArgumentGenerationMode, NestedMode

logger = getLogger(__name__)


class ParsingError(RuntimeError, SystemExit):
    pass


class ArgumentParser(argparse.ArgumentParser):
    """Creates an ArgumentParser instance.

    Parameters
    ----------
    - conflict_resolution : ConflictResolution, optional

        What kind of prefixing mechanism to use when reusing dataclasses
        (argument groups).
        For more info, check the docstring of the `ConflictResolution` Enum.

    - add_option_string_dash_variants : DashVariant, optional

        Whether or not to add option_string variants where the underscores in
        attribute names are replaced with dashes.
        For example, when set to DashVariant.UNDERSCORE_AND_DASH,
        "--no-cache" and "--no_cache" can both be used to point to the same
        attribute `no_cache` on some dataclass.

    - argument_generation_mode : ArgumentGenerationMode, optional

        How to generate the arguments. In the ArgumentGenerationMode.FLAT mode,
        the default one, the arguments are flat when possible, ignoring
        their nested structure and including it only on the presence of a
        conflict.

        In the ArgumentGenerationMode.NESTED mode, the arguments are always
        composed reflecting their nested structure.

        In the ArgumentGenerationMode.BOTH mode, both kind of arguments
        are generated.

    - nested_mode : NestedMode, optional

        How to handle argument generation in for nested arguments
        in the modes ArgumentGenerationMode.NESTED and ArgumentGenerationMode.BOTH.
        In the NestedMode.DEFAULT mode, the nested arguments are generated
        reflecting their full 'destination' path from the returning namespace.

        In the NestedMode.WITHOUT_ROOT, the first level is removed. This is useful when
        parser.add_arguments is only called once, and where the same prefix would be shared
        by all arguments. For example, if you have a single dataclass MyArguments and
        you call parser.add_arguments(MyArguments, "args"), the arguments could look like this:
        '--args.input.path --args.output.path'.
        We could prefer to remove the root level in such a case
            so that the arguments get generated as
        '--input.path --output.path'.

    - formatter_class : Type[HelpFormatter], optional

        The formatter class to use. By default, uses
        `simple_parsing.SimpleHelpFormatter`, which is a combination of the
        `argparse.ArgumentDefaultsHelpFormatter`,
        `argparse.MetavarTypeHelpFormatter` and
        `argparse.RawDescriptionHelpFormatter` classes.

    - add_config_path_arg : bool, optional
        When set to `True`, adds a `--config_path` argument, of type Path, which is used to parse

    """

    def __init__(
        self,
        *args,
        parents: Sequence[ArgumentParser] = (),
        add_help: bool = True,
        conflict_resolution: ConflictResolution = ConflictResolution.AUTO,
        add_option_string_dash_variants: DashVariant = DashVariant.AUTO,
        argument_generation_mode=ArgumentGenerationMode.FLAT,
        nested_mode: NestedMode = NestedMode.DEFAULT,
        formatter_class: type[HelpFormatter] = SimpleHelpFormatter,
        add_config_path_arg: bool | None = None,
        config_path: Path | str | Sequence[Path | str] | None = None,
        add_dest_to_option_strings: bool | None = None,
        **kwargs,
    ):
        kwargs["formatter_class"] = formatter_class
        # Pass parents=[] since we override this mechanism below.
        # NOTE: We end up with the same parents.
        super().__init__(*args, parents=[], add_help=False, **kwargs)
        self.conflict_resolution = conflict_resolution
        # constructor arguments for the dataclass instances.
        # (a Dict[dest, [attribute, value]])
        # TODO: Stop using a defaultdict for the very important `self.constructor_arguments`!
        self.constructor_arguments: dict[str, dict] = defaultdict(dict)

        self._conflict_resolver = ConflictResolver(self.conflict_resolution)
        self._wrappers: list[DataclassWrapper] = []

        if add_dest_to_option_strings:
            argument_generation_mode = ArgumentGenerationMode.BOTH

        self._preprocessing_done: bool = False
        self.add_option_string_dash_variants = add_option_string_dash_variants
        self.argument_generation_mode = argument_generation_mode
        self.nested_mode = nested_mode

        FieldWrapper.add_dash_variants = add_option_string_dash_variants
        FieldWrapper.argument_generation_mode = argument_generation_mode
        FieldWrapper.nested_mode = nested_mode
        self._parents = tuple(parents)
        self._add_argument_replay: list[Callable[[ArgumentParser], Any]] = []

        self.add_help = add_help
        if self.add_help:
            prefix_chars = self.prefix_chars
            default_prefix = "-" if "-" in prefix_chars else prefix_chars[0]
            self._help_action = super().add_argument(
                default_prefix + "h",
                default_prefix * 2 + "help",
                action="help",
                default=SUPPRESS,
                help=_("show this help message and exit"),
            )

        # Add parent arguments and defaults.
        # THis is a little bit different than in Argparse: We replay all the `add_argument` and
        # `add_arguments` calls, instead of adding the same actions.
        # NOTE: We could probably also do this in `preprocessing` instead of `__init__`
        for parent in parents:
            for add_arguments_call in parent._add_argument_replay:
                add_arguments_call(self)

        self.config_path = Path(config_path) if isinstance(config_path, str) else config_path
        if add_config_path_arg is None:
            # By default, add a config path argument if a config path was passed.
            add_config_path_arg = bool(config_path)
        self.add_config_path_arg = add_config_path_arg

    def add_argument(
        self,
        *name_or_flags: str,
        **kwargs,
    ) -> Action:
        if hasattr(self, "_add_argument_replay"):
            # When creating the --help option in super().__init__, we don't yet have this attribute
            # and we don't want to save this call in the replay list, since it will be called
            # anyway when creating the child parser based on `add_help`.
            self._add_argument_replay.append(
                lambda parser: parser.add_argument(*name_or_flags, **kwargs)
            )
        return super().add_argument(
            *name_or_flags,
            **kwargs,
        )

    @overload
    def add_arguments(
        self,
        dataclass: type[Dataclass],
        dest: str,
        *,
        prefix: str = "",
        default: Dataclass | None = None,
        dataclass_wrapper_class: type[DataclassWrapper] = DataclassWrapper,
    ):
        pass

    @overload
    def add_arguments(
        self,
        dataclass: type,
        dest: str,
        *,
        prefix: str = "",
        dataclass_wrapper_class: type[DataclassWrapper] = DataclassWrapper,
    ):
        pass

    def add_arguments(
        self,
        dataclass: type[Dataclass] | Dataclass,
        dest: str,
        *,
        prefix: str = "",
        default: Dataclass = None,
        dataclass_wrapper_class: type[DataclassWrapper] = DataclassWrapper,
    ):
        """Adds command-line arguments for the fields of `dataclass`.

        Parameters
        ----------
        dataclass : Union[Dataclass, Type[Dataclass]]
            The dataclass whose fields are to be parsed from the command-line.
            If an instance of a dataclass is given, it is used as the default
            value if none is provided.
        dest : str
            The destination attribute of the `argparse.Namespace` where the
            dataclass instance will be stored after calling `parse_args()`
        prefix : str, optional
            An optional prefix to add prepend to the names of the argparse
            arguments which will be generated for this dataclass.
            This can be useful when registering multiple distinct instances of
            the same dataclass, by default ""
        default : Dataclass, optional
            An instance of the dataclass type to get default values from, by
            default None
        """
        # Save this call so that we can replay it on any child later.
        self._add_argument_replay.append(
            partial(
                type(self).add_arguments,
                dataclass=dataclass,
                dest=dest,
                prefix=prefix,
                default=default,
                dataclass_wrapper_class=dataclass_wrapper_class,
            )
        )
        for wrapper in self._wrappers:
            if wrapper.dest == dest:
                if wrapper.dataclass == dataclass:
                    raise argparse.ArgumentError(
                        argument=None,
                        message=f"Destination attribute {dest} is already used for "
                        f"dataclass of type {dataclass}. Make sure all destinations"
                        f" are unique. (new dataclass type: {dataclass})",
                    )
        if not isinstance(dataclass, type):
            default = dataclass if default is None else default
            dataclass = type(dataclass)

        new_wrapper = dataclass_wrapper_class(dataclass, dest, prefix=prefix, default=default)

        if new_wrapper.dest in self._defaults:
            new_wrapper.default = self._defaults[new_wrapper.dest]
        if self.nested_mode == NestedMode.WITHOUT_ROOT and all(
            field.name in self._defaults for field in new_wrapper.fields
        ):
            # If we did .set_defaults before we knew what dataclass we're using, then we try to
            # still make use of those defaults:
            new_wrapper.default = {
                k: v
                for k, v in self._defaults.items()
                if k in [f.name for f in dataclasses.fields(new_wrapper.dataclass)]
            }

        self._wrappers.append(new_wrapper)

    def parse_known_args(
        self,
        args: Sequence[str] | None = None,
        namespace: Namespace | None = None,
        attempt_to_reorder: bool = False,
    ):
        # NOTE: since the usual ArgumentParser.parse_args() calls
        # parse_known_args, we therefore just need to overload the
        # parse_known_args method to support both.
        if args is None:
            # args default to the system args
            args = sys.argv[1:]
        else:
            # make sure that args are mutable
            args = list(args)

        # default Namespace built from parser defaults
        if namespace is None:
            namespace = Namespace()
        if self.config_path:
            if isinstance(self.config_path, Path):
                config_paths = [self.config_path]
            else:
                config_paths = self.config_path
            for config_file in config_paths:
                self.set_defaults(config_file)

        if self.add_config_path_arg:
            temp_parser = ArgumentParser(add_config_path_arg=False, add_help=False)
            temp_parser.add_argument(
                "--config_path",
                type=Path,
                nargs="*",
                default=self.config_path,
                help="Path to a config file containing default values to use.",
            )
            args_for_config_path, args = temp_parser.parse_known_args(args)
            config_path = args_for_config_path.config_path

            if config_path is not None:
                config_paths = config_path if isinstance(config_path, list) else [config_path]
                for config_file in config_paths:
                    self.set_defaults(config_file)

            # Adding it here just so it shows up in the help message. The default will be set in
            # the help string.
            self.add_argument(
                "--config_path",
                type=Path,
                default=config_path,
                help="Path to a config file containing default values to use.",
            )

        self._preprocessing()

        logger.debug(f"Parser {id(self)} is parsing args: {args}, namespace: {namespace}")

        parsed_args, unparsed_args = super().parse_known_args(args, namespace)

        if self.subgroups:
            parser = type(self)(
                parents=[self],
                add_help=self._had_help,  # only add help in the child if the parent also had help.
                add_option_string_dash_variants=self.add_option_string_dash_variants,
                argument_generation_mode=self.argument_generation_mode,
                nested_mode=self.nested_mode,
            )
            if not hasattr(namespace, "subgroups"):
                namespace.subgroups = {}
            if not hasattr(parsed_args, "subgroups"):
                parsed_args.subgroups = {}

            for dest, subgroup_dict in self.subgroups.items():
                value = getattr(parsed_args, dest)

                def _get_wrapper_for_dest(dest: str) -> FieldWrapper:
                    """Retrieve the FieldWrapper from self._wrappers that has the given dest."""
                    for wrapper in self._wrappers:
                        for field_wrapper in wrapper.fields:
                            if field_wrapper.dest == dest:
                                return field_wrapper
                    raise ValueError(f"No FieldWrapper found for dest {dest}")

                field_wrapper = _get_wrapper_for_dest(dest)

                logger.debug(f"Chosen value for subgroup {dest}: {value}")
                # The prefix should be 'thing' instead of 'bob.thing'.
                # TODO: This needs to be tested more, in particular with argument conflicts.
                _, _, parent_dest = dest.rpartition(".")
                prefix = parent_dest + "."
                default = None
                chosen_subgroup: str
                if isinstance(value, str):
                    chosen_subgroup = value
                    chosen_class = subgroup_dict[chosen_subgroup]
                else:
                    # The value is not the subgroup name.
                    chosen_class = type(value)
                    default = value
                    if chosen_class in subgroup_dict.values():
                        chosen_subgroup = [
                            k for k, v in subgroup_dict.items() if v == chosen_class
                        ].pop()
                    else:
                        # A dynamic kind of default value?
                        raise RuntimeError(
                            f"Don't yet know how to detect which subgroup in {subgroup_dict} was "
                            f"chosen, if the default value is {value} and the field default is "
                            f"{field_wrapper.field.default}"
                        )
                # prefix = f"{dest}."
                parsed_args.subgroups[dest] = chosen_subgroup
                namespace.subgroups[dest] = chosen_subgroup

                parser.add_arguments(
                    chosen_class,
                    dest=dest,
                    prefix=prefix,
                    default=default,
                )
            # NOTE: Passing the `parsed_args` as the namespace to the child, so that it treats its
            # values as the defaults.
            parsed_args, unparsed_args = parser.parse_known_args(args, namespace=parsed_args)

        if unparsed_args and self._subparsers and attempt_to_reorder:
            logger.warning(
                f"Unparsed arguments when using subparsers. Will "
                f"attempt to automatically re-order the unparsed arguments "
                f"{unparsed_args}."
            )
            index_in_start = args.index(unparsed_args[0])
            # Simply 'cycle' the args to the right ordering.
            new_start_args = args[index_in_start:] + args[:index_in_start]
            parsed_args, unparsed_args = super().parse_known_args(new_start_args)

        parsed_args = self._postprocessing(parsed_args)
        return parsed_args, unparsed_args

    def print_help(self, file=None):
        self._preprocessing()
        # TODO: Need to also add the args for the chosen subgroups here. Is that possible?

        if self.subgroups:
            parser = type(self)(
                parents=[self],
                add_help=self._had_help,  # only add help in the child if the parent also had help.
                add_option_string_dash_variants=self.add_option_string_dash_variants,
                argument_generation_mode=self.argument_generation_mode,
                nested_mode=self.nested_mode,
            )

            for dest, subgroup_dict in self.subgroups.items():
                # Get the default value for that field?
                field_for_that_subgroup: FieldWrapper = [
                    field
                    for wrapper in self._wrappers
                    for field in wrapper.fields
                    if field.dest == dest
                ][0]

                value = field_for_that_subgroup.default

                logger.debug(f"Chosen value for subgroup {dest}: {value}")
                # The prefix should be 'thing' instead of 'bob.thing'.
                # TODO: This needs to be tested more, in particular with argument conflicts.
                _, _, parent_dest = dest.rpartition(".")
                prefix = parent_dest + "."
                if isinstance(value, str):
                    chosen_class = subgroup_dict[value]
                    parser.add_arguments(
                        chosen_class,
                        dest=dest,
                        prefix=prefix,
                    )
                else:
                    default = value
                    chosen_class = type(value)
                    # prefix = f"{dest}."
                    parser.add_arguments(
                        chosen_class,
                        dest=dest,
                        prefix=prefix,
                        default=default,
                    )
            return parser.print_help(file)
        return super().print_help(file)

    def set_defaults(self, config_path: str | Path | None = None, **kwargs: Any) -> None:
        """Set the default argument values, either from a config file, or from the given kwargs."""
        if config_path:
            defaults = read_file(config_path)
            if self.nested_mode == NestedMode.WITHOUT_ROOT and len(self._wrappers) == 1:
                # The file should have the same format as the command-line args, e.g. contain the
                # fields of the 'root' dataclass directly (e.g. "foo: 123"), rather a dict with
                # "config: foo: 123" where foo is a field of the root dataclass at dest 'config'.
                # Therefore, we add the prefix back here.
                defaults = {self._wrappers[0].dest: defaults}
                # We also assume that the kwargs are passed as foo=123
                kwargs = {self._wrappers[0].dest: kwargs}
            # Also include the values from **kwargs.
            kwargs = dict_union(defaults, kwargs)

        # The kwargs that are set in the dataclasses, rather than on the namespace.
        kwarg_defaults_set_in_dataclasses = {}
        for wrapper in self._wrappers:
            if wrapper.dest in kwargs:
                default_for_dataclass = kwargs[wrapper.dest]

                if isinstance(default_for_dataclass, (str, Path)):
                    default_for_dataclass = read_file(path=default_for_dataclass)
                elif not isinstance(default_for_dataclass, dict) and not dataclasses.is_dataclass(
                    default_for_dataclass
                ):
                    raise ValueError(
                        f"Got a default for field {wrapper.dest} that isn't a dataclass, dict or "
                        f"path: {default_for_dataclass}"
                    )

                # Set the .default attribute on the DataclassWrapper (which also updates the
                # defaults of the fields and any nested dataclass fields).
                wrapper.default = default_for_dataclass

                # It's impossible for multiple wrappers in kwargs to have the same destination.
                assert wrapper.dest not in kwarg_defaults_set_in_dataclasses
                value_for_constructor_arguments = (
                    default_for_dataclass
                    if isinstance(default_for_dataclass, dict)
                    else dataclasses.asdict(default_for_dataclass)
                )
                kwarg_defaults_set_in_dataclasses[wrapper.dest] = value_for_constructor_arguments
                # Remove this from the **kwargs, so they don't get set on the namespace.
                kwargs.pop(wrapper.dest)
        # TODO: Stop using a defaultdict for the very important `self.constructor_arguments`!
        self.constructor_arguments = dict_union(
            self.constructor_arguments,
            kwarg_defaults_set_in_dataclasses,
            dict_factory=lambda: defaultdict(dict),
        )
        # For the rest of the values, use the default argparse behaviour (modifying the
        # self._defaults dictionary).
        super().set_defaults(**kwargs)

    def equivalent_argparse_code(self) -> str:
        """Returns the argparse code equivalent to that of `simple_parsing`.

        TODO: Could be fun, pretty sure this is useless though.

        Returns
        -------
        str
            A string containing the auto-generated argparse code.
        """
        self._preprocessing()
        code = "parser = ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)"
        for wrapper in self._wrappers:
            code += "\n"
            code += wrapper.equivalent_argparse_code()
            code += "\n"
        code += "args = parser.parse_args()\n"
        code += "print(args)\n"
        return code

    def _resolve_conflicts(self) -> None:
        self._wrappers = self._conflict_resolver.resolve(self._wrappers)

    def _preprocessing(self) -> None:
        """Resolve potential conflicts and actual add all the arguments."""
        logger.debug("\nPREPROCESSING\n")
        if self._preprocessing_done:
            return

        self._resolve_conflicts()

        # Create one argument group per dataclass
        for wrapper in self._wrappers:
            logger.debug(
                f"Parser {id(self)} is Adding arguments for dataclass: {wrapper.dataclass} "
                f"at destinations {wrapper.destinations}"
            )
            wrapper.add_arguments(parser=self)

        self.subgroups: dict[str, dict[str, type]] = {}
        for wrapper in self._wrappers:
            for field_wrapper in wrapper.fields:
                if not field_wrapper.is_subgroup:
                    continue
                # NOTE: Need to prevent some weird recursion here.
                # A field is only supposed to be considered a subgroup if it hasn't already been
                # resolved by a parent!
                # IF we are a child, and encounter a subgroup field, then we should check if a
                # parent already had this field as a subgroup, and in this case, we just parse the
                # required type.
                if any(field_wrapper.dest in parent.subgroups for parent in self._parents):
                    logger.debug(
                        f"The field {field_wrapper.dest} is a subgroup that has already been "
                        f"resolved by a parent."
                    )
                    continue

                dest = field_wrapper.dest
                subgroups = field_wrapper.field.metadata["subgroups"]
                self.subgroups[dest] = subgroups

        self._had_help = self.add_help
        if self.subgroups and self.add_help:
            logger.debug("Removing the help action from the parser because it has subgroups.")
            self.add_help = False
            self._remove_help_action()

        self._preprocessing_done = True

    def _remove_help_action(self) -> None:
        self.add_help = False
        help_actions = [action for action in self._actions if isinstance(action, _HelpAction)]
        if not help_actions:
            return

        help_action = help_actions[0]
        self._remove_action(help_action)

        for option_string in self._help_action.option_strings:
            self._option_string_actions.pop(option_string)

    def _postprocessing(self, parsed_args: Namespace) -> Namespace:
        """Process the namespace by extract the fields and creating the objects.

        Instantiate the dataclasses from the parsed arguments and set them at
        their destination attribute in the namespace.

        Parameters
        ----------
        parsed_args : Namespace
            the result of calling `super().parse_args(...)` or
            `super().parse_known_args(...)`.
            TODO: Try and maybe return a nicer, typed version of parsed_args.


        Returns
        -------
        Namespace
            The original Namespace, with all the arguments corresponding to the
            dataclass fields removed, and with the added dataclass instances.
            Also keeps whatever arguments were added in the traditional fashion,
            i.e. with `parser.add_argument(...)`.
        """
        logger.debug("\nPOST PROCESSING\n")
        logger.debug(f"(raw) parsed args: {parsed_args}")
        # create the constructor arguments for each instance by consuming all
        # the relevant attributes from `parsed_args`
        parsed_args = self._consume_constructor_arguments(parsed_args)
        parsed_args = self._set_instances_in_namespace(parsed_args)
        return parsed_args

    def _set_instances_in_namespace(self, parsed_args: argparse.Namespace) -> argparse.Namespace:
        """Create the instances set them at their destination in the namespace.

        We now have all the constructor arguments for each instance.
        We can now sort out the dependencies, create the instances, and set them
        as attributes of the Namespace.

        Since the dataclasses might have nested children, and we need to pass
        all the constructor arguments when calling the dataclass constructors,
        we create the instances in a "bottom-up" fashion, creating the deepest
        objects first, and then setting their value in the
        `constructor_arguments` dict.

        Parameters
        ----------
        parsed_args : argparse.Namespace
            The 'raw' Namespace that is produced by `parse_args`.

        Returns
        -------
        argparse.Namespace
            The transformed namespace with the instances set at their
            corresponding destinations.
        """
        # sort the wrappers so as to construct the leaf nodes first.
        sorted_wrappers: list[DataclassWrapper] = sorted(
            self._wrappers, key=lambda w: w.nesting_level, reverse=True
        )
        D = TypeVar("D")

        def _create_dataclass_instance(
            wrapper: DataclassWrapper[D],
            constructor: Callable[..., D],
            constructor_args: dict[str, dict],
        ) -> D | None:

            # Check if the dataclass annotation is marked as Optional.
            # In this case, if no arguments were passed, and the default value is None, then return
            # None.
            if wrapper.optional and wrapper.default is None:
                for field_wrapper in wrapper.fields:
                    arg_value = constructor_args[field_wrapper.name]
                    default_value = field_wrapper.default
                    logger.debug(
                        f"field {field_wrapper.name}, arg value: {arg_value}, "
                        f"default value: {default_value}"
                    )
                    if arg_value != default_value:
                        # Value is not the default value, so an argument must have been passed.
                        # Break, and return the instance.
                        break
                else:
                    logger.debug(f"All fields for {wrapper.dest} were either default or None.")
                    return None
            elif argparse.SUPPRESS in wrapper.defaults:
                if len(constructor_args) == 0:
                    return None
                else:
                    return constructor_args

            return constructor(**constructor_args)

        for wrapper in sorted_wrappers:
            for destination in wrapper.destinations:
                # instantiate the dataclass by passing the constructor arguments
                # to the constructor.
                # TODO: for now, this might prevent users from having required
                # InitVars in their dataclasses, as we can't pass the value to
                # the constructor. Might be fine though.
                constructor = wrapper.dataclass
                constructor_args = self.constructor_arguments[destination]
                # If the dataclass wrapper is marked as 'optional' and all the
                # constructor args are None, then the instance is None.
                instance = _create_dataclass_instance(wrapper, constructor, constructor_args)

                if argparse.SUPPRESS in wrapper.defaults and instance is None:
                    logger.debug(
                        f"Suppressing entire destination {destination} because none of its"
                        f"subattributes were specified on the command line."
                    )
                elif wrapper.parent is not None:
                    parent_key, attr = utils.split_dest(destination)
                    logger.debug(
                        f"Setting a value of {instance} at attribute {attr} in "
                        f"parent at key {parent_key}."
                    )
                    self.constructor_arguments[parent_key][attr] = instance

                elif not hasattr(parsed_args, destination):
                    logger.debug(
                        f"setting attribute '{destination}' on the Namespace "
                        f"to a value of {instance}"
                    )

                    setattr(parsed_args, destination, instance)
                # There is a collision: namespace already has an entry at this destination.
                elif not self.subgroups:
                    existing = getattr(parsed_args, destination)
                    if wrapper.dest in self._defaults:
                        logger.debug(
                            f"Overwriting defaults in the namespace at destination '{destination}' "
                            f"on the Namespace ({existing}) to a value of {instance}"
                        )
                        setattr(parsed_args, destination, instance)
                    else:
                        raise RuntimeError(
                            f"Namespace should not already have a '{destination}' "
                            f"attribute!\n"
                            f"The value would be overwritten:\n"
                            f"- existing value: {existing}\n"
                            f"- new value:      {instance}"
                        )
                elif not any(wrapper.dest in subgroup_dest for subgroup_dest in self.subgroups):
                    # the current dataclass wrapper doesn't have anything to do with the subgroups.
                    existing = getattr(parsed_args, destination)
                    # This dataclass wrapper doesn't have anything to do with subgroups.
                    # BUG: The value in the args should be always the same, no?

                    if existing != instance:
                        logger.warning(
                            f"Ignoring new parsed value of {instance} for {destination}. \n"
                            f"Keeping the value that is already in the args: {existing}"
                        )
                else:
                    # The dataclass wrapper isn't directly for the subgroup: It's for a parent of
                    # the subgroup choice.

                    existing = getattr(parsed_args, destination)
                    # It's ok to overwrite the value of a subgroup choice.
                    # For instance, say its --optimizer_type "adam", then we overwrite the value
                    # at the 'optimizer' key with the value the dataclass config.

                    # TODO: Detect if this wrapper isn't related (e.g. doesn't have any subgroups.)

                    # NOTE: This is also happening here when the parent of a subgroup field, e.g.
                    # `Bob(thing="foo")`` is to be overwritten with `Bob(thing=Foo(a=123, b=2))`

                    # Should we just overwrite (set) the attribute on the existing instance?
                    # or just replace the instance entirely?
                    for subgroup_dest, subgroup_choices in self.subgroups.items():
                        # NOTE: These two cases are simpler, but don't occur here: They are
                        # handled in the FieldWrapper.
                        subgroup_parent, _, attribute = subgroup_dest.rpartition(".")

                        if wrapper.dest not in subgroup_dest:
                            # current dataclass wrapper doesn't have anything to do with this
                            # subgroup. Go to the next subgroup.
                            continue

                        elif subgroup_parent == destination:
                            # Replace the attribute that changed on the dataclass instance.
                            current_value = getattr(existing, attribute)
                            new_value = getattr(instance, attribute)

                            if (
                                isinstance(current_value, str)
                                and current_value in subgroup_choices
                                and not isinstance(new_value, str)
                            ):
                                # Replacing the subgroup name with the dataclass instance.
                                logger.debug(
                                    f"Overwriting attribute {attribute} on {existing} from "
                                    f"{current_value} -> {new_value}."
                                )
                                existing = dataclasses.replace(existing, **{attribute: new_value})
                                setattr(parsed_args, destination, existing)
                        elif subgroup_dest.startswith(wrapper.dest + "."):
                            # subgroup overwrites an attribute in the child of the existing
                            # dataclass.
                            path_from_parent_to_child = subgroup_dest[len(wrapper.dest + ".") :]
                            parts = path_from_parent_to_child.split(".")

                            from simple_parsing.utils import (
                                getattr_recursive,
                                setattr_recursive,
                            )

                            existing_config = getattr_recursive(existing, path_from_parent_to_child)
                            new_config = getattr_recursive(instance, path_from_parent_to_child)
                            if existing_config == new_config:
                                continue

                            if (
                                isinstance(existing_config, str)
                                and existing_config in subgroup_choices
                                and not isinstance(new_config, str)
                            ):
                                attribute = parts[-1]
                                # TODO: This won't work if the dataclasses are frozen! We need some
                                # kind of recursive replace function.
                                logger.debug(
                                    f"Overwriting attribute {attribute} on {existing} to {new_config}."
                                )
                                setattr_recursive(existing, path_from_parent_to_child, new_config)

                        else:
                            raise RuntimeError(
                                "Something went wrong while trying to update the value of a \n"
                                "subgroup in the args! Please report this bug by opening an issue!"
                            )

                # TODO: not needed, but might be a good thing to do?
                # remove the 'args dict' for this child class.
                self.constructor_arguments.pop(destination)

        assert not self.constructor_arguments
        return parsed_args

    def _consume_constructor_arguments(self, parsed_args: argparse.Namespace) -> argparse.Namespace:
        """Create the constructor arguments for each instance.

        Creates the arguments by consuming all the attributes from
        `parsed_args`.
        Here we imitate a custom action, by having the FieldWrappers be
        callables that set their value in the `constructor_args` attribute.

        Parameters
        ----------
        parsed_args : argparse.Namespace
            the argparse.Namespace returned from super().parse_args().

        Returns
        -------
        argparse.Namespace
            The namespace, without the consumed arguments.
        """
        parsed_arg_values = vars(parsed_args)
        for wrapper in self._wrappers:
            for field in wrapper.fields:
                if argparse.SUPPRESS in wrapper.defaults and field.dest not in parsed_args:
                    continue

                if not field.field.init:
                    # The field isn't an argument of the dataclass constructor.
                    continue
                values = parsed_arg_values.get(field.dest, field.default)

                # call the "action" for the given attribute. This sets the right
                # value in the `self.constructor_arguments` dictionary.
                field(parser=self, namespace=parsed_args, values=values)

        # "Clean up" the Namespace by returning a new Namespace without the
        # consumed attributes.
        deleted_values: dict[str, Any] = {}
        for wrapper in self._wrappers:
            for field in wrapper.fields:
                value = parsed_arg_values.pop(field.dest, None)
                deleted_values[field.dest] = value

        leftover_args = argparse.Namespace(**parsed_arg_values)
        if deleted_values:
            logger.debug(f"deleted values: {deleted_values}")
            logger.debug(f"leftover args: {leftover_args}")
        return leftover_args


T = TypeVar("T")


def parse(
    config_class: type[Dataclass],
    config_path: Path | str | None = None,
    args: str | Sequence[str] | None = None,
    default: Dataclass | None = None,
    dest: str = "config",
    *,
    prefix: str = "",
    nested_mode: NestedMode = NestedMode.WITHOUT_ROOT,
    conflict_resolution: ConflictResolution = ConflictResolution.AUTO,
    add_option_string_dash_variants: DashVariant = DashVariant.AUTO,
    argument_generation_mode=ArgumentGenerationMode.FLAT,
    formatter_class: type[HelpFormatter] = SimpleHelpFormatter,
    add_config_path_arg: bool | None = None,
) -> Dataclass:
    """Parse the given dataclass from the command-line.

    See the `ArgumentParser` constructor for more details on the arguments (they are the same here
    except for `nested_mode`, which has a different default value).

    If `config_path` is passed, loads the values from that file and uses them as defaults.
    """
    parser = ArgumentParser(
        nested_mode=nested_mode,
        add_help=True,
        # add_config_path_arg=None,
        config_path=config_path,
        conflict_resolution=conflict_resolution,
        add_option_string_dash_variants=add_option_string_dash_variants,
        argument_generation_mode=argument_generation_mode,
        formatter_class=formatter_class,
        add_config_path_arg=add_config_path_arg,
    )

    parser.add_arguments(config_class, prefix=prefix, dest=dest, default=default)

    if isinstance(args, str):
        args = shlex.split(args)
    parsed_args = parser.parse_args(args)

    config: Dataclass = getattr(parsed_args, dest)
    return config


def parse_known_args(
    config_class: type[Dataclass],
    config_path: Path | str | None = None,
    args: str | Sequence[str] | None = None,
    default: Dataclass | None = None,
    dest: str = "config",
    attempt_to_reorder: bool = False,
    *,
    nested_mode: NestedMode = NestedMode.WITHOUT_ROOT,
    conflict_resolution: ConflictResolution = ConflictResolution.AUTO,
    add_option_string_dash_variants: DashVariant = DashVariant.AUTO,
    argument_generation_mode=ArgumentGenerationMode.FLAT,
    formatter_class: type[HelpFormatter] = SimpleHelpFormatter,
    add_config_path_arg: bool | None = None,
) -> tuple[Dataclass, list[str]]:
    """Parse the given dataclass from the command-line, returning the leftover arguments.

    See the `ArgumentParser` constructor for more details on the arguments (they are the same here
    except for `nested_mode`, which has a different default value).

    If `config_path` is passed, loads the values from that file and uses them as defaults.
    """

    if isinstance(args, str):
        args = shlex.split(args)
    parser = ArgumentParser(
        nested_mode=nested_mode,
        add_help=True,
        # add_config_path_arg=None,
        config_path=config_path,
        conflict_resolution=conflict_resolution,
        add_option_string_dash_variants=add_option_string_dash_variants,
        argument_generation_mode=argument_generation_mode,
        formatter_class=formatter_class,
        add_config_path_arg=add_config_path_arg,
    )
    parser.add_arguments(config_class, dest=dest, default=default)
    parsed_args, unknown_args = parser.parse_known_args(args, attempt_to_reorder=attempt_to_reorder)
    config: Dataclass = getattr(parsed_args, dest)
    return config, unknown_args
