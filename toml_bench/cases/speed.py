import timeit
import urllib.request
from typing import Any
from ..case import TestCase
from ..api import APIs
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


@doc_formatter(url=PYTOMLPP_DATA_URL)
class TestWithPytomlppData(TestCase):
    """Test the speed of loading data provided by pytomlpp.


    %(url)s"""

    def __init__(self) -> None:
        super().__init__()
        self.number = None

    def _prepare_datafile(self, filename: str, url: str) -> None:
        self.datafile = self.args.datadir / "speed" / filename
        self.number = self.args.iter
        if not self.datafile.exists():
            self.datafile.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(url) as resp, self.datafile.open(
                "wb"
            ) as f:
                f.write(resp.read())

    def prepare(self, name: str) -> None:
        super().prepare(name)
        self._prepare_datafile("pytomlpp.toml", PYTOMLPP_DATA_URL)

    def run(self, case: "TestCase", name: str) -> Any:
        super().run(case, name)
        api = APIs[name]

        data = case.datafile.read_text()
        return timeit.timeit(lambda: api.loads(data), number=case.number)

    def result(self, out: Any) -> str:
        return f"{out:.2f}s ({self.number} iterations)"


@doc_formatter(url=TOMLI_DATA_URL)
class TestWithTomliData(TestWithPytomlppData):
    """Test the speed of loading data provided by tomli.

    %(url)s"""

    def prepare(self, name: str) -> None:
        super().prepare(name)
        self._prepare_datafile("tomli.toml", TOMLI_DATA_URL)


@doc_formatter(url=RTOML_DATA_URL)
class TestWithRtomlData(TestWithPytomlppData):
    """Test the speed of loading data provided by rtoml.

    %(url)s"""

    def prepare(self, name: str) -> None:
        super().prepare(name)
        self._prepare_datafile("rtoml.toml", RTOML_DATA_URL)
