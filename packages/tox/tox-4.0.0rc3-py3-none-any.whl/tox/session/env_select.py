from __future__ import annotations

from argparse import ArgumentParser
from collections import Counter
from dataclasses import dataclass
from itertools import chain
from typing import TYPE_CHECKING, Any, Dict, Iterable, Iterator, List, cast

from tox.config.loader.str_convert import StrConvert
from tox.tox_env.api import ToxEnvCreateArgs
from tox.tox_env.register import REGISTER
from tox.tox_env.runner import RunToxEnv

from ..config.loader.memory import MemoryLoader
from ..config.types import EnvList
from ..report import HandledError
from ..tox_env.errors import Skip
from ..tox_env.package import PackageToxEnv

if TYPE_CHECKING:
    from tox.session.state import State


class CliEnv:
    """CLI tox env selection"""

    def __init__(self, value: None | list[str] | str = None):
        if isinstance(value, str):
            value = StrConvert().to(value, of_type=List[str], factory=None)
        self._names: list[str] | None = value

    def __iter__(self) -> Iterator[str]:
        if not self.is_all and self._names is not None:  # pragma: no branch
            yield from self._names

    def __str__(self) -> str:
        return "ALL" if self.is_all else ("<env_list>" if self.is_default_list else ",".join(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({'' if self.is_default_list else repr(str(self))})"

    def __eq__(self, other: Any) -> bool:
        return type(self) == type(other) and self._names == other._names

    def __ne__(self, other: Any) -> bool:
        return not (self == other)

    @property
    def is_all(self) -> bool:
        return self._names is not None and "ALL" in self._names

    @property
    def is_default_list(self) -> bool:
        return not (self._names or [])


def register_env_select_flags(
    parser: ArgumentParser,
    default: CliEnv | None,
    multiple: bool = True,
    group_only: bool = False,
) -> ArgumentParser:
    """
    Register environment selection flags.

    :param parser: the parser to register to
    :param default: the default value for env selection
    :param multiple: allow selecting multiple environments
    :param group_only:
    :return:
    """
    if multiple:
        group = parser.add_argument_group("select target environment(s)")
        add_to: ArgumentParser = group.add_mutually_exclusive_group(required=False)  # type: ignore
    else:
        add_to = parser
    if not group_only:
        if multiple:
            help_msg = "enumerate (ALL -> all environments, not set -> use <env_list> from config)"
        else:
            help_msg = "environment to run"
        add_to.add_argument("-e", dest="env", help=help_msg, default=default, type=CliEnv)
    if multiple:
        help_msg = "labels to evaluate"
        add_to.add_argument("-m", dest="labels", metavar="label", help=help_msg, default=[], type=str, nargs="+")
        help_msg = "factors to evaluate"
        add_to.add_argument("-f", dest="factors", metavar="factor", help=help_msg, default=[], type=str, nargs="+")
    return add_to


@dataclass
class _ToxEnvInfo:
    """tox environment information"""

    env: PackageToxEnv | RunToxEnv  #: the tox environment
    is_active: bool  #: a flag indicating if the environment is marked as active in the current run
    package_skip: tuple[str, Skip] | None = None  #: if set the creation of the packaging environment failed


class EnvSelector:
    def __init__(self, state: State) -> None:
        # needs core to load the default tox environment list
        # to load the package environments of a run environments we need the run environment builder
        # to load labels we need core + the run environment
        self.on_empty_fallback_py = True
        self._state = state
        self._cli_envs: CliEnv | None = getattr(self._state.conf.options, "env", None)
        self._defined_envs_: None | dict[str, _ToxEnvInfo] = None
        self._pkg_env_counter: Counter[str] = Counter()
        from tox.plugin.manager import MANAGER

        self._manager = MANAGER
        self._log_handler = self._state._options.log_handler
        self._journal = self._state._journal
        self._provision: None | tuple[bool, str, MemoryLoader] = None

        self._state.conf.core.add_config("labels", Dict[str, EnvList], {}, "core labels")

    def _collect_names(self) -> Iterator[tuple[Iterable[str], bool]]:
        """:return: sources of tox environments defined with name and if is marked as target to run"""
        if self._provision is not None:  # pragma: no branch
            yield (self._provision[1],), False
        env_list, everything_active = self._state.conf.core["env_list"], False
        if self._cli_envs is None or self._cli_envs.is_default_list:
            yield env_list, True
        elif self._cli_envs.is_all:
            everything_active = True
        else:
            yield self._cli_envs, True
        yield self._state.conf, everything_active
        label_envs = dict.fromkeys(chain.from_iterable(self._state.conf.core["labels"].values()))
        if label_envs:
            yield label_envs.keys(), False

    def _env_name_to_active(self) -> dict[str, bool]:
        env_name_to_active_map = {}
        for a_collection, is_active in self._collect_names():
            for name in a_collection:
                if name not in env_name_to_active_map:
                    env_name_to_active_map[name] = is_active
        # for factor/label selection update the active flag
        if not (getattr(self._state.conf.options, "labels", []) or getattr(self._state.conf.options, "factors", [])):
            # if no active environment is defined fallback to py
            if self.on_empty_fallback_py and not any(env_name_to_active_map.values()):
                env_name_to_active_map["py"] = True
        return env_name_to_active_map

    @property
    def _defined_envs(self) -> dict[str, _ToxEnvInfo]:
        # The problem of classifying run/package environments:
        # There can be two type of tox environments: run or package. Given a tox environment name there's no easy way to
        # find out which it is.  Intuitively a run environment is any environment that's not used for packaging by
        # another run environment. To find out what are the packaging environments for a run environment you have to
        # first construct it. This implies a two phase solution: construct all environments and query their packaging
        # environments. The run environments are the ones not marked as of packaging type. This requires being able
        # to change tox environments type, if it was earlier discovered as a run environment and is marked as packaging
        # we need to redefine it, e.g. when it shows up in config as [testenv:.package] and afterwards by a run env is
        # marked as package_env.

        if self._defined_envs_ is None:
            self._defined_envs_ = {}
            failed: dict[str, Exception] = {}
            env_name_to_active = self._env_name_to_active()
            for name, is_active in env_name_to_active.items():
                if name in self._pkg_env_counter:  # already marked as packaging, nothing to do here
                    continue
                with self._log_handler.with_context(name):
                    run_env = self._build_run_env(name)
                    if run_env is None:
                        continue
                    self._defined_envs_[name] = _ToxEnvInfo(run_env, is_active)
                    pkg_name_type = run_env.get_package_env_types()
                if pkg_name_type is not None:
                    # build package env and assign it, then register the run environment which can trigger generation
                    # of additional run environments
                    start_package_env_use_counter = self._pkg_env_counter.copy()
                    try:
                        run_env.package_env = self._build_pkg_env(pkg_name_type, name, env_name_to_active)
                    except Exception as exception:
                        # if it's not a run environment,  wait to see if ends up being a packaging one -> rollback
                        failed[name] = exception
                        for key in self._pkg_env_counter - start_package_env_use_counter:
                            del self._defined_envs_[key]
                            self._state.conf.clear_env(key)
                        self._pkg_env_counter = start_package_env_use_counter
                        del self._defined_envs_[name]
                        self._state.conf.clear_env(name)
                    else:
                        try:
                            for env in run_env.package_envs:
                                # check if any packaging envs are already run and remove them
                                other_env_info = self._defined_envs_.get(env.name)
                                if other_env_info is not None and isinstance(other_env_info.env, RunToxEnv):
                                    del self._defined_envs_[env.name]  # pragma: no cover
                                    for _pkg_env in other_env_info.env.package_envs:  # pragma: no cover
                                        self._pkg_env_counter[_pkg_env.name] -= 1  # pragma: no cover
                        except Exception:
                            assert self._defined_envs_[name].package_skip is not None
            failed_to_create = failed.keys() - self._defined_envs_.keys()
            if failed_to_create:
                raise failed[next(iter(failed_to_create))]
            for name, count in self._pkg_env_counter.items():
                if not count:
                    self._defined_envs_.pop(name)  # pragma: no cover

            # reorder to as defined rather as found
            order = chain(env_name_to_active, (i for i in self._defined_envs_ if i not in env_name_to_active))
            self._defined_envs_ = {name: self._defined_envs_[name] for name in order if name in self._defined_envs_}
            self._finalize_config()
            self._mark_active()
        return self._defined_envs_

    def _finalize_config(self) -> None:
        assert self._defined_envs_ is not None
        for tox_env in self._defined_envs_.values():
            tox_env.env.conf.mark_finalized()
        self._state.conf.core.mark_finalized()

    def _build_run_env(self, name: str) -> RunToxEnv | None:
        if self._provision is not None and self._provision[0] is False and name == self._provision[1]:
            return None
        env_conf = self._state.conf.get_env(
            name,
            package=False,
            loaders=[self._provision[2]] if self._provision is not None and self._provision[1] == name else None,
        )
        desc = "the tox execute used to evaluate this environment"
        env_conf.add_config(keys="runner", desc=desc, of_type=str, default=self._state.conf.options.default_runner)
        runner = REGISTER.runner(cast(str, env_conf["runner"]))
        journal = self._journal.get_env_journal(name)
        args = ToxEnvCreateArgs(env_conf, self._state.conf.core, self._state.conf.options, journal, self._log_handler)
        run_env = runner(args)
        self._manager.tox_add_env_config(env_conf, self._state)
        return run_env

    def _build_pkg_env(self, name_type: tuple[str, str], run_env_name: str, active: dict[str, bool]) -> PackageToxEnv:
        name, core_type = name_type
        with self._log_handler.with_context(name):
            if run_env_name == name:
                raise HandledError(f"{run_env_name} cannot self-package")
            missing_active = self._cli_envs is not None and self._cli_envs.is_all
            try:
                package_tox_env = self._get_package_env(core_type, name, active.get(name, missing_active))
                self._pkg_env_counter[name] += 1
                run_env: RunToxEnv = self._defined_envs_[run_env_name].env  # type: ignore
                child_package_envs = package_tox_env.register_run_env(run_env)
                try:
                    name_type = next(child_package_envs)
                    while True:
                        child_pkg_env = self._build_pkg_env(name_type, run_env_name, active)
                        self._pkg_env_counter[name_type[0]] += 1
                        name_type = child_package_envs.send(child_pkg_env)
                except StopIteration:
                    pass
            except Skip as exception:
                assert self._defined_envs_ is not None
                self._defined_envs_[run_env_name].package_skip = (name_type[0], exception)
            return package_tox_env

    def _get_package_env(self, packager: str, name: str, is_active: bool) -> PackageToxEnv:
        assert self._defined_envs_ is not None
        if name in self._defined_envs_:
            env = self._defined_envs_[name].env
            if isinstance(env, PackageToxEnv):
                if env.id() != packager:  # pragma: no branch # same env name is used by different packaging
                    msg = f"{name} is already defined as a {env.id()}, cannot be {packager} too"  # pragma: no cover
                    raise HandledError(msg)  # pragma: no cover
                return env
            else:
                self._state.conf.clear_env(name)
        package_type = REGISTER.package(packager)
        pkg_conf = self._state.conf.get_env(name, package=True)
        journal = self._journal.get_env_journal(name)
        args = ToxEnvCreateArgs(pkg_conf, self._state.conf.core, self._state.conf.options, journal, self._log_handler)
        pkg_env: PackageToxEnv = package_type(args)
        self._defined_envs_[name] = _ToxEnvInfo(pkg_env, is_active)
        self._manager.tox_add_env_config(pkg_conf, self._state)
        return pkg_env

    def _mark_active(self) -> None:
        labels = set(getattr(self._state.conf.options, "labels", []))
        factors = set(getattr(self._state.conf.options, "factors", []))
        assert self._defined_envs_ is not None
        if labels or factors:
            for env_info in self._defined_envs_.values():
                env_info.is_active = False  # if any was selected reset
            if labels:
                for label in labels:
                    for env_name in self._state.conf.core["labels"].get(label, []):
                        self._defined_envs_[env_name].is_active = True
                for env_info in self._defined_envs_.values():
                    if labels.intersection(env_info.env.conf["labels"]):
                        env_info.is_active = True
            if self._state.conf.options.factors:  # if matches mark it active
                for name, env_info in self._defined_envs_.items():
                    if factors.issubset(set(name.split("-"))):
                        env_info.is_active = True

    def __getitem__(self, item: str) -> RunToxEnv | PackageToxEnv:
        """
        :param item: the name of the environment
        :return: the tox environment
        """
        return self._defined_envs[item].env

    def iter(
        self,
        *,
        only_active: bool = True,
        package: bool = False,
    ) -> Iterator[str]:
        """
        Get tox environments.

        :param only_active: active environments are marked to be executed in the current target
        :param package: return package environments

        :return: an iteration of tox environments
        """
        ignore_envs: set[str] = set()
        for name, env_info in self._defined_envs.items():
            if only_active and not env_info.is_active:
                continue
            if not package and not isinstance(env_info.env, RunToxEnv):
                continue
            yield name
            ignore_envs.add(name)

    def ensure_only_run_env_is_active(self) -> None:
        envs, active = self._defined_envs, self._env_name_to_active()
        invalid = [n for n, a in active.items() if a and isinstance(envs[n].env, PackageToxEnv)]
        if invalid:
            raise HandledError(f"cannot run packaging environment(s) {','.join(invalid)}")

    def _mark_provision(self, on: bool, provision_tox_env: str, loader: MemoryLoader) -> None:
        self._provision = on, provision_tox_env, loader


__all__ = [
    "register_env_select_flags",
    "EnvSelector",
    "CliEnv",
]
