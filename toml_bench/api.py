from __future__ import annotations

import sys
from abc import ABC, abstractproperty
from typing import TYPE_CHECKING, Any, Mapping

import importlib_metadata as im
from benchwork import BenchAPI

import qtoml
import rtoml
import toml
import tomli
import tomli_w
import tomlkit

try:
    import pytomlpp
except ImportError:
    pytomlpp = None

try:
    import tomllib
except ImportError:
    tomllib = None

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
    loads = lambda self, data: tomli.loads(data)  # noqa: E731
    load = lambda self, f: tomli.load(f)  # noqa: E731

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


if pytomlpp:
    class PyTOMLPPAPI(APIBase):
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


if tomllib:
    class TOMLLibAPI(APIBase):
        OPEN_FLAG = "rb"

        _name = "tomllib"
        package = tomllib
        repo = "https://docs.python.org/3/library/tomllib.html"

        @property
        def version(self) -> str:
            return (
                "(Python "
                f"{sys.version_info.major}."
                f"{sys.version_info.minor}."
                f"{sys.version_info.micro})"
            )

        def dumps(self, data: Mapping[str, Any]) -> str:
            raise NotImplementedError("Dumping not supported")

        def dump(self, data: Mapping[str, Any], path: PathLike) -> None:
            raise NotImplementedError("Dumping not supported")
