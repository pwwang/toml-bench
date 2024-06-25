from benchwork import run_suite
from argx import ArgumentParser

from .suite import BenchSuite


def init_params() -> ArgumentParser:
    """Init the parameters"""
    parser = ArgumentParser(
        prog="toml_bench",
        description="Benchmarking on toml packages in python",
    )
    parser.add_argument(
        "--datadir",
        type="path",
        default="/tmp/toml-bench",
        help="Where to put the test-data",
    )
    parser.add_argument(
        "--report",
        type="path",
        default="/dev/stdout",
        help="If provided, the report will be written to this file",
    )
    parser.add_argument(
        "--title",
        default="Report",
        help="The title of the report",
    )
    parser.add_argument(
        "--comver",
        default="1.5.0",
        help="The version of the toml-test to use in compliance tests",
    )
    parser.add_argument(
        "--cpyver",
        default="3.12.4",
        help="The version (tag) of cpython to grab the tomllib test data",
    )
    parser.add_argument(
        "--nocache",
        action="store_true",
        help="Do not use cached data, re-download them.",
    )
    parser.add_argument(
        "--iter",
        type="int",
        default=5000,
        help="The number of iterations to run in speed tests",
    )
    return parser


def main():
    """Main entrance"""
    args = init_params().parse_args()
    run_suite(
        BenchSuite,
        args=args,
        title=args.title,
        outfile=args.report,
    )


if __name__ == "__main__":
    main()
