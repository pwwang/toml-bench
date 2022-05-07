from typing import Any
from ..case import TestCase, TestCaseDummy


class TestDumpNoneDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)
        try:
            return self.api.dumps(None)
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        if isinstance(out, Exception):
            return f"Raises {replace_newline(str(out))}"
        return f"Dumps to `{out!r}`"


class TestDumpNone(TestCase):
    """How the package dumps `None` value in python,
    literally `<package>.dumps(None)`
    """

    HEADER = "Dumped value or error"
    DUMMY_CLASS = TestDumpNoneDummy


class TestDumpValueNoneDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)
        try:
            return self.api.dumps({"key": None})
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        if isinstance(out, Exception):
            return f"Raises {replace_newline(str(out))}"
        if out == "":
            return "Ignores the key (dumps to an empty string)"
        return f"Dumps to `{replace_newline(out)}`"


class TestDumpValueNone(TestCase):
    """How the package dumps key-value pair with value `None`,
    literally `<package>.dumps({"key": None})`
    """

    HEADER = "Dumped value or error"
    DUMMY_CLASS = TestDumpValueNoneDummy


class TestLoadNoneLikeDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)
        try:
            return self.api.loads('v1 = "null"\nv2 = "None"')
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        return f"`{out!r}`"


class TestLoadNoneLike(TestCase):
    """How the package loads `None`-like value in string,
    literally `<package>.loads('v1 = "null"\nv2 = "None"')`
    """

    HEADER = "Loaded as"
    DUMMY_CLASS = TestLoadNoneLikeDummy
