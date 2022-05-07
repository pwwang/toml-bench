from typing import Any
from ..case import TestCase, TestCaseDummy


class TestDumpsUnicodeDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)
        v1 = {"你好": "世界"}
        try:
            return self.api.dumps(v1)
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        return f"`{replace_newline(str(out))}`"


class TestDumpsUnicode(TestCase):
    """How the package dumps Unicode in python,
    literally, `<api>.dumps({"你好": "世界"})`"""

    HEADER = "Dumped value"
    DUMMY_CLASS = TestDumpsUnicodeDummy


class TestLoadUnicodeDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)
        try:
            with open(case.datafile, "r", encoding="utf-8") as f:
                return self.api.load(f)
        except Exception as e:
            return e

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        return f"`{replace_newline(str(out))}`"


class TestLoadUnicode(TestCase):
    """How the package loads a file with unicode.

    # Create a file with unicode content
    with open(self.datafile, "w", encoding="utf-8") as f:
        f.write('"你好" = "世界"\\n')

    # Use `<api>.load()` to load the file
    with open(self.datafile, "r", encoding="utf-8") as f:
        loaded = self.api.load(f)
    """

    HEADER = "Loaded as"
    DUMMY_CLASS = TestLoadUnicodeDummy

    def __init__(self) -> None:
        super().__init__()
        self.datafile = None

    def prepare(self) -> None:
        super().prepare()
        self.datafile = self.args.datadir / "unicode" / "unicode.toml"
        self.datafile.parent.mkdir(parents=True, exist_ok=True)
        with open(self.datafile, "w", encoding="utf-8") as f:
            f.write('"你好" = "世界"\n')
