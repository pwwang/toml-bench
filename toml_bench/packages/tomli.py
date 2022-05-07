import importlib_metadata as im
import tomli
import tomli_w
from ..api import API


class TOMLiAPI(API):
    package = tomli_w
    repo = "https://github.com/hukkin/tomli"
    loads = lambda self, data: tomli.loads(data)
    load = lambda self, f: tomli.load(f)

    def version(self) -> str:
        return (
            f"{im.version('tomli')}, "
            f"tomli_w: {im.version(self.package.__name__)}"
        )
