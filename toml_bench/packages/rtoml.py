import rtoml
from ..api import API
from ..cases.compliance import (
    TestComplianceValidDummy,
    TestComplianceInValidDummy,
)


class TOMLKitAPI(API):
    package = rtoml
    repo = "https://github.com/samuelcolvin/rtoml"


class RTOMLTestComplianceValidDummy(TestComplianceValidDummy):
    OPEN_FLAG = "r"


class RTOMLTestComplianceInValidDummy(TestComplianceInValidDummy):
    OPEN_FLAG = "r"
