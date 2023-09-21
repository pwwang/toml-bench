# toml-bench

[![deps][1]][2]

Which toml package to use in python?

See also: [toml-lang](https://toml.io/en/) and [PEP 680](https://www.python.org/dev/peps/pep-0680/)

{{latest-report}}

## Other reports

- [Tests with `toml-test` v1.2.0](./reports/with_toml-test_v1.2.0.md)
- [Tests with `toml-test` v1.1.0](./reports/with_toml-test_v1.1.0.md)
- [Tests with `toml-test` v1.0.0](./reports/with_toml-test_v1.0.0.md)
- [Tests with python 3.11 (`tomllib` included)](./reports/with_python3.11.md)

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
