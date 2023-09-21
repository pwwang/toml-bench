# Report

## Version

The verions of the packages tested in this report.

| |Version|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|0.10.2|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|2.0.1; **tomli_w**: 1.0.0|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|0.11.8|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|1.0.13|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|0.9.0|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|0.3.1|

## Dumping `None` value

How the package dumps `None` value in python

Literally `<package>.dumps(None)`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|'NoneType' object is not iterable|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|'NoneType' object has no attribute 'items'|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Expecting Mapping or TOML Container, <class 'NoneType'> given|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|dumps(): incompatible function arguments. The following argument types are supported:<br />    1. (arg0: dict) -> str<br /><br />Invoked with: None|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|"null"|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|'NoneType' object has no attribute 'items'|

## Dumping key-`None` pair

How the package dumps key-value pair with value `None`

Literally `<package>.dumps({"key": None})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>||
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Object of type <class 'NoneType'> is not TOML serializable|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Invalid type <class 'NoneType'>|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|cannot convert value None to proper toml type<br />|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|key = "null"<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|TOML cannot encode None|

## Dumping list with `None` value

How the package dumps a list with `None` value in it.

Literally `<package>.dumps({"key": [1, 2, 3, None, 5]})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|key = [ 1, 2, 3, "None", 5,]<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Object of type <class 'NoneType'> is not TOML serializable|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Invalid type <class 'NoneType'>|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|not a valid type for conversion None|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|key = [1, 2, 3, "null", 5]<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|bad type '<class 'NoneType'>' for dump_value|

## Loading `None`-like values

How the package loads `None`-like value in string

Literally `<package>.loads('v1 = "null" v2 = "None"')`


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|{'v1': 'null', 'v2': 'None'}|

## Dumping a heterogenous array

How the package dumps a python dictionary with a heterogenous array.

Literally `<package>.dumps({"v": [1, 1.2, True, "string"]})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|v&nbsp;=&nbsp;\[&nbsp;1,&nbsp;1.2,&nbsp;true,&nbsp;"string",\]<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|v&nbsp;=&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;1,<br />&nbsp;&nbsp;&nbsp;&nbsp;1.2,<br />&nbsp;&nbsp;&nbsp;&nbsp;true,<br />&nbsp;&nbsp;&nbsp;&nbsp;"string",<br />\]<br />|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|v&nbsp;=&nbsp;\[1,&nbsp;1.2,&nbsp;true,&nbsp;"string"\]<br />|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|v&nbsp;=&nbsp;\[&nbsp;1,&nbsp;1.2,&nbsp;1,&nbsp;'string'&nbsp;\]|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|v&nbsp;=&nbsp;\[1,&nbsp;1.2,&nbsp;true,&nbsp;"string"\]<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|v&nbsp;=&nbsp;\[1,&nbsp;1.2,&nbsp;true,&nbsp;'string'\]<br />|

## Loading a heterogenous array

How the package loads a toml string with a heterogenous array.

Literally `<package>.loads('v = [1, 1.2, True, "string"]')`


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Not a homogeneous array (line 2 column 1 char 1)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|`{'v': [1, 1.2, True, 'string']}`|

## Dumping a nested array

How the package dumps a python dictionary with a nested array.

Literally `<package>.dumps({"v": [[1], [1, 2]]})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|v&nbsp;=&nbsp;\[&nbsp;\[&nbsp;1,\],&nbsp;\[&nbsp;1,&nbsp;2,\],\]<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|v&nbsp;=&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,<br />&nbsp;&nbsp;&nbsp;&nbsp;\],<br />&nbsp;&nbsp;&nbsp;&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2,<br />&nbsp;&nbsp;&nbsp;&nbsp;\],<br />\]<br />|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|v&nbsp;=&nbsp;\[\[1\],&nbsp;\[1,&nbsp;2\]\]<br />|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|v&nbsp;=&nbsp;\[&nbsp;\[&nbsp;1&nbsp;\],&nbsp;\[&nbsp;1,&nbsp;2&nbsp;\]&nbsp;\]|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|v&nbsp;=&nbsp;\[\[1\],&nbsp;\[1,&nbsp;2\]\]<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|v&nbsp;=&nbsp;\[\[1\],&nbsp;\[1,&nbsp;2\]\]<br />|

## Loading a nested array

How the package loads a toml string with a nested array.

Literally `<package>.loads('v = [[1], [1, 2]]')`


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|`{'v': [[1], [1, 2]]}`|

## Dumping keeps order of keys?

Whether the package preserves the order of the keys while dumps
a python dictionary.

Thus, whether `<package>.dumps({"c": 1, "a": 2, "b": 3})` yields a string
like `c = 1\na = 2\nb = 3\n`.


| |Order kept?|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Kept|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Kept|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Kept|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|Lost|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Kept|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Kept|

## Loading keeps order of keys?

Whether the package preserves the order of the keys
while loads a TOML string.

Thus, whether `<package>.loads('c = 1\na = 2\nb = 3\n')` yields
a dictionary with keys in the order of `['c', 'a', 'b']`.


| |Order kept?|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Kept|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Kept|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Kept|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|Lost|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Kept|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Kept|

## Dumping unicode

How the package dumps Unicode in python

Literally, `<package>.dumps({"你好": "世界"})`


| |Dumped value|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|'你好' = '世界'|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|'你好' = '世界'<br />|

## Loaded unicode

How the package loads a file with unicode.

The file was created by:

```python
# Create a file with unicode content
with open(self.datafile, "w", encoding="utf-8") as f:
    f.write('"你好" = "世界"\n')

# Use `<package>.load()` to load the file
with open(self.datafile, "r", encoding="utf-8") as f:
    loaded = <package>.load(f)
```


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`<br />When loaded with `rb`:<br />{'你好': '世界'}|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|{'你好': '世界'}|

## Compliance with valid tests in toml-test

Test the compliance with the standard test suites for valid toml files
here:

> https://github.com/BurntSushi/toml-test/

The tests come up with a JSON counterpart that can be used to valid whether
loading the toml file yields the same result as the JSON counterpart.


| |Result (toml-test v1.2.0)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|[key/escapes.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/key/escapes.toml) Parsed as unexpected data.<br />[key/dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/key/dotted.toml) Found invalid character in key name: '"'. Try quoting the key name. (line 12 column 11 char 245)<br />[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/comment/tricky.toml) Parsed as unexpected data.<br />[inline-table/key-dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/inline-table/key-dotted.toml) Parsed as unexpected data.<br />[inline-table/multiline.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/inline-table/multiline.toml) Invalid inline table value encountered (line 1 column 1 char 0)<br />[array/nested-double.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/array/nested-double.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-int-string.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/array/mixed-int-string.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-string-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/array/mixed-string-table.toml) list index out of range<br />[array/mixed-int-array.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/array/mixed-int-array.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-int-float.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/array/mixed-int-float.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[float/zero.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/float/zero.toml) Weirdness with leading zeroes or underscores in your number. (line 4 column 1 char 47)<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/escape-esc.toml) Reserved escape sequence used (line 1 column 1 char 0)<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/datetime/datetime.toml) Parsed as unexpected data.<br />[datetime/local-time.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/datetime/local-time.toml) Parsed as unexpected data.<br />*86/100 (86.00%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/escape-esc.toml) Unescaped '\' in a string (at line 1, column 10)<br />*99/100 (99.00%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/escape-esc.toml) Invalid character 'e' in string at line 1 col 8<br />*99/100 (99.00%) passed*|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/escape-esc.toml) Error while parsing string: escape sequence '\e' is not supported in TOML 1.0.0 and earlier 	(error occurred at line 1, column 9)<br />*99/100 (99.00%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/escape-esc.toml) invalid escape character in string: `e` at line 1 column 9<br />*99/100 (99.00%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/comment/tricky.toml) can't parse type (line 11, column 7)<br />[string/multiline-quotes.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/multiline-quotes.toml) Didn't find expected newline (line 4, column 26)<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/string/escape-esc.toml) \e not a valid escape (line 1, column 33)<br />[datetime/milliseconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/datetime/milliseconds.toml) Didn't find expected newline (line 2, column 27)<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//valid/datetime/datetime.toml) Didn't find expected newline (line 2, column 18)<br />*95/100 (95.00%) passed*|

## Compliance with invalid tests in toml-test

Test the compliance with the standard test suites for invalid toml files
here:

> https://github.com/BurntSushi/toml-test/

- `Not OK`: The toml file is parsed without error, but expected to fail.
- `OK`: All files are failed to parse, as expected. Showing the last
parsing error.


| |Result (toml-test v1.2.0)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Not OK: [key/escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/key/escape.toml) incorrectly parsed.<br />Not OK: [key/special-character.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/key/special-character.toml) incorrectly parsed.<br />Not OK: [key/two-equals3.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/key/two-equals3.toml) incorrectly parsed.<br />Not OK: [key/two-equals2.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/key/two-equals2.toml) incorrectly parsed.<br />Not OK: [inline-table/add.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/inline-table/add.toml) incorrectly parsed.<br />Not OK: [array/no-close-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/array/no-close-2.toml) incorrectly parsed.<br />Not OK: [array/tables-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/array/tables-1.toml) incorrectly parsed.<br />Not OK: [array/no-close.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/array/no-close.toml) incorrectly parsed.<br />Not OK: [array/extending-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/array/extending-table.toml) incorrectly parsed.<br />Not OK: [array/no-close-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/array/no-close-table.toml) incorrectly parsed.<br />Not OK: *36 more items incorrectly parsed.*<br />*177/223 (79.37%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|OK: [datetime/mday-under.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/datetime/mday-under.toml) Expected newline or end of document after a statement (at line 3, column 9)<br /> *223/223 (100%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/table/append-with-dotted-keys-2.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/table/append-with-dotted-keys-1.toml) incorrectly parsed.<br />*219/223 (98.21%) passed*|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />*221/223 (99.10%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [integer/positive-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/integer/positive-hex.toml) incorrectly parsed.<br />Not OK: [integer/positive-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/integer/positive-bin.toml) incorrectly parsed.<br />*218/223 (97.76%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Not OK: [inline-table/trailing-comma.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/inline-table/trailing-comma.toml) incorrectly parsed.<br />Not OK: [inline-table/add.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/inline-table/add.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-us.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-us.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/comment-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-lf.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/comment-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/control/comment-null.toml) incorrectly parsed.<br />Not OK: [table/duplicate-key-dotted-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/table/duplicate-key-dotted-table.toml) incorrectly parsed.<br />Not OK: [table/duplicate-key-dotted-table2.toml](https://github.com/BurntSushi/toml-test/blob/v1.2.0/tests//invalid/table/duplicate-key-dotted-table2.toml) incorrectly parsed.<br />Not OK: *2 more items incorrectly parsed.*<br />*211/223 (94.62%) passed*|

## Compliance with valid tests in python tomllib test data

Test the compliance with python tomllib test data (since python 3.11)
for valid toml files here:

> https://github.com/python/cpython/tree/3.11/Lib/test/test_tomllib/data/valid

The tests come up with a JSON counterpart that can be used to valid whether
loading the toml file yields the same result as the JSON counterpart.


| |Result (cpython tag 3.11.0)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|[apostrophes-in-literal-string.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/apostrophes-in-literal-string.toml) Unbalanced quotes (line 1 column 50 char 49)<br />[five-quotes.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/five-quotes.toml) Unterminated string found. Reached end of file. (line 7 column 1 char 97)<br />[dates-and-times/datetimes.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/dates-and-times/datetimes.toml) Parsed as unexpected data.<br />[multiline-basic-str/ends-in-whitespace-escape.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/multiline-basic-str/ends-in-whitespace-escape.toml) Reserved escape sequence used (line 6 column 1 char 28)<br />*8/12 (66.67%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|[apostrophes-in-literal-string.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/apostrophes-in-literal-string.toml) Didn't find expected newline (line 3, column 3)<br />[five-quotes.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/five-quotes.toml) Didn't find expected newline (line 3, column 3)<br />[dates-and-times/datetimes.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//valid/dates-and-times/datetimes.toml) Didn't find expected newline (line 1, column 19)<br />*9/12 (75.00%) passed*|

## Compliance with invalid tests in python tomllib test data

Test the compliance with python tomllib test data (since python 3.11)
for invalid toml files here:

> https://github.com/python/cpython/tree/main/Lib/test/test_tomllib/data/invalid

- `Not OK`: The toml file is parsed without error, but expected to fail.
- `OK`: All files are failed to parse, as expected. Showing the last
parsing error.


| |Result (cpython tag 3.11.0)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Not OK: [invalid-comment-char.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/invalid-comment-char.toml) incorrectly parsed.<br />Not OK: [inline-table/unclosed-empty.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/inline-table/unclosed-empty.toml) incorrectly parsed.<br />Not OK: [inline-table/overwrite-value-in-inner-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/inline-table/overwrite-value-in-inner-table.toml) incorrectly parsed.<br />Not OK: [array/unclosed-empty.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/array/unclosed-empty.toml) incorrectly parsed.<br />Not OK: [array/unclosed-after-item.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/array/unclosed-after-item.toml) incorrectly parsed.<br />Not OK: [array/file-end-after-val.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/array/file-end-after-val.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table-with-subtable.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table-with-subtable.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table.toml) incorrectly parsed.<br />Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />*41/50 (82.00%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|OK: [multiline-basic-str/escape-only.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/multiline-basic-str/escape-only.toml) Unterminated string (at end of document)<br /> *50/50 (100%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Not OK: [inline-table/override-val-in-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/inline-table/override-val-in-table.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table-with-subtable.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table-with-subtable.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-aot.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-aot.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table.toml) incorrectly parsed.<br />Not OK: [array-of-tables/overwrite-array-in-parent.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/array-of-tables/overwrite-array-in-parent.toml) incorrectly parsed.<br />Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />*44/50 (88.00%) passed*|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />*49/50 (98.00%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />*49/50 (98.00%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Not OK: [non-scalar-escaped.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/non-scalar-escaped.toml) incorrectly parsed.<br />Not OK: [invalid-comment-char.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/invalid-comment-char.toml) incorrectly parsed.<br />Not OK: [inline-table/override-val-with-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/inline-table/override-val-with-table.toml) incorrectly parsed.<br />Not OK: [inline-table/overwrite-value-in-inner-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/inline-table/overwrite-value-in-inner-table.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table-with-subtable.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table-with-subtable.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table.toml) incorrectly parsed.<br />Not OK: [table/redefine-2.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/table/redefine-2.toml) incorrectly parsed.<br />Not OK: [table/redefine-1.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/table/redefine-1.toml) incorrectly parsed.<br />Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.11.0/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />*41/50 (82.00%) passed*|

## Running speed with data provided by `pytomlpp`

Test the speed of loading and dumping the loaded
using data provided by `pytomlpp`

> https://github.com/bobfang1992/pytomlpp/raw/master/benchmark/data.toml


| |Loading speed|Dumping speed|
|-|-|-|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Excluded (heterogeneous arrays not supported)|Excluded (heterogeneous arrays not supported)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|7.34s (1000 iterations)|3.21s (1000 iterations)|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|146.22s (1000 iterations)|2.32s (1000 iterations)|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|1.61s (1000 iterations)|1.08s (1000 iterations)|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|1.00s (1000 iterations)|values must be emitted before tables|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|18.91s (1000 iterations)|5.37s (1000 iterations)|

## Running speed with data provided by `rtoml`

Test the speed of loading and dumping the loaded using data
provided by `rtoml`

> https://github.com/samuelcolvin/rtoml/raw/main/tests/data.toml


| |Loading speed|Dumping speed|
|-|-|-|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Excluded (heterogeneous arrays not supported)|Excluded (heterogeneous arrays not supported)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|1.71s (1000 iterations)|0.56s (1000 iterations)|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|30.65s (1000 iterations)|0.90s (1000 iterations)|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|0.30s (1000 iterations)|0.24s (1000 iterations)|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|0.23s (1000 iterations)|0.06s (1000 iterations)|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|5.47s (1000 iterations)|1.47s (1000 iterations)|

## Running speed with data provided by `tomli`

Test the speed of loading and dumping the loaded using data
provided by `tomli`

> https://github.com/hukkin/tomli/raw/master/benchmark/data.toml


| |Loading speed|Dumping speed|
|-|-|-|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Excluded (heterogeneous arrays not supported)|Excluded (heterogeneous arrays not supported)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|1.25s (1000 iterations)|0.42s (1000 iterations)|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|19.34s (1000 iterations)|0.39s (1000 iterations)|
|<a target="_blank" href="https://github.com/bobfang1992/pytomlpp">pytomlpp</a>|0.25s (1000 iterations)|0.16s (1000 iterations)|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|0.16s (1000 iterations)|0.10s (1000 iterations)|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|3.19s (1000 iterations)|0.87s (1000 iterations)|

