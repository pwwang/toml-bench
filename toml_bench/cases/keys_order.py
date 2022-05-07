from typing import Any
from ..case import TestCase, TestCaseDummy


class TestDumpKeysOrderDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)

        v1 = {"a": 1, "b": 2, "c": 3}
        v2 = {"b": 1, "c": 2, "a": 3}
        v3 = {"c": 1, "a": 2, "b": 3}

        return [self.api.dumps(v1), self.api.dumps(v2), self.api.dumps(v3)]

    def result(self, out: Any) -> str:
        e1 = "a = 1\nb = 2\nc = 3\n"
        e2 = "b = 1\nc = 2\na = 3\n"
        e3 = "c = 1\na = 2\nb = 3\n"
        if out[0] == e1 and out[1] == e2 and out[2] == e3:
            return "Kept"
        return "Lost"


class TestDumpKeysOrder(TestCase):
    """Whether the package preserves the order of the keys while dumps
    a python dictionary. Thus, whether
    `<package>.dumps({"c": 1, "a": 2, "b": 3})` yields
    a string like `c = 1\\na = 2\\nb = 3\\n`.
    """

    HEADER = "Keys order kept?"
    DUMMY_CLASS = TestDumpKeysOrderDummy


class TestLoadKeysOrderDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)

        v1 = "a = 1\nb = 2\nc = 3\n"
        v2 = "b = 1\nc = 2\na = 3\n"
        v3 = "c = 1\na = 2\nb = 3\n"

        return [self.api.loads(v1), self.api.loads(v2), self.api.loads(v3)]

    def result(self, out: Any) -> str:
        e1 = ["a", "b", "c"]
        e2 = ["b", "c", "a"]
        e3 = ["c", "a", "b"]

        if list(out[0]) == e1 and list(out[1]) == e2 and list(out[2]) == e3:
            return "Kept"
        return "Lost"


class TestLoadKeysOrder(TestCase):
    """Whether the package preserves the order of the keys while loads
    a TOML string. Thus, whether
    `<package>.loads('c = 1\na = 2\nb = 3\n')` yields a dictionary
    with keys in the order of `['c', 'a', 'b']`.
    """

    HEADER = "Keys order kept?"
    DUMMY_CLASS = TestLoadKeysOrderDummy
