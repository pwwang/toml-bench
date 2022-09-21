from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Type
from benchwork import BenchCase

from ..utils import load_json_data

if TYPE_CHECKING:
    from argparse import Namespace
    from pathlib import Path
    from benchwork import BenchAPI

TEST_FILE_PREFIX = (
    "https://github.com/BurntSushi/toml-test/blob/v%(ver)s/tests/"
)


class BenchCaseCompliance(BenchCase):

    KIND = None

    def __init__(self, args: Namespace, api_class: Type[BenchAPI]) -> None:
        super().__init__(args, api_class)
        self.total = 0
        self.datadir = None

    def _runfile(
        self,
        tomlfile: Path,
        subdir: bool = False,
    ) -> Any:
        ...

    def _result(
        self,
        out: List[Any],
    ) -> Any:
        ...

    def run(self) -> Any:
        errors = []
        kind = self.__class__.KIND
        for tomlfile in self.datadir.joinpath("tests", kind).glob("*.toml"):
            out = self._runfile(tomlfile)
            if out is not None:
                errors.append(out)

        for tomlfile in self.datadir.joinpath("tests", kind).glob("*/*.toml"):
            out = self._runfile(tomlfile, subdir=True)
            if out is not None:
                errors.append(out)

        return self._result(errors)


class BenchCaseComplianceValid(BenchCaseCompliance):

    KIND = "valid"

    def _runfile(self, tomlfile: Path, subdir: bool = False) -> Any:

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
        with tomlfile.open(self.api.OPEN_FLAG) as f:
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

    def _result(self, out: List[Any]) -> Any:

        if not out:
            return f"OK, *{self.total}/{self.total} (100%) passed*"

        passed = self.total - len(out)
        out.append(
            f"*{passed}/{self.total} "
            f"({100.0 * passed / self.total:.2f}%) passed*"
        )

        return "<br />".join(str(e).replace("\n", " ") for e in out)


class BenchCaseComplianceInvalid(BenchCaseCompliance):

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
        with tomlfile.open(self.api.OPEN_FLAG) as f:
            try:
                self.api.load(f)
            except Exception as e:
                return Exception(f"[{filename}]({url}) {e}")
            else:
                return f"Not OK: [{filename}]({url}) incorrectly parsed."

    def _result(self, out: List[Any]) -> Any:

        replace_newline = lambda s: s.replace("\n", " ")
        passed = [isinstance(e, Exception) for e in out]
        failed = [e for e in out if not isinstance(e, Exception)]
        if all(passed):
            return (
                f"OK: {replace_newline(str(out[-1]))}<br /> "
                f"*{len(passed)}/{len(passed)} (100%) passed*"
            )

        if len(failed) > 10:
            failed = failed[:10] + [
                f"Not OK: *{len(failed) - 10} more items incorrectly parsed.*"
            ]

        failed.append(
            f"*{sum(passed)}/{self.total} "
            f"({100.0 * sum(passed) / self.total:.2f}%) passed*"
        )
        return "<br />".join(replace_newline(str(e)) for e in failed)
