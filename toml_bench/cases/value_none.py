from typing import Any
from benchwork import BenchCase


class BenchCaseDumpNone(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.dumps_none(None)
        except Exception as e:
            return e


class BenchCaseDumpValueNone(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.dumps_none({"key": None})
        except Exception as e:
            return e


class BenchCaseDumpListWithNone(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.dumps_none({"key": [1, 2, 3, None, 5]})
        except Exception as e:
            return e


class BenchCaseLoadNoneLike(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.loads_none('v1 = "null"\nv2 = "None"')
        except Exception as e:
            return e
