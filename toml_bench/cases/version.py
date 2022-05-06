from typing import Any
from ..case import TestCase
from ..api import APIs


class Version(TestCase):
    """The verions of the packages tested in this report."""

    ORDER = -99
    header = "Version"

    def run(self, casename: str, name: str) -> Any:
        super().run(casename, name)
        api = APIs[name]
        return api.version()

    def result(self, out: Any) -> str:
        return str(out)
