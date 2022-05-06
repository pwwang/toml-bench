from abc import ABC
from types import ModuleType
import importlib_metadata as im

from typing import Any, Mapping, TYPE_CHECKING


if TYPE_CHECKING:
    from os import PathLike


APIs = {}


class API(ABC):

    package = None
    repo = ""

    @classmethod
    def __init_subclass__(cls) -> None:
        APIs[cls.__module__.split(".")[-1]] = cls(cls.package)

    def __init__(self, package: ModuleType) -> None:
        self.package = package

    def load(self, path: "PathLike") -> Mapping[str, Any]:
        return self.package.load(path)

    def dumps(self, data: Mapping[str, Any]) -> str:
        return self.package.dumps(data)

    def loads(self, data: str) -> Mapping[str, Any]:
        return self.package.loads(data)

    def dump(self, data: Mapping[str, Any], path: "PathLike") -> None:
        self.package.dump(data, path)

    def version(self) -> str:
        return im.version(self.package.__name__)
