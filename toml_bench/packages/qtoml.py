import qtoml
from ..api import API
from ..cases.compliance import TestComplianceValidDummy


class QTOMLAPI(API):
    package = qtoml
    repo = "https://github.com/alethiophile/qtoml"


class QTOMLTestComplianceValidDummy(TestComplianceValidDummy):
    OPEN_FLAG = "r"
