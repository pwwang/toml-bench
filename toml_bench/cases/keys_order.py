from typing import Any
from benchwork import BenchCase


class BenchCaseDumpKeysOrder(BenchCase):

    def run(self) -> Any:
        v1 = {"a": 1, "b": 2, "c": 3}
        v2 = {"b": 1, "c": 2, "a": 3}
        v3 = {"c": 1, "a": 2, "b": 3}

        e1 = "a = 1\nb = 2\nc = 3\n"
        e2 = "b = 1\nc = 2\na = 3\n"
        e3 = "c = 1\na = 2\nb = 3\n"

        try:
            if (
                self.api.dumps(v1) == e1
                and self.api.dumps(v2) == e2
                and self.api.dumps(v3) == e3
            ):
                return "Kept"
            return "Lost"
        except Exception as ex:
            return str(ex)


class BenchCaseLoadKeysOrder(BenchCase):

    def run(self) -> Any:
        v1 = "a = 1\nb = 2\nc = 3\n"
        v2 = "b = 1\nc = 2\na = 3\n"
        v3 = "c = 1\na = 2\nb = 3\n"

        e1 = ["a", "b", "c"]
        e2 = ["b", "c", "a"]
        e3 = ["c", "a", "b"]

        if (
            list(self.api.loads(v1)) == e1
            and list(self.api.loads(v2)) == e2
            and list(self.api.loads(v3)) == e3
        ):
            return "Kept"
        return "Lost"
