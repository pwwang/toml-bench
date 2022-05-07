from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from .utils import get_object, load_subpkgs, logger
from .api import APIs, API

if TYPE_CHECKING:
    from pyparam import Namespace


class TestCaseDummy(ABC):
    def __init__(self) -> None:
        self.args = None
        self.pkgname = None

    @property
    def api(self) -> API:
        return APIs[self.pkgname]

    @abstractmethod
    def run(self, case: "TestCase") -> Any:
        logger.info(
            "[%s][%s] Running test case ...",
            case.__class__.__name__,
            self.pkgname,
        )

    def result(self, out: Any) -> str:
        return str(out)


class TestCase(ABC):

    ORDER = 0
    HEADER = "Result"
    DUMMY_CLASS = TestCaseDummy

    def __init__(self) -> None:
        self.results = {}
        self.dummies = []
        self.args = None

    def set_args(self, args: "Namespace") -> None:
        self.args = args
        for dummy in self.dummies:
            dummy.args = args

    def load_dummies(self):
        for name, pkg in load_subpkgs("packages").items():
            dummy_class = get_object(
                pkg,
                lambda obj: (
                    isinstance(obj, type)
                    and issubclass(obj, self.__class__.DUMMY_CLASS)
                    and obj is not self.__class__.DUMMY_CLASS
                ),
            )
            if dummy_class is None:
                dummy_class = self.__class__.DUMMY_CLASS
            dummy = dummy_class()
            dummy.pkgname = name
            self.dummies.append(dummy)

    def prepare(self) -> None:
        logger.info("[%s] Preparing test case ...", self.__class__.__name__)

    def run_all(self) -> None:
        for dummy in self.dummies:
            result = dummy.run(self)
            self.results[dummy.pkgname] = dummy.result(result)

    def result_all(self) -> str:
        ret = []
        for dummy in self.dummies:
            out = self.results[dummy.pkgname]
            ret.append(f"|[{dummy.pkgname}]({dummy.api.repo})|{out}|")
        return "\n".join(ret)
