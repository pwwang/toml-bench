from __future__ import annotations

from abc import ABC, abstractproperty
from typing import TYPE_CHECKING, Any, Mapping

import importlib_metadata as im
from benchwork import BenchAPI

import pytomlpp
import qtoml
import rtoml
import toml
import tomli
import tomli_w
import tomlkit

if TYPE_CHECKING:
    from os import PathLike
    from types import ModuleType


class APIBase(BenchAPI, ABC):
    _SUBCLASSES = None
    OPEN_FLAG = "r"

    @abstractproperty
    def package(self) -> ModuleType:
        ...

    @abstractproperty
    def repo(self) -> str:
        ...

    @abstractproperty
    def _name(self) -> str:
        ...

    @property
    def name(self) -> str:
        return f'<a target="_blank" href="{self.repo}">{self._name}</a>'

    def load(self, path: PathLike) -> Mapping[str, Any]:
        return self.package.load(path)

    def dumps(self, data: Mapping[str, Any]) -> str:
        return self.package.dumps(data)

    def loads(self, data: str) -> Mapping[str, Any]:
        return self.package.loads(data)

    def dump(self, data: Mapping[str, Any], path: PathLike) -> None:
        self.package.dump(data, path)

    @property
    def version(self) -> str:
        return im.version(self.package.__name__)


class TOMLAPI(APIBase):
    _name = "toml"
    package = toml
    repo = "https://github.com/uiri/toml"


class TOMLiAPI(APIBase):
    OPEN_FLAG = "rb"
    _name = "tomli/tomli_w"
    package = tomli_w
    repo = "https://github.com/hukkin/tomli"
    loads = lambda self, data: tomli.loads(data)
    load = lambda self, f: tomli.load(f)

    @property
    def version(self) -> str:
        return (
            f"{im.version('tomli')}; "
            f"**tomli_w**: {im.version(self.package.__name__)}"
        )


class TOMLKitAPI(APIBase):
    _name = "tomlkit"
    package = tomlkit
    repo = "https://github.com/sdispater/tomlkit"

    def load(self, f):
        content = f.read()
        return tomlkit.loads(content)


class PyTOMLAPI(APIBase):
    _name = "pytomlpp"
    package = pytomlpp
    repo = "https://github.com/bobfang1992/pytomlpp"


class RTOMLAPI(APIBase):
    _name = "rtoml"
    package = rtoml
    repo = "https://github.com/samuelcolvin/rtoml"


class QTOMLAPI(APIBase):
    _name = "qtoml"
    package = qtoml
    repo = "https://github.com/alethiophile/qtoml"
