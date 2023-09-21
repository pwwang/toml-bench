from __future__ import annotations

from typing import TYPE_CHECKING, Any, Type
from benchwork import BenchCaseSpeed

if TYPE_CHECKING:
    from argparse import Namespace
    from benchwork import BenchAPI


class BenchCaseSpeed(BenchCaseSpeed):

    timeit_number = "iter"

    def __init__(self, args: Namespace, api_class: Type[BenchAPI]) -> None:
        super().__init__(args, api_class)
        self.data = None
        self.loaded = None

    def run_core(self):
        ...

    def run_loading(self):
        self.loaded = self.api.loads(self.data)
        return self.loaded

    def run_dumping(self):
        return self.api.dumps(self.loaded)

    def run(self) -> Any:
        if self.api._name == "toml":
            return [
                "Excluded (heterogeneous arrays not supported)",
                "Excluded (heterogeneous arrays not supported)",
            ]

        self.run_core = self.run_loading
        out = super().run()
        loading = f"{out:.2f}s ({self.args.iter} iterations)"

        self.run_core = self.run_dumping
        try:
            out = super().run()
        except Exception as e:
            dumping = str(e)
        else:
            dumping = f"{out:.2f}s ({self.args.iter} iterations)"

        return [loading, dumping]
