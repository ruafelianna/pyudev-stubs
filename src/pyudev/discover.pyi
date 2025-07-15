from abc import abstractmethod
from collections.abc import Callable
from typing import Any

from .core import Context
from .device import Device

def wrap_exception[TFunc : Callable[..., Any]](func : TFunc) -> TFunc: ...

class Hypothesis[TMatch]:
    @classmethod
    @abstractmethod
    def match(cls, value : str) -> TMatch | None: ...

    @classmethod
    @abstractmethod
    def lookup(cls, context : Context, key : TMatch) -> frozenset[Device]: ...

    @classmethod
    def setup(cls, context : Context) -> None: ...

    @classmethod
    def get_devices(cls, context : Context, value : str) -> set[Device]: ...

class DeviceNumberHypothesis(Hypothesis[int]):
    @classmethod
    def _match_major_minor(cls, value : str) -> int | None: ...

    @classmethod
    def _match_number(cls, value : str) -> int | None: ...

    @classmethod
    def match(cls, value : str) -> int | None: ...

    @classmethod
    def find_subsystems(cls, context : Context) -> list[str]: ...

    @classmethod
    def lookup(cls, context : Context, key : int) -> frozenset[Device]: ...

class DevicePathHypothesis(Hypothesis[str]):
    @classmethod
    def match(cls, value : str) -> str | None: ...

    @classmethod
    def lookup(cls, context : Context, key : str) -> frozenset[Device]: ...

class DeviceNameHypothesis(Hypothesis[str]):
    @classmethod
    def find_subsystems(cls, context : Context) -> frozenset[str]: ...

    @classmethod
    def match(cls, value : str) -> str | None: ...

    @classmethod
    def lookup(cls, context : Context, key : str) -> frozenset[Device]: ...

class DeviceFileHypothesis(Hypothesis[str]):
    _LINK_DIRS : list[str]

    @classmethod
    def get_link_dirs(cls, context : Context) -> list[str]: ...

    @classmethod
    def setup(cls, context : Context) -> None: ...

    @classmethod
    def match(cls, value : str) -> str: ...

    @classmethod
    def lookup(cls, context : Context, key : str) -> frozenset[Device]: ...

class Discovery:
    _HYPOTHESES : list[Hypothesis[Any]]

    def __init__(self) -> None: ...

    def setup(self, context : Context) -> None: ...

    def get_devices(self, context : Context, value : str) -> frozenset[Device]: ...
