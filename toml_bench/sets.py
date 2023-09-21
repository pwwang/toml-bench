import zipfile
import urllib.request

from benchwork import BenchSetVersion, BenchSetTable, BenchSetMultiColTable

from .api import APIBase
from .cases.value_none import (
    BenchCaseDumpListWithNone,
    BenchCaseDumpValueNone,
    BenchCaseDumpNone,
    BenchCaseLoadNoneLike,
)
from .cases.hetero_array import (
    BenchCaseDumpsHeteroArray,
    BenchCaseLoadsHeteroArray,
    BenchCaseDumpsNestedArray,
    BenchCaseLoadsNestedArray,
)
from .cases.keys_order import (
    BenchCaseDumpKeysOrder,
    BenchCaseLoadKeysOrder,
)
from .cases.unicode import (
    BenchCaseDumpsUnicode,
    BenchCaseLoadsUnicode,
)
from .cases.compliance import (
    BenchCaseComplianceValid,
    BenchCaseComplianceInvalid,
    BenchCaseTomllibComplianceValid,
    BenchCaseTomllibComplianceInvalid,
)
from .cases.speed import BenchCaseSpeed

TOML_TEST_REPO = "https://github.com/BurntSushi/toml-test/"

TOMLLIB_DATA_REPO = "https://github.com/python/cpython"

PYTOMLPP_DATA_URL = (
    "https://github.com/bobfang1992/pytomlpp/raw/master/benchmark/data.toml"
)

TOMLI_DATA_URL = (
    "https://github.com/hukkin/tomli/raw/master/benchmark/data.toml"
)

RTOML_DATA_URL = (
    "https://github.com/samuelcolvin/rtoml/raw/main/tests/data.toml"
)


class BenchSetVersion(BenchSetVersion):
    """The verions of the packages tested in this report."""

    header = "Version"
    title = "Version"
    api_base = APIBase


class BenchSetDumpNone(BenchSetTable):
    """How the package dumps `None` value in python

    Literally `<package>.dumps(None)`
    """

    title = "Dumping `None` value"
    header = "Dumped value or error"
    api_base = APIBase
    case = BenchCaseDumpNone


class BenchSetDumpValueNone(BenchSetTable):
    """How the package dumps key-value pair with value `None`

    Literally `<package>.dumps({"key": None})`
    """

    title = "Dumping key-`None` pair"
    header = "Dumped value or error"
    api_base = APIBase
    case = BenchCaseDumpValueNone


class BenchSetDumpListWithNone(BenchSetTable):
    """How the package dumps a list with `None` value in it.

    Literally `<package>.dumps({"key": [1, 2, 3, None, 5]})`
    """

    title = "Dumping list with `None` value"
    header = "Dumped value or error"
    api_base = APIBase
    case = BenchCaseDumpListWithNone


class BenchSetLoadNoneLike(BenchSetTable):
    """How the package loads `None`-like value in string

    Literally `<package>.loads('v1 = "null" v2 = "None"')`
    """

    title = "Loading `None`-like values"
    header = "Loaded as"
    api_base = APIBase
    case = BenchCaseLoadNoneLike


class BenchSetDumpsHeteroArray(BenchSetTable):
    """How the package dumps a python dictionary with a heterogenous array.

    Literally `<package>.dumps({"v": [1, 1.2, True, "string"]})`
    """

    title = "Dumping a heterogenous array"
    header = "Dumped value or error"
    api_base = APIBase
    case = BenchCaseDumpsHeteroArray


class BenchSetLoadsHeteroArray(BenchSetTable):
    """How the package loads a toml string with a heterogenous array.

    Literally `<package>.loads('v = [1, 1.2, True, "string"]')`
    """

    title = "Loading a heterogenous array"
    header = "Loaded as"
    api_base = APIBase
    case = BenchCaseLoadsHeteroArray


class BenchSetDumpsNestedArray(BenchSetTable):
    """How the package dumps a python dictionary with a nested array.

    Literally `<package>.dumps({"v": [[1], [1, 2]]})`
    """

    title = "Dumping a nested array"
    header = "Dumped value or error"
    api_base = APIBase
    case = BenchCaseDumpsNestedArray


class BenchSetLoadsNestedArray(BenchSetTable):
    """How the package loads a toml string with a nested array.

    Literally `<package>.loads('v = [[1], [1, 2]]')`
    """
    title = "Loading a nested array"
    header = "Loaded as"
    api_base = APIBase
    case = BenchCaseLoadsNestedArray


class BenchSetDumpKeysOrder(BenchSetTable):
    """Whether the package preserves the order of the keys while dumps
    a python dictionary.

    Thus, whether `<package>.dumps({"c": 1, "a": 2, "b": 3})` yields a string
    like `c = 1\\na = 2\\nb = 3\\n`.
    """

    title = "Dumping keeps order of keys?"
    header = "Order kept?"
    api_base = APIBase
    case = BenchCaseDumpKeysOrder


class BenchSetLoadKeysOrder(BenchSetTable):
    """Whether the package preserves the order of the keys
    while loads a TOML string.

    Thus, whether `<package>.loads('c = 1\\na = 2\\nb = 3\\n')` yields
    a dictionary with keys in the order of `['c', 'a', 'b']`.
    """

    title = "Loading keeps order of keys?"
    header = "Order kept?"
    api_base = APIBase
    case = BenchCaseLoadKeysOrder


class BenchSetDumpsUnicode(BenchSetTable):
    """How the package dumps Unicode in python

    Literally, `<package>.dumps({"你好": "世界"})`
    """

    title = "Dumping unicode"
    header = "Dumped value"
    api_base = APIBase
    case = BenchCaseDumpsUnicode


class BenchSetLoadsUnicode(BenchSetTable):
    """How the package loads a file with unicode.

    The file was created by:

    ```python
    # Create a file with unicode content
    with open(self.datafile, "w", encoding="utf-8") as f:
        f.write('"你好" = "世界"\\n')

    # Use `<package>.load()` to load the file
    with open(self.datafile, "r", encoding="utf-8") as f:
        loaded = <package>.load(f)
    ```
    """

    title = "Loaded unicode"
    header = "Loaded as"
    api_base = APIBase
    case = BenchCaseLoadsUnicode

    def prepare_cases(self):

        datafile = self.args.datadir / "unicode" / "unicode.toml"
        datafile.parent.mkdir(parents=True, exist_ok=True)
        with open(datafile, "w", encoding="utf-8") as f:
            f.write('"你好" = "世界"\n')

        for case in self.cases:
            case.datafile = datafile
            case.prepare()


class BenchSetComplianceValid(BenchSetTable):
    """Test the compliance with the standard test suites for valid toml files
    here:

    > https://github.com/BurntSushi/toml-test/

    The tests come up with a JSON counterpart that can be used to valid whether
    loading the toml file yields the same result as the JSON counterpart.
    """
    title = "Compliance with valid tests in toml-test"
    api_base = APIBase
    case = BenchCaseComplianceValid

    @property
    def header(self) -> str:
        return f"Result (toml-test v{self.args.comver})"

    def prepare_cases(self):

        ver = self.args.comver
        datafile = self.args.datadir / "compliance" / f"toml-test-{ver}.zip"
        datadir = self.args.datadir / "compliance" / f"toml-test-{ver}"
        datadir.parent.mkdir(parents=True, exist_ok=True)
        url = f"{TOML_TEST_REPO}/archive/refs/tags/v{ver}.zip"
        if not datadir.exists() or self.args.nocache:
            if not datafile.exists():
                with urllib.request.urlopen(url) as resp, datafile.open(
                    "wb"
                ) as f:
                    f.write(resp.read())
            with zipfile.ZipFile(datafile) as zf:
                zf.extractall(datadir.parent)

        for case in self.cases:
            case.datadir = datadir
            case.prepare()


class BenchSetComplianceInvalid(BenchSetTable):
    """Test the compliance with the standard test suites for invalid toml files
    here:

    > https://github.com/BurntSushi/toml-test/

    - `Not OK`: The toml file is parsed without error, but expected to fail.
    - `OK`: All files are failed to parse, as expected. Showing the last
    parsing error.
    """
    title = "Compliance with invalid tests in toml-test"
    api_base = APIBase
    case = BenchCaseComplianceInvalid

    @property
    def header(self) -> str:
        return f"Result (toml-test v{self.args.comver})"

    def prepare_cases(self):

        ver = self.args.comver
        # data prepared in BenchSetComplianceValid
        for case in self.cases:
            case.datadir = self.args.datadir / "compliance" / f"toml-test-{ver}"
            case.prepare()


class BenchSetTomllibComplianceValid(BenchSetTable):
    """Test the compliance with python tomllib test data (since python 3.11)
    for valid toml files here:

    > https://github.com/python/cpython/tree/3.11/Lib/test/test_tomllib/data/valid

    The tests come up with a JSON counterpart that can be used to valid whether
    loading the toml file yields the same result as the JSON counterpart.
    """  # noqa: E501
    title = "Compliance with valid tests in python tomllib test data"
    api_base = APIBase
    case = BenchCaseTomllibComplianceValid

    @property
    def header(self) -> str:
        return f"Result (cpython tag {self.args.cpyver})"

    def prepare_cases(self):

        datafile = self.args.datadir.joinpath(
            "tomllib-compliance",
            f"tomllib-data-{self.args.cpyver}.zip",
        )
        datadir = self.args.datadir.joinpath(
            "tomllib-compliance",
            f"tomllib-data-{self.args.cpyver}",
        )
        datadir.parent.mkdir(parents=True, exist_ok=True)
        url = f"{TOMLLIB_DATA_REPO}/archive/refs/tags/v{self.args.cpyver}.zip"
        if not datadir.exists() or self.args.nocache:
            if not datafile.exists():
                with urllib.request.urlopen(url) as resp, datafile.open(
                    "wb"
                ) as f:
                    f.write(resp.read())
            with zipfile.ZipFile(datafile) as zf:
                namelist = zf.namelist()
                first = namelist[0]
                member_data = f"{first}Lib/test/test_tomllib/data/"
                members = [m for m in namelist if m.startswith(member_data)]
                zf.extractall(datadir.parent, members=members)
            datadir.parent.joinpath(first).rename(datadir)

        for case in self.cases:
            case.datadir = datadir
            case.prepare()


class BenchSetTomllibComplianceInvalid(BenchSetTomllibComplianceValid):
    """Test the compliance with python tomllib test data (since python 3.11)
    for invalid toml files here:

    > https://github.com/python/cpython/tree/main/Lib/test/test_tomllib/data/invalid

    - `Not OK`: The toml file is parsed without error, but expected to fail.
    - `OK`: All files are failed to parse, as expected. Showing the last
    parsing error.
    """  # noqa: E501
    title = "Compliance with invalid tests in python tomllib test data"
    case = BenchCaseTomllibComplianceInvalid

    def prepare_cases(self):

        # data prepared in BenchSetTomllibComplianceValid
        for case in self.cases:
            case.datadir = self.args.datadir.joinpath(
                "tomllib-compliance",
                f"tomllib-data-{self.args.cpyver}",
            )
            case.prepare()


class BenchSetSpeed(BenchSetMultiColTable):

    header = ["Loading speed", "Dumping speed"]
    api_base = APIBase
    case = BenchCaseSpeed

    @property
    def package_name(self) -> str:
        ...

    @property
    def url(self) -> str:
        ...

    @property
    def title(self) -> str:
        return f"Running speed with data provided by `{self.package_name}`"

    def prepare_cases(self):

        datafile = self.args.datadir / "speed" / f"{self.package_name}.toml"

        if not datafile.exists() or self.args.nocache:
            datafile.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(self.url) as resp, datafile.open(
                "wb"
            ) as f:
                f.write(resp.read())

        data = datafile.read_text()

        for case in self.cases:
            case.data = data
            case.prepare()


class BenchSetSpeedWithPytomlppData(BenchSetSpeed):
    """Test the speed of loading and dumping the loaded
    using data provided by `pytomlpp`

    > https://github.com/bobfang1992/pytomlpp/raw/master/benchmark/data.toml
    """
    package_name = "pytomlpp"
    url = PYTOMLPP_DATA_URL


class BenchSetSpeedWithRtomlData(BenchSetSpeed):
    """Test the speed of loading and dumping the loaded using data
    provided by `rtoml`

    > https://github.com/samuelcolvin/rtoml/raw/main/tests/data.toml
    """
    package_name = "rtoml"
    url = RTOML_DATA_URL


class BenchSetSpeedWithTomliData(BenchSetSpeed):
    """Test the speed of loading and dumping the loaded using data
    provided by `tomli`

    > https://github.com/hukkin/tomli/raw/master/benchmark/data.toml
    """
    package_name = "tomli"
    url = TOMLI_DATA_URL
