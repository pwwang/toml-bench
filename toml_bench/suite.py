from benchwork import BenchSuite

from .sets import (
    BenchSetVersion,
    BenchSetDumpNone,
    BenchSetDumpValueNone,
    BenchSetDumpListWithNone,
    BenchSetLoadNoneLike,
    BenchSetDumpKeysOrder,
    BenchSetLoadKeysOrder,
    BenchSetDumpsUnicode,
    BenchSetLoadsUnicode,
    BenchSetComplianceValid,
    BenchSetComplianceInvalid,
    BenchSetTomllibComplianceValid,
    BenchSetTomllibComplianceInvalid,
    BenchSetSpeedWithPytomlppData,
    BenchSetSpeedWithRtomlData,
    BenchSetSpeedWithTomliData,
)


class BenchSuite(BenchSuite):
    set_classes = [
        BenchSetVersion,
        BenchSetDumpNone,
        BenchSetDumpValueNone,
        BenchSetDumpListWithNone,
        BenchSetLoadNoneLike,
        BenchSetDumpKeysOrder,
        BenchSetLoadKeysOrder,
        BenchSetDumpsUnicode,
        BenchSetLoadsUnicode,
        BenchSetComplianceValid,
        BenchSetComplianceInvalid,
        BenchSetTomllibComplianceValid,
        BenchSetTomllibComplianceInvalid,
        BenchSetSpeedWithPytomlppData,
        BenchSetSpeedWithRtomlData,
        BenchSetSpeedWithTomliData,
    ]
