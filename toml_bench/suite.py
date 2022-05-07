from typing import TYPE_CHECKING

from .utils import load_subpkgs, logger, get_object
from .case import TestCase

if TYPE_CHECKING:
    from pyparam import Namespace


class TestSuite:
    def __init__(self) -> None:
        """Collect cases"""
        self.cases = []
        self.args = None
        for name, case in load_subpkgs("cases").items():
            logger.info("[%s] Collecting test cases ...", name)
            case_classes = get_object(
                case,
                lambda obj: (
                    isinstance(obj, type)
                    and issubclass(obj, TestCase)
                    and obj is not TestCase
                ),
                multi=True,
            )
            for case_class in case_classes:
                case = case_class()
                case.load_dummies()
                self.cases.append(case)

        # put it in the right order
        self.cases.sort(key=lambda x: x.ORDER)

    def set_args(self, args: "Namespace") -> None:
        """Set args"""
        self.args = args
        for case in self.cases:
            case.set_args(args)

        kw = self.args.keyword
        if kw:
            self.cases = [
                case
                for case in self.cases
                if kw.lower() in case.__class__.__name__.lower()
            ]

    def _prepare_datadir(self) -> None:
        """Prepare packages"""
        logger.info(
            "[%s] Preparing data directory ...",
            self.__class__.__name__,
        )
        self.args.datadir.mkdir(parents=True, exist_ok=True)

    def prepare(self) -> None:
        """Prepare all cases"""
        self._prepare_datadir()
        for case in self.cases:
            case.prepare()

    def run(self) -> None:
        """Run all cases"""
        for case in self.cases:
            case.run_all()

    def result(self) -> None:
        """Result of all cases"""
        report = []
        for case in self.cases:
            report.append("")
            report.append(f"### {case.__class__.__name__}")
            report.append("")
            report.append(case.__doc__ or "")
            report.append("")
            report.append(f"|Package|{case.HEADER}|")
            report.append("|:------|:------|")
            report.append(case.result_all())
        report.append("")
        report.append("")

        if self.args.report is None:
            print("\n".join(report))
            return

        logger.info(
            "[%s] Writing report to [%s] ...",
            self.__class__.__name__,
            self.args.report,
        )
        out = []
        report_hit = False
        if self.args.report.exists():
            with open(self.args.report, "r") as f:
                for line in f:
                    line = line.rstrip()
                    if line == "## Report":
                        out.append(line)
                        out.extend(report)
                        report_hit = True
                    elif (
                        # Next session or links
                        (line.startswith("## ") or line.startswith("["))
                        and report_hit
                    ):
                        out.append(line)
                        report_hit = False
                    elif not report_hit:
                        out.append(line)
        else:
            out.append("## Report")
            out.extend(report)

        out.append("")

        with open(self.args.report, "w") as f:
            f.write("\n".join(out))
