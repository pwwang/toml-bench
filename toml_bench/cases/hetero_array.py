from typing import Any
from benchwork import BenchCase


class BenchCaseDumpsHeteroArray(BenchCase):
    def run(self) -> Any:
        v1 = {
            "v": [1, 1.2, True, "string"]
        }
        try:
            return (
                self.api.dumps(v1)
                .replace('[', r'\[')
                .replace(']', r'\]')
                .replace(' ', '&nbsp;')
            )
        except Exception as e:
            return e


class BenchCaseLoadsHeteroArray(BenchCase):

    def run(self) -> Any:
        v1 = """
            v = [1, 1.2, true, "string"]
        """
        try:
            return f"`{self.api.loads(v1)}`"
        except Exception as e1:
            return e1


class BenchCaseDumpsNestedArray(BenchCase):
    def run(self) -> Any:
        v1 = {
            "v": [[1], [1, 2]]
        }
        try:
            return (
                self.api.dumps(v1)
                .replace('[', r'\[')
                .replace(']', r'\]')
                .replace(' ', '&nbsp;')
            )
        except Exception as e:
            return e


class BenchCaseLoadsNestedArray(BenchCase):

    def run(self) -> Any:
        v1 = """
            v = [[1], [1, 2]]
        """
        try:
            return f"`{self.api.loads(v1)}`"
        except Exception as e1:
            return e1
