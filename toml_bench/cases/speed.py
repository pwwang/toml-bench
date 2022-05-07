import timeit
import urllib.request
from typing import Any
from ..case import TestCase, TestCaseDummy
from ..utils import doc_formatter

PYTOMLPP_DATA_URL = (
    "https://github.com/bobfang1992/pytomlpp/raw/master/benchmark/data.toml"
)

TOMLI_DATA_URL = (
    "https://github.com/hukkin/tomli/raw/master/benchmark/data.toml"
)

RTOML_DATA_URL = (
    "https://github.com/samuelcolvin/rtoml/raw/main/benchmarks/data.toml"
)


class TestSpeedDummy(TestCaseDummy):
    def run(self, case: TestCase) -> Any:
        super().run(case)

        data = case.datafile.read_text()
        return timeit.timeit(
            lambda: self.api.loads(data),
            number=self.args.iter,
        )

    def result(self, out: Any) -> str:
        return f"{out:.2f}s ({self.args.iter} iterations)"


class TestSpeedWithPytomlppDataDummy(TestSpeedDummy):
    ...


@doc_formatter(url=PYTOMLPP_DATA_URL)
class TestSpeedWithPytomlppData(TestCase):
    """Test the speed of loading data provided by pytomlpp.


    %(url)s"""

    DUMMY_CLASS = TestSpeedWithPytomlppDataDummy
    ORDER = 9

    def _prepare_datafile(self, filename: str, url: str) -> None:
        self.datafile = self.args.datadir / "speed" / filename
        self.number = self.args.iter
        if not self.datafile.exists():
            self.datafile.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(url) as resp, self.datafile.open(
                "wb"
            ) as f:
                f.write(resp.read())

    def prepare(self) -> None:
        super().prepare()
        self._prepare_datafile("pytomlpp.toml", PYTOMLPP_DATA_URL)


class TestSpeedWithTomliDataDummy(TestSpeedDummy):
    ...


@doc_formatter(url=TOMLI_DATA_URL)
class TestSpeedWithTomliData(TestSpeedWithPytomlppData):
    """Test the speed of loading data provided by tomli.

    %(url)s"""

    DUMMY_CLASS = TestSpeedWithTomliDataDummy

    def prepare(self) -> None:
        super().prepare()
        self._prepare_datafile("tomli.toml", TOMLI_DATA_URL)


class TestSpeedWithRtomlDataDummy(TestSpeedDummy):
    ...


@doc_formatter(url=RTOML_DATA_URL)
class TestSpeedWithRtomlData(TestSpeedWithPytomlppData):
    """Test the speed of loading data provided by rtoml.

    %(url)s"""

    DUMMY_CLASS = TestSpeedWithRtomlDataDummy

    def prepare(self) -> None:
        super().prepare()
        self._prepare_datafile("rtoml.toml", RTOML_DATA_URL)
