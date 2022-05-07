import zipfile
import urllib.request
from pathlib import Path
from typing import Any

from ..case import TestCase, TestCaseDummy
from ..utils import doc_formatter, load_json_data


TOML_TEST_REPO = (
    # "https://github.com/BurntSushi/toml-test/archive/refs/tags/v1.1.0.zip"
    "https://github.com/BurntSushi/toml-test/"
)

TEST_FILE_PREFIX = (
    "https://github.com/BurntSushi/toml-test/blob/v%(ver)s/tests/"
)


class TestComplianceDummy(TestCaseDummy):

    OPEN_FLAG = "rb"
    KIND = "valid"

    def __init__(self) -> None:
        super().__init__()
        self.total = 0

    def _runfile(
        self,
        tomlfile: Path,
        subdir: bool = False,
    ) -> Any:
        self.total += 1
        filename = (
            tomlfile.name
            if not subdir
            else f"{tomlfile.parent.name}/{tomlfile.name}"
        )
        url = (
            f"{TEST_FILE_PREFIX % {'ver': self.args.comver}}"
            f"/{self.__class__.KIND}/{filename}"
        )
        with tomlfile.open(self.__class__.OPEN_FLAG) as f:
            try:
                data = self.api.load(f)
            except Exception as e:
                return Exception(f"[{filename}]({url}) {e}")
        with tomlfile.with_suffix(".json").open("r") as f:
            expect = load_json_data(f)

        try:
            assert (
                data == expect
            ), f"[{filename}]({url}) Parsed as unexpected data."
        except AssertionError as e:
            return e

    def run(self, case: "TestCase") -> Any:
        super().run(case)
        errors = []
        kind = self.__class__.KIND
        for tomlfile in case.datadir.joinpath("tests", kind).glob("*.toml"):
            out = self._runfile(tomlfile)
            if out is not None:
                errors.append(out)

        for tomlfile in case.datadir.joinpath("tests", kind).glob("*/*.toml"):
            out = self._runfile(tomlfile, subdir=True)
            if out is not None:
                errors.append(out)
        return errors

    def result(self, out: Any) -> str:
        if not out:
            return f"OK, *{self.total}/{self.total} (100%) passed*"

        passed = self.total - len(out)
        out.append(
            f"*{passed}/{self.total} "
            f"({100.0 * passed / self.total:.2f}%) passed*"
        )

        return "<br />".join(str(e) for e in out)


class TestComplianceValidDummy(TestComplianceDummy):
    KIND = "valid"


@doc_formatter(url=TOML_TEST_REPO)
class TestComplianceValid(TestCase):
    """Test the compliance with the standard test suites for
        valid toml files here:

        %(url)s

    The tests come up with a JSON counterpart that can be used to valid whether
    loading the toml file yields the same result as the JSON counterpart.
    """

    ORDER = 1
    DUMMY_CLASS = TestComplianceValidDummy

    def _prepare_data(self) -> None:
        ver = self.args.comver
        self.HEADER = f"{self.HEADER} (BurntSushi/toml-test v{ver})"
        datafile = self.args.datadir / "compliance" / f"toml-test-{ver}.zip"
        self.datadir = self.args.datadir / "compliance" / f"toml-test-{ver}"
        self.datadir.parent.mkdir(parents=True, exist_ok=True)
        url = f"{TOML_TEST_REPO}/archive/refs/tags/v{ver}.zip"
        if not self.datadir.exists():
            if not datafile.exists():
                with urllib.request.urlopen(url) as resp, datafile.open(
                    "wb"
                ) as f:
                    f.write(resp.read())
            with zipfile.ZipFile(datafile) as zf:
                zf.extractall(self.datadir.parent)

    def prepare(self) -> None:
        super().prepare()
        self._prepare_data()


class TestComplianceInValidDummy(TestComplianceDummy):

    KIND = "invalid"

    def _runfile(self, tomlfile: Path, subdir: bool = False) -> Any:
        self.total += 1
        filename = (
            tomlfile.name
            if not subdir
            else f"{tomlfile.parent.name}/{tomlfile.name}"
        )
        url = (
            f"{TEST_FILE_PREFIX % {'ver': self.args.comver}}/invalid/{filename}"
        )
        with tomlfile.open(self.__class__.OPEN_FLAG) as f:
            try:
                self.api.load(f)
            except Exception as e:
                return Exception(f"[{filename}]({url}) {e}")
            else:
                return f"Not OK: [{filename}]({url}) incorrectly parsed."

    def result(self, out: Any) -> str:
        replace_newline = lambda s: s.replace("\n", " ")
        passed = [isinstance(e, Exception) for e in out]
        if all(passed):
            return (
                f"OK: {replace_newline(str(out[-1]))}<br /> "
                f"*{len(passed)}/{len(passed)} (100%) passed*"
            )
        out.append(
            f"*{sum(passed)}/{self.total} "
            f"({100.0 * sum(passed) / self.total:.2f}%) passed*"
        )
        return "<br />".join(
            replace_newline(e) for e in out if isinstance(e, str)
        )


@doc_formatter(url=TOML_TEST_REPO)
class TestComplianceInvalid(TestComplianceValid):
    """Test the compliance with the standard test suites for
        invalid toml files here:

        %(url)s

    - `Not OK`: The toml file is parsed without error, but expected to fail.
    - `OK`: All files are failed to parse, as expected. Showing the last parsing
        error.
    """

    ORDER = 2
    DUMMY_CLASS = TestComplianceInValidDummy
