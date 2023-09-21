from benchwork import run_suite
from pyparam import Params

from .suite import BenchSuite


def init_params() -> Params:
    params = Params(
        prog="toml_bench",
        help_on_void=False,
        desc="Benchmarking on toml packages in python",
    )
    params.add_param(
        "datadir",
        type="path",
        default="/tmp/toml-bench",
        desc="Where to put the test-data",
    )
    params.add_param(
        "report",
        default="<stdout>",
        desc="If provided, the report will be written to this file",
    )
    params.add_param(
        "title",
        default="Report",
        desc="The title of the report",
    )
    params.add_param(
        "comver",
        default="1.3.0",
        desc="The version of the toml-test to use in compliance tests",
    )
    params.add_param(
        "cpyver",
        default="3.11.0",
        desc="The version (tag) of cpython to grab the tomllib test data",
    )
    params.add_param(
        "nocache",
        default=False,
        desc="Do not use cached data, re-download them.",
    )
    params.add_param(
        "iter",
        default=5000,
        desc="The number of iterations to run in speed tests",
    )
    return params


def main():
    """Main entrance"""
    args = init_params().parse()
    run_suite(
        BenchSuite,
        args=args,
        title=args.title,
        outfile=args.report,
    )


if __name__ == "__main__":
    main()
