from regex import P
import tomlkit
from ..api import API


class TOMLKitAPI(API):
    package = tomlkit
    repo = "https://github.com/sdispater/tomlkit"

    def load(self, f):
        content = f.read()
        return tomlkit.loads(content)
