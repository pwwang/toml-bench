import toml

from ..api import API
from ..cases.compliance import (
    TestComplianceValidDummy,
    TestComplianceInValidDummy,
)


class TOMLAPI(API):
    package = toml
    repo = "https://github.com/uiri/toml"


class TOMLTestComplianceValidDummy(TestComplianceValidDummy):
    OPEN_FLAG = "r"


class TOMLTestComplianceInValidDummy(TestComplianceInValidDummy):
    OPEN_FLAG = "r"
