from typing import Any
from ..case import TestCase, TestCaseDummy
from ..api import APIs


class VersionDummy(TestCaseDummy):
    def run(self, case: "TestCase") -> Any:
        super().run(case)
        return self.api.version()


class Version(TestCase):
    """The verions of the packages tested in this report."""

    ORDER = -99
    HEADER = "Version"
    DUMMY_CLASS = VersionDummy
