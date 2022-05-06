import tomli
import tomli_w
from ..api import API


class TOMLKitAPI(API):
    package = tomli_w
    repo = "https://github.com/hukkin/tomli"
    loads = lambda self, data: tomli.loads(data)
    load = lambda self, f: tomli.load(f)
