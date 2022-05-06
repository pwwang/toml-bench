from abc import ABC, abstractmethod
from typing import Any

from .utils import get_instance, load_subpkgs, logger
from .api import APIs


class TestCase(ABC):

    ORDER = 0
    header = "Result"

    def __init__(self) -> None:
        self.out_all = {}
        self.pkgs = {}
        self.args = None

    def load_pkgs(self):
        for name, pkg in load_subpkgs("packages").items():
            pkg = get_instance(
                pkg,
                lambda obj: (
                    isinstance(obj, type)
                    and issubclass(obj, self.__class__)
                    and obj is not self.__class__
                ),
            )
            if pkg is None:
                pkg = self.__class__
            self.pkgs[name] = pkg()

    def prepare(self, name: str) -> None:
        logger.info("[%s] Preparing test case ...", name)

    def run_all(self) -> None:
        for name, pkg in self.pkgs.items():
            self.out_all[name] = self.result(pkg.run(self, name))

    @abstractmethod
    def run(self, case: "TestCase", name: str) -> Any:
        logger.info(
            "[%s][%s] Running test case ...",
            case.__class__.__name__,
            name,
        )

    def result(self, out: Any) -> str:
        return str(out)

    def result_all(self) -> str:
        ret = []
        for name, out in self.out_all.items():
            ret.append(f"|[{name}]({APIs[name].repo})|{out}|")
        return "\n".join(ret)
