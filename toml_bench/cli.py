from pyparam import Params

from .suite import TestSuite
from .utils import logger


def _init_params() -> Params:
    params = Params(help_on_void=False)
    params.add_param(
        "datadir",
        type="path",
        default="/tmp/toml-bench",
        desc="Where to put the test-data",
    )
    params.add_param(
        "report",
        type="file",
        desc=(
            "If provided, the report will be written to "
            "this file under section `## Report` in markdown format. "
            "If the section exists, it will be overwritten."
        ),
    )
    params.add_param(
        "comver",
        default="1.1.0",
        desc="The version of the toml-test to use in compliance tests",
    )
    params.add_param(
        "iter",
        default=5000,
        desc="The number of iterations to run in speed tests",
    )
    return params


def main():
    parsed = _init_params().parse()
    logger.info("Data directory: %s", parsed.datadir)
    suite = TestSuite()
    suite.set_args(parsed)
    suite.prepare()
    suite.run()
    suite.result()
