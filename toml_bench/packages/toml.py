import toml

from ..api import API


class TOMLAPI(API):
    package = toml
    repo = "https://github.com/uiri/toml"
