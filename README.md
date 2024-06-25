# toml-bench

[![deps][1]][2]

Which toml package to use in python?

See also: [toml-lang](https://toml.io/en/) and [PEP 680](https://www.python.org/dev/peps/pep-0680/)

## Report

### Version

The verions of the packages tested in this report.

| |Version|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|0.10.2|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|2.0.1; **tomli_w**: 1.0.0|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|0.12.5|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|0.11.0|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|0.3.1|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|(Python 3.12.2)|

### Dumping `None` value

How the package dumps `None` value in python

Literally `<package>.dumps(None)`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|'NoneType' object is not iterable|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|'NoneType' object has no attribute 'items'|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Expecting Mapping or TOML Container, <class 'NoneType'> given|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|"null"<br />---<br />rtoml v0.11+ supports dumping None to a desired string:<br />`rtoml.dumps(data, none_value='@None')`:<br />"@None"|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|'NoneType' object has no attribute 'items'|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|module 'tomllib' has no attribute 'dumps'|

### Dumping key-`None` pair

How the package dumps key-value pair with value `None`

Literally `<package>.dumps({"key": None})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>||
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Object of type <class 'NoneType'> is not TOML serializable|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Invalid type <class 'NoneType'>|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|key = "null"<br /><br />---<br />rtoml v0.11+ supports dumping None to a desired string:<br />`rtoml.dumps(data, none_value='@None')`:<br />key = "@None"<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|TOML cannot encode None|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|module 'tomllib' has no attribute 'dumps'|

### Dumping list with `None` value

How the package dumps a list with `None` value in it.

Literally `<package>.dumps({"key": [1, 2, 3, None, 5]})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|key = [ 1, 2, 3, "None", 5,]<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Object of type <class 'NoneType'> is not TOML serializable|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Invalid type <class 'NoneType'>|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|key = [1, 2, 3, "null", 5]<br /><br />---<br />rtoml v0.11+ supports dumping None to a desired string:<br />`rtoml.dumps(data, none_value='@None')`:<br />key = [1, 2, 3, "@None", 5]<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|bad type '<class 'NoneType'>' for dump_value|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|module 'tomllib' has no attribute 'dumps'|

### Loading `None`-like values

How the package loads `None`-like value in string

Literally `<package>.loads('v1 = "null" v2 = "None"')`


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|module 'tomli_w' has no attribute 'loads'|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|{'v1': 'null', 'v2': 'None'}<br />---<br />rtoml v0.11+ supports loading custom None values:<br />`rtoml.loads(data, none_value='None')`:<br />{'v1': 'null', 'v2': None}<br />`rtoml.loads(data, none_value='null')`:<br />{'v1': None, 'v2': 'None'}|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|{'v1': 'null', 'v2': 'None'}|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|{'v1': 'null', 'v2': 'None'}|

### Dumping a heterogenous array

How the package dumps a python dictionary with a heterogenous array.

Literally `<package>.dumps({"v": [1, 1.2, True, "string"]})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|v&nbsp;=&nbsp;\[&nbsp;1,&nbsp;1.2,&nbsp;true,&nbsp;"string",\]<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|v&nbsp;=&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;1,<br />&nbsp;&nbsp;&nbsp;&nbsp;1.2,<br />&nbsp;&nbsp;&nbsp;&nbsp;true,<br />&nbsp;&nbsp;&nbsp;&nbsp;"string",<br />\]<br />|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|v&nbsp;=&nbsp;\[1,&nbsp;1.2,&nbsp;true,&nbsp;"string"\]<br />|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|v&nbsp;=&nbsp;\[1,&nbsp;1.2,&nbsp;true,&nbsp;"string"\]<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|v&nbsp;=&nbsp;\[1,&nbsp;1.2,&nbsp;true,&nbsp;'string'\]<br />|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|Dumping not supported|

### Loading a heterogenous array

How the package loads a toml string with a heterogenous array.

Literally `<package>.loads('v = [1, 1.2, True, "string"]')`


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Not a homogeneous array (line 2 column 1 char 1)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|`{'v': [1, 1.2, True, 'string']}`|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|`{'v': [1, 1.2, True, 'string']}`|

### Dumping a nested array

How the package dumps a python dictionary with a nested array.

Literally `<package>.dumps({"v": [[1], [1, 2]]})`


| |Dumped value or error|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|v&nbsp;=&nbsp;\[&nbsp;\[&nbsp;1,\],&nbsp;\[&nbsp;1,&nbsp;2,\],\]<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|v&nbsp;=&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,<br />&nbsp;&nbsp;&nbsp;&nbsp;\],<br />&nbsp;&nbsp;&nbsp;&nbsp;\[<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2,<br />&nbsp;&nbsp;&nbsp;&nbsp;\],<br />\]<br />|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|v&nbsp;=&nbsp;\[\[1\],&nbsp;\[1,&nbsp;2\]\]<br />|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|v&nbsp;=&nbsp;\[\[1\],&nbsp;\[1,&nbsp;2\]\]<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|v&nbsp;=&nbsp;\[\[1\],&nbsp;\[1,&nbsp;2\]\]<br />|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|Dumping not supported|

### Loading a nested array

How the package loads a toml string with a nested array.

Literally `<package>.loads('v = [[1], [1, 2]]')`


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|`{'v': [[1], [1, 2]]}`|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|`{'v': [[1], [1, 2]]}`|

### Dumping keeps order of keys?

Whether the package preserves the order of the keys while dumps
a python dictionary.

Thus, whether `<package>.dumps({"c": 1, "a": 2, "b": 3})` yields a string
like `c = 1\na = 2\nb = 3\n`.


| |Order kept?|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Kept|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Kept|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Kept|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Kept|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Kept|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|Dumping not supported|

### Loading keeps order of keys?

Whether the package preserves the order of the keys
while loads a TOML string.

Thus, whether `<package>.loads('c = 1\na = 2\nb = 3\n')` yields
a dictionary with keys in the order of `['c', 'a', 'b']`.


| |Order kept?|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Kept|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|Kept|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Kept|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Kept|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Kept|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|Kept|

### Dumping unicode

How the package dumps Unicode in python

Literally, `<package>.dumps({"你好": "世界"})`


| |Dumped value|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|"你好" = "世界"<br />|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|'你好' = '世界'<br />|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|Dumping not supported|

### Loaded unicode

How the package loads a file with unicode.

The file was created by:

```python
## Create a file with unicode content
with open(self.datafile, "w", encoding="utf-8") as f:
    f.write('"你好" = "世界"\n')

## Use `<package>.load()` to load the file
with open(self.datafile, "r", encoding="utf-8") as f:
    loaded = <package>.load(f)
```


| |Loaded as|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`<br />When loaded with `rb`:<br />{'你好': '世界'}|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|{'你好': '世界'}|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|{'你好': '世界'}|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`<br />When loaded with `rb`:<br />{'你好': '世界'}|

### Compliance with valid tests in toml-test

Test the compliance with the standard test suites for valid toml files
here:

> https://github.com/BurntSushi/toml-test/

The tests come up with a JSON counterpart that can be used to valid whether
loading the toml file yields the same result as the JSON counterpart.


| |Result (toml-test v1.5.0)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|[spec/array-0.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/spec/array-0.toml) Not a homogeneous array (line 8 column 1 char 261)<br />[spec/keys-4.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/spec/keys-4.toml) Found invalid character in key name: 'c'. Try quoting the key name. (line 2 column 8 char 57)<br />[spec/local-time-0.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/spec/local-time-0.toml) Parsed as unexpected data.<br />[datetime/no-seconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/no-seconds.toml) invalid literal for int() with base 0: '13:37' (line 2 column 1 char 46)<br />[datetime/local-time.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/local-time.toml) Parsed as unexpected data.<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/datetime.toml) Parsed as unexpected data.<br />[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/comment/tricky.toml) Parsed as unexpected data.<br />[key/dotted-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/dotted-1.toml) Parsed as unexpected data.<br />[key/unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/unicode.toml) Found invalid character in key name: '‍'. Try quoting the key name. (line 5 column 2 char 67)<br />[key/dotted-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/dotted-2.toml) Found invalid character in key name: '"'. Try quoting the key name. (line 7 column 11 char 166)<br />[key/quoted-unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/quoted-unicode.toml) Duplicate keys! (line 3 column 1 char 19)<br />[key/dotted-empty.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/dotted-empty.toml) Duplicate keys! (line 2 column 1 char 17)<br />[key/escapes.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/escapes.toml) Parsed as unexpected data.<br />[table/empty-name.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/table/empty-name.toml) Can't have a keygroup with an empty name (line 1 column 1 char 0)<br />[string/raw-multiline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/raw-multiline.toml) Unbalanced quotes (line 20 column 50 char 532)<br />[string/ends-in-whitespace-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/ends-in-whitespace-escape.toml) Reserved escape sequence used (line 6 column 1 char 28)<br />[string/hex-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/hex-escape.toml) Reserved escape sequence used (line 3 column 1 char 35)<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/escape-esc.toml) Reserved escape sequence used (line 1 column 1 char 0)<br />[string/multiline-quotes.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/multiline-quotes.toml) Unterminated string found. Reached end of file. (line 27 column 1 char 664)<br />[float/zero.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/float/zero.toml) Weirdness with leading zeroes or underscores in your number. (line 4 column 1 char 47)<br />[array/mixed-int-string.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/array/mixed-int-string.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/nested-double.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/array/nested-double.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/string-with-comma-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/array/string-with-comma-2.toml) string index out of range<br />[array/mixed-int-float.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/array/mixed-int-float.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[array/mixed-string-table.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/array/mixed-string-table.toml) list index out of range<br />[array/mixed-int-array.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/array/mixed-int-array.toml) Not a homogeneous array (line 1 column 1 char 0)<br />[inline-table/multiline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/multiline.toml) Invalid inline table value encountered (line 1 column 1 char 0)<br />[inline-table/key-dotted-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/key-dotted-1.toml) Parsed as unexpected data.<br />[inline-table/key-dotted-5.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/key-dotted-5.toml) Not a homogeneous array (line 2 column 1 char 20)<br />[inline-table/newline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/newline.toml) Key name found without value. Reached end of line. (line 5 column 2 char 98)<br />*157/187 (83.96%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|[datetime/no-seconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/no-seconds.toml) Expected newline or end of document after a statement (at line 2, column 23)<br />[key/unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/unicode.toml) Invalid statement (at line 3, column 1)<br />[string/hex-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/hex-escape.toml) Unescaped '\' in a string (at line 3, column 22)<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/escape-esc.toml) Unescaped '\' in a string (at line 1, column 10)<br />[inline-table/newline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/newline.toml) Invalid initial character for a key part (at line 3, column 21)<br />*182/187 (97.33%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|[datetime/no-seconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/no-seconds.toml) Invalid number at line 2 col 25<br />[key/unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/unicode.toml) Empty key at line 3 col 0<br />[string/hex-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/hex-escape.toml) Invalid character 'x' in string at line 3 col 20<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/escape-esc.toml) Invalid character 'e' in string at line 1 col 8<br />[inline-table/newline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/newline.toml) Empty key at line 3 col 20<br />*182/187 (97.33%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|[spec/table-9.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/spec/table-9.toml) duplicate key: `apple` for key `fruit` at line 8 column 1<br />[datetime/no-seconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/no-seconds.toml) expected a colon, found a newline at line 2 column 26<br />[key/unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/unicode.toml) unexpected character found: `\u{20ac}` at line 3 column 1<br />[table/array-within-dotted.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/table/array-within-dotted.toml) duplicate key: `apple` for key `fruit` at line 4 column 1<br />[string/hex-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/hex-escape.toml) invalid escape character in string: `x` at line 3 column 21<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/escape-esc.toml) invalid escape character in string: `e` at line 1 column 9<br />[inline-table/newline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/newline.toml) expected a table key, found a newline at line 3 column 21<br />*180/187 (96.26%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|[spec/string-4.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/spec/string-4.toml) Didn't find expected newline (line 7, column 62)<br />[spec/string-7.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/spec/string-7.toml) Didn't find expected newline (line 7, column 50)<br />[datetime/no-seconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/no-seconds.toml) can't parse type (line 2, column 20)<br />[datetime/milliseconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/milliseconds.toml) Didn't find expected newline (line 2, column 27)<br />[datetime/datetime.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/datetime.toml) Didn't find expected newline (line 4, column 18)<br />[comment/after-literal-no-ws.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/comment/after-literal-no-ws.toml) can't parse type (line 1, column 4)<br />[comment/tricky.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/comment/tricky.toml) can't parse type (line 11, column 7)<br />[key/unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/unicode.toml) '€' cannot begin key (line 3, column 0)<br />[string/raw-multiline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/raw-multiline.toml) Didn't find expected newline (line 22, column 3)<br />[string/hex-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/hex-escape.toml) \x not a valid escape (line 3, column 43)<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/escape-esc.toml) \e not a valid escape (line 1, column 33)<br />[string/multiline-quotes.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/multiline-quotes.toml) Didn't find expected newline (line 4, column 26)<br />[inline-table/newline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/newline.toml) ' ' cannot begin key (line 3, column 20)<br />*174/187 (93.05%) passed*|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|[datetime/no-seconds.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/datetime/no-seconds.toml) Expected newline or end of document after a statement (at line 2, column 23)<br />[key/unicode.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/key/unicode.toml) Invalid statement (at line 3, column 1)<br />[string/hex-escape.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/hex-escape.toml) Unescaped '\' in a string (at line 3, column 22)<br />[string/escape-esc.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/string/escape-esc.toml) Unescaped '\' in a string (at line 1, column 10)<br />[inline-table/newline.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//valid/inline-table/newline.toml) Invalid initial character for a key part (at line 3, column 21)<br />*182/187 (97.33%) passed*|

### Compliance with invalid tests in toml-test

Test the compliance with the standard test suites for invalid toml files
here:

> https://github.com/BurntSushi/toml-test/

- `Not OK`: The toml file is parsed without error, but expected to fail.
- `OK`: All files are failed to parse, as expected. Showing the last
parsing error.


| |Result (toml-test v1.5.0)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Not OK: [integer/double-sign-plus.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/double-sign-plus.toml) incorrectly parsed.<br />Not OK: [integer/us-after-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/us-after-bin.toml) incorrectly parsed.<br />Not OK: [integer/double-sign-nex.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/double-sign-nex.toml) incorrectly parsed.<br />Not OK: [integer/us-after-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/us-after-hex.toml) incorrectly parsed.<br />Not OK: [integer/us-after-oct.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/us-after-oct.toml) incorrectly parsed.<br />Not OK: [spec/inline-table-2-0.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/spec/inline-table-2-0.toml) incorrectly parsed.<br />Not OK: [datetime/offset-overflow-minute.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/datetime/offset-overflow-minute.toml) incorrectly parsed.<br />Not OK: [datetime/offset-overflow-hour.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/datetime/offset-overflow-hour.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/string-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/string-del.toml) incorrectly parsed.<br />Not OK: *63 more items incorrectly parsed.*<br />*298/371 (80.32%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|OK: [inline-table/linebreak-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/inline-table/linebreak-1.toml) Unclosed inline table (at line 3, column 18)<br /> *371/371 (100%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/multi-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/multi-cr.toml) incorrectly parsed.<br />Not OK: [control/rawmulti-cd.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/rawmulti-cd.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/table/append-with-dotted-keys-1.toml) incorrectly parsed.<br />Not OK: [table/overwrite-array-in-parent.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/table/overwrite-array-in-parent.toml) incorrectly parsed.<br />Not OK: [table/append-to-array-with-dotted-keys.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/table/append-to-array-with-dotted-keys.toml) incorrectly parsed.<br />Not OK: [table/append-with-dotted-keys-2.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/table/append-with-dotted-keys-2.toml) incorrectly parsed.<br />Not OK: [array/extend-defined-aot.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/array/extend-defined-aot.toml) incorrectly parsed.<br />Not OK: [inline-table/overwrite-09.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/inline-table/overwrite-09.toml) incorrectly parsed.<br />*361/371 (97.30%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Not OK: [integer/positive-hex.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/positive-hex.toml) incorrectly parsed.<br />Not OK: [integer/positive-bin.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/positive-bin.toml) incorrectly parsed.<br />Not OK: [integer/positive-oct.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/integer/positive-oct.toml) incorrectly parsed.<br />Not OK: [datetime/offset-overflow-minute.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/datetime/offset-overflow-minute.toml) incorrectly parsed.<br />Not OK: [datetime/offset-overflow-hour.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/datetime/offset-overflow-hour.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/multi-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/multi-cr.toml) incorrectly parsed.<br />Not OK: [control/rawmulti-cd.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/rawmulti-cd.toml) incorrectly parsed.<br />Not OK: [control/bare-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/bare-cr.toml) incorrectly parsed.<br />*361/371 (97.30%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Not OK: [spec/inline-table-2-0.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/spec/inline-table-2-0.toml) incorrectly parsed.<br />Not OK: [spec/table-9-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/spec/table-9-1.toml) incorrectly parsed.<br />Not OK: [spec/table-9-0.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/spec/table-9-0.toml) incorrectly parsed.<br />Not OK: [datetime/offset-overflow-minute.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/datetime/offset-overflow-minute.toml) incorrectly parsed.<br />Not OK: [control/comment-del.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-del.toml) incorrectly parsed.<br />Not OK: [control/comment-lf.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-lf.toml) incorrectly parsed.<br />Not OK: [control/comment-null.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-null.toml) incorrectly parsed.<br />Not OK: [control/comment-ff.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-ff.toml) incorrectly parsed.<br />Not OK: [control/comment-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/comment-cr.toml) incorrectly parsed.<br />Not OK: [control/multi-cr.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/control/multi-cr.toml) incorrectly parsed.<br />Not OK: *14 more items incorrectly parsed.*<br />*347/371 (93.53%) passed*|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|OK: [inline-table/linebreak-1.toml](https://github.com/BurntSushi/toml-test/blob/v1.5.0/tests//invalid/inline-table/linebreak-1.toml) Unclosed inline table (at line 3, column 18)<br /> *371/371 (100%) passed*|

### Compliance with valid tests in python tomllib test data

Test the compliance with python tomllib test data (since python 3.11)
for valid toml files here:

> https://github.com/python/cpython/tree/3.11/Lib/test/test_tomllib/data/valid

The tests come up with a JSON counterpart that can be used to valid whether
loading the toml file yields the same result as the JSON counterpart.


| |Result (cpython tag 3.12.4)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|[apostrophes-in-literal-string.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/apostrophes-in-literal-string.toml) Unbalanced quotes (line 1 column 50 char 49)<br />[five-quotes.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/five-quotes.toml) Unterminated string found. Reached end of file. (line 7 column 1 char 97)<br />[dates-and-times/datetimes.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/dates-and-times/datetimes.toml) Parsed as unexpected data.<br />[multiline-basic-str/ends-in-whitespace-escape.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/multiline-basic-str/ends-in-whitespace-escape.toml) Reserved escape sequence used (line 6 column 1 char 28)<br />*8/12 (66.67%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|OK, *12/12 (100%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|[apostrophes-in-literal-string.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/apostrophes-in-literal-string.toml) Didn't find expected newline (line 3, column 3)<br />[five-quotes.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/five-quotes.toml) Didn't find expected newline (line 3, column 3)<br />[dates-and-times/datetimes.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//valid/dates-and-times/datetimes.toml) Didn't find expected newline (line 1, column 19)<br />*9/12 (75.00%) passed*|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|OK, *12/12 (100%) passed*|

### Compliance with invalid tests in python tomllib test data

Test the compliance with python tomllib test data (since python 3.11)
for invalid toml files here:

> https://github.com/python/cpython/tree/main/Lib/test/test_tomllib/data/invalid

- `Not OK`: The toml file is parsed without error, but expected to fail.
- `OK`: All files are failed to parse, as expected. Showing the last
parsing error.


| |Result (cpython tag 3.12.4)|
|-|-----------------------|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Not OK: [invalid-comment-char.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/invalid-comment-char.toml) incorrectly parsed.<br />Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table-with-subtable.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table-with-subtable.toml) incorrectly parsed.<br />Not OK: [array/unclosed-empty.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/array/unclosed-empty.toml) incorrectly parsed.<br />Not OK: [array/file-end-after-val.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/array/file-end-after-val.toml) incorrectly parsed.<br />Not OK: [array/unclosed-after-item.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/array/unclosed-after-item.toml) incorrectly parsed.<br />Not OK: [inline-table/overwrite-value-in-inner-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/overwrite-value-in-inner-table.toml) incorrectly parsed.<br />Not OK: [inline-table/unclosed-empty.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/unclosed-empty.toml) incorrectly parsed.<br />*41/50 (82.00%) passed*|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|OK: [inline-table/overwrite-implicitly.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/overwrite-implicitly.toml) Cannot overwrite a value (at line 1, column 21)<br /> *50/50 (100%) passed*|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|Not OK: [array-of-tables/overwrite-array-in-parent.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/array-of-tables/overwrite-array-in-parent.toml) incorrectly parsed.<br />Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-aot.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-aot.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table-with-subtable.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table-with-subtable.toml) incorrectly parsed.<br />Not OK: [inline-table/override-val-in-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/override-val-in-table.toml) incorrectly parsed.<br />*44/50 (88.00%) passed*|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />*49/50 (98.00%) passed*|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|Not OK: [non-scalar-escaped.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/non-scalar-escaped.toml) incorrectly parsed.<br />Not OK: [invalid-comment-char.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/invalid-comment-char.toml) incorrectly parsed.<br />Not OK: [table/redefine-2.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/table/redefine-2.toml) incorrectly parsed.<br />Not OK: [table/redefine-1.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/table/redefine-1.toml) incorrectly parsed.<br />Not OK: [multiline-basic-str/carriage-return.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/multiline-basic-str/carriage-return.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table.toml) incorrectly parsed.<br />Not OK: [dotted-keys/extend-defined-table-with-subtable.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/dotted-keys/extend-defined-table-with-subtable.toml) incorrectly parsed.<br />Not OK: [inline-table/overwrite-value-in-inner-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/overwrite-value-in-inner-table.toml) incorrectly parsed.<br />Not OK: [inline-table/override-val-with-table.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/override-val-with-table.toml) incorrectly parsed.<br />*41/50 (82.00%) passed*|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|OK: [inline-table/overwrite-implicitly.toml](https://github.com/python/cpython/tree/v3.12.4/Lib/test/test_tomllib/data//invalid/inline-table/overwrite-implicitly.toml) Cannot overwrite a value (at line 1, column 21)<br /> *50/50 (100%) passed*|

### Running speed with data provided by `rtoml`

Test the speed of loading and dumping the loaded using data
provided by `rtoml`

> https://github.com/samuelcolvin/rtoml/raw/main/tests/data.toml


| |Loading speed|Dumping speed|
|-|-|-|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Excluded (heterogeneous arrays not supported)|Excluded (heterogeneous arrays not supported)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|2.14s (5000 iterations)|0.73s (5000 iterations)|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|39.78s (5000 iterations)|0.98s (5000 iterations)|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|0.37s (5000 iterations)|0.08s (5000 iterations)|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|4.99s (5000 iterations)|1.87s (5000 iterations)|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|2.04s (5000 iterations)|Dumping not supported|

### Running speed with data provided by `tomli`

Test the speed of loading and dumping the loaded using data
provided by `tomli`

> https://github.com/hukkin/tomli/raw/master/benchmark/data.toml


| |Loading speed|Dumping speed|
|-|-|-|
|<a target="_blank" href="https://github.com/uiri/toml">toml</a>|Excluded (heterogeneous arrays not supported)|Excluded (heterogeneous arrays not supported)|
|<a target="_blank" href="https://github.com/hukkin/tomli">tomli/tomli_w</a>|1.41s (5000 iterations)|0.46s (5000 iterations)|
|<a target="_blank" href="https://github.com/sdispater/tomlkit">tomlkit</a>|24.55s (5000 iterations)|0.51s (5000 iterations)|
|<a target="_blank" href="https://github.com/samuelcolvin/rtoml">rtoml</a>|0.32s (5000 iterations)|0.16s (5000 iterations)|
|<a target="_blank" href="https://github.com/alethiophile/qtoml">qtoml</a>|3.63s (5000 iterations)|1.25s (5000 iterations)|
|<a target="_blank" href="https://docs.python.org/3/library/tomllib.html">tomllib</a>|1.44s (5000 iterations)|Dumping not supported|



## Other reports

- [Tests with `toml-test` v1.4.0](./reports/with_toml-test_v1.4.0.md)
- [Tests with `toml-test` v1.3.0](./reports/with_toml-test_v1.3.0.md)
- [Tests with `toml-test` v1.2.0](./reports/with_toml-test_v1.2.0.md)

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
toml-bench --iter 5000
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

[1]: https://img.shields.io/librariesio/release/pypi/toml-bench?style=flat-square
[2]: https://libraries.io/github/pwwang/toml-bench#repository_dependencies
