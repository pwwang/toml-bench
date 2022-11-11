from typing import Any
from benchwork import BenchCase


class BenchCaseDumpsUnicode(BenchCase):
    def run(self) -> Any:
        v1 = {"你好": "世界"}
        try:
            return self.api.dumps(v1)
        except Exception as e:
            return e


class BenchCaseLoadsUnicode(BenchCase):

    def run(self) -> Any:
        try:
            with open(self.datafile, "r", encoding="utf-8") as f1:
                return self.api.load(f1)
        except Exception as e1:
            try:
                with open(self.datafile, "rb") as f2:
                    loaded = self.api.load(f2)
                    return f"{e1}\nWhen loaded with `rb`:\n{loaded}"
            except Exception:
                return e1
