from typing import Any
from benchwork import BenchCase


class BenchCaseDumpNone(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.dumps(None)
        except Exception as e:
            return e


class BenchCaseDumpValueNone(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.dumps({"key": None})
        except Exception as e:
            return e


class BenchCaseDumpListWithNone(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.dumps({"key": [1, 2, 3, None, 5]})
        except Exception as e:
            return e


class BenchCaseLoadNoneLike(BenchCase):

    def run(self) -> Any:
        try:
            return self.api.loads('v1 = "null"\nv2 = "None"')
        except Exception as e:
            return e
