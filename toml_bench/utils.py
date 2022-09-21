
import json
import math
from typing import Any, Mapping
from dateutil import parser


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
