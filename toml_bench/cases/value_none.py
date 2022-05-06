from email import header
from typing import Any
from ..case import TestCase
from ..api import APIs


class TestDumpNone(TestCase):
    """How the package dumps `None` value in python,
    literally `<package>.dumps(None)`
    """
    header = "Dumped value or error"

    def run(self, casename: str, name: str) -> Any:
        super().run(casename, name)
        api = APIs[name]
        try:
            return api.dumps(None)
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        if isinstance(out, Exception):
            return f"Raises {replace_newline(str(out))}"
        return f"Dumps to `{out}`"


class TestDumpValueNone(TestCase):
    """How the package dumps key-value pair with value `None`,
    literally `<package>.dumps({"key": None})`
    """
    header = "Dumped value or error"

    def run(self, casename: str, name: str) -> Any:
        super().run(casename, name)
        api = APIs[name]
        try:
            return api.dumps({"key": None})
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        if isinstance(out, Exception):
            return f"Raises {replace_newline(str(out))}"
        if out == "":
            return "Ignores the key (dumps to an empty string)"
        return f"Dumps to `{replace_newline(out)}`"


class TestLoadNoneLike(TestCase):
    """How the package loads `None`-like value in string,
    literally `<package>.loads('v1 = "null"\nv2 = "None"')`
    """
    header = "Loaded as"

    def run(self, casename: str, name: str) -> Any:
        super().run(casename, name)
        api = APIs[name]
        try:
            return api.loads('v1 = "null"\nv2 = "None"')
        except Exception as e:
            return e
