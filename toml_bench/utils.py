import sys
import math
import logging
import json
from os import PathLike
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Any, Callable, Mapping, Type

from dateutil import parser

# logger
logger = logging.getLogger("toml-bench")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(
    logging.Formatter(
        "[%(asctime)s][%(levelname)7s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)
logger.addHandler(stream_handler)


def load_subpkgs(dire: PathLike) -> Mapping[str, ModuleType]:
    """Get all packages and the module from .packages"""
    out = {}
    for path in Path(__file__).parent.joinpath(dire).glob("*.py"):
        if path.name.startswith("_"):
            continue

        out[path.stem] = import_module(
            f".{dire}.{path.stem}",
            package=__package__,
        )

    return out


def get_object(
    module: ModuleType,
    checker: Callable[[Any], bool],
    multi: bool = False,
) -> Any:
    """Get object from a module with a checker"""
    out = [] if multi else None
    for attr in dir(module):
        if attr.startswith("_"):
            continue

        obj = getattr(module, attr)
        if checker(obj):
            if not multi:
                return obj
            out.append(obj)

    return out


def doc_formatter(**kwargs: Any) -> Callable[[Type], Type]:
    """Format docstring of a class"""

    def decorator(cls: Type) -> Type:
        cls.__doc__ = cls.__doc__ % kwargs
        return cls

    return decorator


class NAN:
    def __eq__(self, other):
        return math.isnan(other)

    def __ne__(self, other):
        return not math.isnan(other)


def _cast_value(value: Any) -> Any:
    if isinstance(value, list):
        return [_cast_value(v) for v in value]
    if not isinstance(value, dict):
        return value

    out = value.copy()
    if len(value) == 2 and "value" in value and "type" in value:
        if value["type"] == "integer":
            return int(value["value"])
        if value["type"] == "array":
            return [_cast_value(v) for v in value["value"]]
        if value["type"] == "string":
            return str(value["value"])
        if value["type"] == "float":
            out = float(value["value"])
            if math.isnan(out):
                out = NAN()
            return out
        if value["type"] == "bool":
            return value["value"] == "true"
        if value["type"] == "datetime":
            return parser.isoparse(value["value"])
        if value["type"] == "datetime-local":
            return parser.parse(value["value"])
        if value["type"] == "date":
            return parser.isoparse(value["value"]).date()
        if value["type"] == "date-local":
            return parser.parse(value["value"]).date()
        if value["type"] == "time":
            return parser.isoparse(value["value"]).time()
        if value["type"] == "time-local":
            return parser.parse(value["value"]).time()

        return out["value"]

    for key, val in value.items():
        out[key] = _cast_value(val)
    return out


def load_json_data(file) -> Mapping[str, Any]:
    data = json.load(file)
    return _cast_value(data)
