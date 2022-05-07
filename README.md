# toml-bench

Which toml package to use in python?

See also: [PEP 680](https://www.python.org/dev/peps/pep-0680/)


## Report

### Version

The verions of the packages tested in this report.

|Package|Version|
|:------|:------|
|[toml](https://github.com/uiri/toml)|0.10.2|
|[rtoml](https://github.com/samuelcolvin/rtoml)|0.7.1|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|1.0.11|
|[tomli](https://github.com/hukkin/tomli)|0.4.0|
|[qtoml](https://github.com/alethiophile/qtoml)|0.3.1|
|[tomlkit](https://github.com/sdispater/tomlkit)|0.7.2|

### TestDumpNone

How the package dumps `None` value in python,
    literally `<package>.dumps(None)`
    

|Package|Dumped value or error|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Raises 'NoneType' object is not iterable|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Dumps to `"null"`|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Raises dumps(): incompatible function arguments. The following argument types are supported:     1. (arg0: dict) -> str  Invoked with: None|
|[tomli](https://github.com/hukkin/tomli)|Raises 'NoneType' object has no attribute 'items'|
|[qtoml](https://github.com/alethiophile/qtoml)|Raises 'NoneType' object has no attribute 'items'|
|[tomlkit](https://github.com/sdispater/tomlkit)|Raises 'NoneType' object has no attribute 'as_string'|

### TestDumpValueNone

How the package dumps key-value pair with value `None`,
    literally `<package>.dumps({"key": None})`
    

|Package|Dumped value or error|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Ignores the key (dumps to an empty string)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Dumps to `key = "null" `|
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
|[toml](https://github.com/uiri/toml)|{'v1': 'null', 'v2': 'None'}|
|[rtoml](https://github.com/samuelcolvin/rtoml)|{'v1': 'null', 'v2': 'None'}|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|{'v1': 'null', 'v2': 'None'}|
|[tomli](https://github.com/hukkin/tomli)|{'v1': 'null', 'v2': 'None'}|
|[qtoml](https://github.com/alethiophile/qtoml)|{'v1': 'null', 'v2': 'None'}|
|[tomlkit](https://github.com/sdispater/tomlkit)|{'v1': 'null', 'v2': 'None'}|

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

### TestComplianceInvalid

Test the compliance with the standard test suites for
    invalid toml files here:

    https://github.com/BurntSushi/toml-test/

- `Not OK`: The toml file is parsed without error, but expected to fail.
- `OK`: All files are failed to parse, as expected. Showing the last parsing
    error.
    

|Package|Result (BurntSushi/toml-test v1.1.0)|
|:------|:------|
|[toml](https://github.com/uiri/toml)|Not OK: [integer/us-after-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/us-after-hex.toml) incorrectly parsed.<br />Not OK: [integer/us-after-oct.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/us-after-oct.toml) incorrectly parsed.<br />Not OK: [integer/double-sign-plus.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/double-sign-plus.toml) incorrectly parsed.<br />Not OK: [integer/double-sign-nex.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/double-sign-nex.toml) incorrectly parsed.<br />Not OK: [integer/us-after-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/us-after-bin.toml) incorrectly parsed.<br />Not OK: [array/no-close.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/array/no-close.toml) incorrectly parsed.<br />Not OK: [array/tables-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/array/tables-1.toml) incorrectly parsed.<br />Not OK: [array/no-close-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/array/no-close-2.toml) incorrectly parsed.<br />Not OK: [array/no-close-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/array/no-close-table.toml) incorrectly parsed.<br />Not OK: [array/no-close-table-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/array/no-close-table-2.toml) incorrectly parsed.<br />Not OK: [float/inf_underscore.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/inf_underscore.toml) incorrectly parsed.<br />Not OK: [float/nan_underscore.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/nan_underscore.toml) incorrectly parsed.<br />Not OK: [float/exp-point-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/exp-point-2.toml) incorrectly parsed.<br />Not OK: [float/trailing-us-exp.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/trailing-us-exp.toml) incorrectly parsed.<br />Not OK: [float/exp-leading-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/exp-leading-us.toml) incorrectly parsed.<br />Not OK: [key/two-equals3.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/key/two-equals3.toml) incorrectly parsed.<br />Not OK: [key/escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/key/escape.toml) incorrectly parsed.<br />Not OK: [key/two-equals2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/key/two-equals2.toml) incorrectly parsed.<br />Not OK: [key/special-character.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/key/special-character.toml) incorrectly parsed.<br />Not OK: [inline-table/add.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/inline-table/add.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/rawstring-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawstring-null.toml) incorrectly parsed.<br />Not OK: [control/string-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/string-del.toml) incorrectly parsed.<br />Not OK: [control/string-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/string-null.toml) incorrectly parsed.<br />Not OK: [control/rawmulti-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawmulti-del.toml) incorrectly parsed.<br />Not OK: [control/string-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/string-us.toml) incorrectly parsed.<br />Not OK: [control/comment-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-null.toml) incorrectly parsed.<br />Not OK: [control/rawstring-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawstring-del.toml) incorrectly parsed.<br />Not OK: [control/rawstring-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawstring-lf.toml) incorrectly parsed.<br />Not OK: [control/rawmulti-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawmulti-null.toml) incorrectly parsed.<br />Not OK: [control/rawmulti-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawmulti-us.toml) incorrectly parsed.<br />Not OK: [control/multi-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/multi-lf.toml) incorrectly parsed.<br />Not OK: [control/multi-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/multi-us.toml) incorrectly parsed.<br />Not OK: [control/string-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/string-lf.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/string-bs.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/string-bs.toml) incorrectly parsed.<br />Not OK: [control/rawmulti-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawmulti-lf.toml) incorrectly parsed.<br />Not OK: [control/comment-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-us.toml) incorrectly parsed.<br />Not OK: [control/multi-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/multi-del.toml) incorrectly parsed.<br />Not OK: [control/rawstring-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/rawstring-us.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [control/multi-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/multi-null.toml) incorrectly parsed.<br />Not OK: [control/comment-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-lf.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-1.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-2.toml) incorrectly parsed.<br />*169/214 (78.97%) passed*|
|[rtoml](https://github.com/samuelcolvin/rtoml)|Not OK: [integer/positive-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/positive-hex.toml) incorrectly parsed.<br />Not OK: [integer/positive-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/integer/positive-bin.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />*209/214 (97.66%) passed*|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />*212/214 (99.07%) passed*|
|[tomli](https://github.com/hukkin/tomli)|Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-1.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-2.toml) incorrectly parsed.<br />*210/214 (98.13%) passed*|
|[qtoml](https://github.com/alethiophile/qtoml)|Not OK: [inline-table/add.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/inline-table/add.toml) incorrectly parsed.<br />Not OK: [inline-table/trailing-comma.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/inline-table/trailing-comma.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/comment-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-null.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-us.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-lf.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-1.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-2.toml) incorrectly parsed.<br />Not OK: [table/duplicate-key-dotted-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/duplicate-key-dotted-table.toml) incorrectly parsed.<br />Not OK: [table/duplicate-key-dotted-table2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/duplicate-key-dotted-table2.toml) incorrectly parsed.<br />*202/214 (94.39%) passed*|
|[tomlkit](https://github.com/sdispater/tomlkit)|Not OK: [float/leading-point-plus.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/leading-point-plus.toml) incorrectly parsed.<br />Not OK: [float/exp-point-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/exp-point-2.toml) incorrectly parsed.<br />Not OK: [float/leading-point-neg.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/float/leading-point-neg.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-1.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//invalid/table/append-with-dotted-keys-2.toml) incorrectly parsed.<br />*207/214 (96.73%) passed*|

### TestComplianceValid

Test the compliance with the standard test suites for
    valid toml files here:

    https://github.com/BurntSushi/toml-test/

The tests come up with a JSON counterpart that can be used to valid whether
loading the toml file yields the same result as the JSON counterpart.
    

|Package|Result (BurntSushi/toml-test v1.1.0)|
|:------|:------|
|[toml](https://github.com/uiri/toml)|[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/comment/tricky.toml) Parsed as unexpected data.<br />[array/mixed-int-array.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/array/mixed-int-array.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-int-float.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/array/mixed-int-float.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-string-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/array/mixed-string-table.toml) list index out of range<br />[array/mixed-int-string.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/array/mixed-int-string.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/nested-double.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/array/nested-double.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[float/zero.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/float/zero.toml) Weirdness with leading zeroes or underscores in your number. (line 4 column 1 char 47)<br />[key/escapes.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/key/escapes.toml) Parsed as unexpected data.<br />[key/dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/key/dotted.toml) Found invalid character in key name: '"'. Try quoting the key name. (line 12 column 11 char 245)<br />[inline-table/key-dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/inline-table/key-dotted.toml) Parsed as unexpected data.<br />[inline-table/multiline.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/inline-table/multiline.toml) Invalid inline table value encountered (line 1 column 1 char 0)<br />[datetime/local-time.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/datetime/local-time.toml) Parsed as unexpected data.<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/datetime/datetime.toml) Parsed as unexpected data.<br />*86/99 (86.87%) passed*|
|[rtoml](https://github.com/samuelcolvin/rtoml)|[key/empty.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/key/empty.toml) empty table key found at line 1 column 1<br />*98/99 (98.99%) passed*|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|OK, *99/99 (100%) passed*|
|[tomli](https://github.com/hukkin/tomli)|[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/datetime/datetime.toml) Expected newline or end of document after a statement (at line 2, column 19)<br />*98/99 (98.99%) passed*|
|[qtoml](https://github.com/alethiophile/qtoml)|[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/comment/tricky.toml) can't parse type (line 11, column 7)<br />[string/multiline-quotes.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/string/multiline-quotes.toml) Didn't find expected newline (line 4, column 26)<br />[datetime/milliseconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/datetime/milliseconds.toml) Didn't find expected newline (line 2, column 27)<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/datetime/datetime.toml) Didn't find expected newline (line 2, column 18)<br />*95/99 (95.96%) passed*|
|[tomlkit](https://github.com/sdispater/tomlkit)|[key/escapes.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/key/escapes.toml) Unexpected character: 'j' at line 3 col 8<br />[key/dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/key/dotted.toml) Unexpected character: '.' at line 4 col 6<br />[inline-table/key-dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/inline-table/key-dotted.toml) Unexpected character: '.' at line 6 col 11<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/datetime/datetime.toml) Invalid number at line 2 col 28<br />[table/names.toml](https://github.com/BurntSushi/toml-test/blob/v1.1.0/tests//valid/table/names.toml) Parsed as unexpected data.<br />*94/99 (94.95%) passed*|

### TestWithPytomlppData

Test the speed of loading data provided by pytomlpp.


    https://github.com/bobfang1992/pytomlpp/raw/master/benchmark/data.toml

|Package|Result|
|:------|:------|
|[toml](https://github.com/uiri/toml)|6.76s (5000 iterations)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|0.79s (5000 iterations)|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|0.92s (5000 iterations)|
|[tomli](https://github.com/hukkin/tomli)|3.40s (5000 iterations)|
|[qtoml](https://github.com/alethiophile/qtoml)|10.14s (5000 iterations)|
|[tomlkit](https://github.com/sdispater/tomlkit)|50.81s (5000 iterations)|

### TestWithRtomlData

Test the speed of loading data provided by rtoml.

    https://github.com/samuelcolvin/rtoml/raw/main/benchmarks/data.toml

|Package|Result|
|:------|:------|
|[toml](https://github.com/uiri/toml)|16.59s (5000 iterations)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|1.30s (5000 iterations)|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|1.26s (5000 iterations)|
|[tomli](https://github.com/hukkin/tomli)|7.43s (5000 iterations)|
|[qtoml](https://github.com/alethiophile/qtoml)|18.90s (5000 iterations)|
|[tomlkit](https://github.com/sdispater/tomlkit)|105.06s (5000 iterations)|

### TestWithTomliData

Test the speed of loading data provided by tomli.

    https://github.com/hukkin/tomli/raw/master/benchmark/data.toml

|Package|Result|
|:------|:------|
|[toml](https://github.com/uiri/toml)|10.43s (5000 iterations)|
|[rtoml](https://github.com/samuelcolvin/rtoml)|0.99s (5000 iterations)|
|[pytomlpp](https://github.com/bobfang1992/pytomlpp)|1.16s (5000 iterations)|
|[tomli](https://github.com/hukkin/tomli)|4.49s (5000 iterations)|
|[qtoml](https://github.com/alethiophile/qtoml)|13.32s (5000 iterations)|
|[tomlkit](https://github.com/sdispater/tomlkit)|72.39s (5000 iterations)|


## Run your own report

### Install

```shell
pip install -U toml-bench
```

### Generate your own report

```shell
toml-bench
```

#### Use a different data directory than the default one

```shell
toml-bench --datadir /tmp/toml-bench
```

#### Write the report to a markdown file

```shell
toml-bench --report ./README.md
```

#### Test with a different version of compliance set (`BurntSushi/toml-test`)

```shell
toml-bench --comver 1.0.0
```

#### Use a different number of iterations in speed tests

```shell
toml-bench --iter 1000
```

#### Test with different versions of packages

```shell
git clone https://github.com/pwwang/toml-bench.git
cd toml-bench
# See https://python-poetry.org/docs/cli/#add
# for how to specify a version constraint
poetry add "tomli=2.0.0"
poetry update
poetry install
poetry run toml-bench
```

