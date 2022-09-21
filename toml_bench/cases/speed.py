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

    def run_core(self):
        return self.api.loads(self.data)

    def run(self) -> Any:
        out = super().run()
        return f"{out:.2f}s ({self.args.iter} iterations)"
