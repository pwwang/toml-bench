## Report

### Version

The verions of the packages tested in this report.

|Package|Version|
|:------|:------|
|[toml](https://github.com/uiri/toml)|0.10.2|
|[rtoml](https://github.com/samuelcolvin/rtoml)|0.7.1|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|1.0.11|
|[tomli](https://github.com/hukkin/tomli)|2.0.1; **tomli_w**: 1.0.0|
|[qtoml](https://github.com/alethiophile/qtoml)|0.3.1|
|[tomlkit](https://github.com/sdispater/tomlkit)|0.10.2|

### TestDumpListWithNone

How the package dumps a list with `None` value in it.
    Literally `<package>.dumps({"key": [1, 2, 3, None, 5]})`


|Package|Dumped value or error|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Dumps to `'key = [ 1, 2, 3, "None", 5,]\n'`|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Dumps to `'key = [1, 2, 3, "null", 5]\n'`|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Raises not a valid type for conversion None|
|[tomli](https://github.com/hukkin/tomli)|Raises Object of type <class 'NoneType'> is not TOML serializable|
|[qtoml](https://github.com/alethiophile/qtoml)|Raises bad type '<class 'NoneType'>' for dump_value|
|[tomlkit](https://github.com/sdispater/tomlkit)|Raises Invalid type <class 'NoneType'>|

### TestDumpNone

How the package dumps `None` value in python,
    literally `<package>.dumps(None)`


|Package|Dumped value or error|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Raises 'NoneType' object is not iterable|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Dumps to `'"null"'`|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Raises dumps(): incompatible function arguments. The following argument types are supported:     1. (arg0: dict) -> str  Invoked with: None|
|[tomli](https://github.com/hukkin/tomli)|Raises 'NoneType' object has no attribute 'items'|
|[qtoml](https://github.com/alethiophile/qtoml)|Raises 'NoneType' object has no attribute 'items'|
|[tomlkit](https://github.com/sdispater/tomlkit)|Raises Expecting Mapping or TOML Container, <class 'NoneType'> given|

### TestDumpValueNone

How the package dumps key-value pair with value `None`,
    literally `<package>.dumps({"key": None})`


|Package|Dumped value or error|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Ignores the key (dumps to an empty string)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Dumps to `'key = "null"\n'`|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Raises cannot convert value None to proper toml type |
|[tomli](https://github.com/hukkin/tomli)|Raises Object of type <class 'NoneType'> is not TOML serializable|
|[qtoml](https://github.com/alethiophile/qtoml)|Raises TOML cannot encode None|
|[tomlkit](https://github.com/sdispater/tomlkit)|Raises Invalid type <class 'NoneType'>|

### TestLoadNoneLike

How the package loads `None`-like value in string,
    literally `<package>.loads('v1 = "null"
v2 = "None"')`


|Package|Loaded as|
|:------|:------|
|[toml](https://github.com/uiri/toml)|`{'v1': 'null', 'v2': 'None'}`|
|[rtoml](https://github.com/samuelcolvin/rtoml)|`{'v1': 'null', 'v2': 'None'}`|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|`{'v1': 'null', 'v2': 'None'}`|
|[tomli](https://github.com/hukkin/tomli)|`{'v1': 'null', 'v2': 'None'}`|
|[qtoml](https://github.com/alethiophile/qtoml)|`{'v1': 'null', 'v2': 'None'}`|
|[tomlkit](https://github.com/sdispater/tomlkit)|`{'v1': 'null', 'v2': 'None'}`|

### TestDumpKeysOrder

Whether the package preserves the order of the keys while dumps
    a python dictionary. Thus, whether
    `<package>.dumps({"c": 1, "a": 2, "b": 3})` yields
    a string like `c = 1\na = 2\nb = 3\n`.


|Package|Keys order kept?|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Kept|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Kept|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Lost|
|[tomli](https://github.com/hukkin/tomli)|Kept|
|[qtoml](https://github.com/alethiophile/qtoml)|Kept|
|[tomlkit](https://github.com/sdispater/tomlkit)|Kept|

### TestLoadKeysOrder

Whether the package preserves the order of the keys while loads
    a TOML string. Thus, whether
    `<package>.loads('c = 1
a = 2
b = 3
')` yields a dictionary
    with keys in the order of `['c', 'a', 'b']`.


|Package|Keys order kept?|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Kept|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Kept|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Lost|
|[tomli](https://github.com/hukkin/tomli)|Kept|
|[qtoml](https://github.com/alethiophile/qtoml)|Kept|
|[tomlkit](https://github.com/sdispater/tomlkit)|Kept|

### TestDumpsUnicode

How the package dumps Unicode in python,
    literally, `<api>.dumps({"你好": "世界"})`

|Package|Dumped value|
|:------|:------|
|[toml](https://github.com/uiri/toml)|`"你好" = "世界" `|
|[rtoml](https://github.com/samuelcolvin/rtoml)|`"你好" = "世界" `|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|`'你好' = '世界'`|
|[tomli](https://github.com/hukkin/tomli)|`"你好" = "世界" `|
|[qtoml](https://github.com/alethiophile/qtoml)|`'你好' = '世界' `|
|[tomlkit](https://github.com/sdispater/tomlkit)|`"你好" = "世界" `|

### TestLoadUnicode

How the package loads a file with unicode.

    # Create a file with unicode content
    with open(self.datafile, "w", encoding="utf-8") as f:
        f.write('"你好" = "世界"\n')

    # Use `<api>.load()` to load the file
    with open(self.datafile, "r", encoding="utf-8") as f:
        loaded = self.api.load(f)


|Package|Loaded as|
|:------|:------|
|[toml](https://github.com/uiri/toml)|`{'你好': '世界'}`|
|[rtoml](https://github.com/samuelcolvin/rtoml)|`{'你好': '世界'}`|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|`{'你好': '世界'}`|
|[tomli](https://github.com/hukkin/tomli)|```TypeError: File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')` ```<br />**When load with:**<br />`with open(datafile, 'rb') as f:`<br />`　   loaded = self.api.load(f)`<br />**Yields:**<br />`{'你好': '世界'}`|
|[qtoml](https://github.com/alethiophile/qtoml)|`{'你好': '世界'}`|
|[tomlkit](https://github.com/sdispater/tomlkit)|`{'你好': '世界'}`|

### TestComplianceValid

Test the compliance with the standard test suites for
        valid toml files here:

    https://github.com/BurntSushi/toml-test/

The tests come up with a JSON counterpart that can be used to valid whether
loading the toml file yields the same result as the JSON counterpart.


|Package|Result (BurntSushi/toml-test v1.0.0)|
|:------|:------|
|[toml](https://github.com/uiri/toml)|[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/comment/tricky.toml) Parsed as unexpected data.<br />[array/mixed-int-array.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/array/mixed-int-array.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-int-float.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/array/mixed-int-float.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-string-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/array/mixed-string-table.toml) list index out of range<br />[array/mixed-int-string.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/array/mixed-int-string.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/nested-double.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/array/nested-double.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[float/zero.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/float/zero.toml) Weirdness with leading zeroes or underscores in your number. (line 4 column 1 char 29)<br />[key/escapes.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/key/escapes.toml) Parsed as unexpected data.<br />[key/dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/key/dotted.toml) Found invalid character in key name: '"'. Try quoting the key name. (line 12 column 11 char 245)<br />[inline-table/key-dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/inline-table/key-dotted.toml) Parsed as unexpected data.<br />[inline-table/multiline.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/inline-table/multiline.toml) Invalid inline table value encountered (line 1 column 1 char 0)<br />[datetime/local-time.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/datetime/local-time.toml) Parsed as unexpected data.<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/datetime/datetime.toml) Parsed as unexpected data.<br />*83/96 (86.46%) passed*|
|[rtoml](https://github.com/samuelcolvin/rtoml)|[key/empty.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/key/empty.toml) empty table key found at line 1 column 1<br />*95/96 (98.96%) passed*|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|OK, *96/96 (100%) passed*|
|[tomli](https://github.com/hukkin/tomli)|OK, *96/96 (100%) passed*|
|[qtoml](https://github.com/alethiophile/qtoml)|[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/comment/tricky.toml) can't parse type (line 11, column 7)<br />[string/multiline-quotes.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/string/multiline-quotes.toml) Didn't find expected newline (line 4, column 26)<br />[datetime/milliseconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/datetime/milliseconds.toml) Didn't find expected newline (line 2, column 27)<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//valid/datetime/datetime.toml) Didn't find expected newline (line 2, column 18)<br />*92/96 (95.83%) passed*|
|[tomlkit](https://github.com/sdispater/tomlkit)|OK, *96/96 (100%) passed*|

### TestComplianceInvalid

Test the compliance with the standard test suites for
        invalid toml files here:

    https://github.com/BurntSushi/toml-test/

- `Not OK`: The toml file is parsed without error, but expected to fail.
- `OK`: All files are failed to parse, as expected. Showing the last parsing
    error.


|Package|Result (BurntSushi/toml-test v1.0.0)|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Not OK: [integer/us-after-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/us-after-hex.toml) incorrectly parsed.<br />Not OK: [integer/us-after-oct.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/us-after-oct.toml) incorrectly parsed.<br />Not OK: [integer/double-sign-plus.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/double-sign-plus.toml) incorrectly parsed.<br />Not OK: [integer/double-sign-nex.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/double-sign-nex.toml) incorrectly parsed.<br />Not OK: [integer/us-after-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/us-after-bin.toml) incorrectly parsed.<br />Not OK: [array/no-close.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/array/no-close.toml) incorrectly parsed.<br />Not OK: [array/tables-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/array/tables-1.toml) incorrectly parsed.<br />Not OK: [array/no-close-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/array/no-close-2.toml) incorrectly parsed.<br />Not OK: [array/no-close-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/array/no-close-table.toml) incorrectly parsed.<br />Not OK: [array/no-close-table-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/array/no-close-table-2.toml) incorrectly parsed.<br />Not OK: *29 more items incorrectly parsed.*<br />*146/185 (78.92%) passed*|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Not OK: [integer/positive-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/positive-hex.toml) incorrectly parsed.<br />Not OK: [integer/positive-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/integer/positive-bin.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />*182/185 (98.38%) passed*|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|OK: [table/nested-brackets-close.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/table/nested-brackets-close.toml) Error while parsing table header: expected a comment or whitespace, saw 'b' 	(error occurred at line 1, column 4)<br /> *185/185 (100%) passed*|
|[tomli](https://github.com/hukkin/tomli)|OK: [table/nested-brackets-close.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/table/nested-brackets-close.toml) Expected newline or end of document after a statement (at line 1, column 4)<br /> *185/185 (100%) passed*|
|[qtoml](https://github.com/alethiophile/qtoml)|OK: [table/nested-brackets-close.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/table/nested-brackets-close.toml) 'in <string>' requires string as left operand, not int<br /> *185/185 (100%) passed*|
|[tomlkit](https://github.com/sdispater/tomlkit)|Not OK: [encoding/bad-utf8-in-comment.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/encoding/bad-utf8-in-comment.toml) incorrectly parsed.<br />Not OK: [encoding/bad-utf8-in-string.toml](https://github.com/BurntSushi/toml-test/blob/v1.0.0/tests//invalid/encoding/bad-utf8-in-string.toml) incorrectly parsed.<br />*183/185 (98.92%) passed*|

### TestSpeedWithPytomlppData

Test the speed of loading data provided by pytomlpp.


    https://github.com/bobfang1992/pytomlpp/raw/master/benchmark/data.toml

|Package|Result|
|:------|:------|
|[toml](https://github.com/uiri/toml)|6.25s (5000 iterations)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|0.72s (5000 iterations)|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|0.87s (5000 iterations)|
|[tomli](https://github.com/hukkin/tomli)|3.10s (5000 iterations)|
|[qtoml](https://github.com/alethiophile/qtoml)|9.69s (5000 iterations)|
|[tomlkit](https://github.com/sdispater/tomlkit)|53.57s (5000 iterations)|

### TestSpeedWithRtomlData

Test the speed of loading data provided by rtoml.

    https://github.com/samuelcolvin/rtoml/raw/main/benchmarks/data.toml

|Package|Result|
|:------|:------|
|[toml](https://github.com/uiri/toml)|16.20s (5000 iterations)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|1.33s (5000 iterations)|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|1.23s (5000 iterations)|
|[tomli](https://github.com/hukkin/tomli)|6.65s (5000 iterations)|
|[qtoml](https://github.com/alethiophile/qtoml)|18.71s (5000 iterations)|
|[tomlkit](https://github.com/sdispater/tomlkit)|140.71s (5000 iterations)|

### TestSpeedWithTomliData

Test the speed of loading data provided by tomli.

    https://github.com/hukkin/tomli/raw/master/benchmark/data.toml

|Package|Result|
|:------|:------|
|[toml](https://github.com/uiri/toml)|12.57s (5000 iterations)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|1.01s (5000 iterations)|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|1.11s (5000 iterations)|
|[tomli](https://github.com/hukkin/tomli)|4.35s (5000 iterations)|
|[qtoml](https://github.com/alethiophile/qtoml)|13.82s (5000 iterations)|
|[tomlkit](https://github.com/sdispater/tomlkit)|81.82s (5000 iterations)|

