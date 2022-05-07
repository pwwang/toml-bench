from typing import Any
import importlib_metadata as im
import tomli
import tomli_w
from ..api import API
from ..cases.unicode import TestLoadUnicodeDummy


class TOMLiAPI(API):
    package = tomli_w
    repo = "https://github.com/hukkin/tomli"
    loads = lambda self, data: tomli.loads(data)
    load = lambda self, f: tomli.load(f)

    def version(self) -> str:
        return (
            f"{im.version('tomli')}; "
            f"**tomli_w**: {im.version(self.package.__name__)}"
        )


class TOMLiTestLoadUnicodeDummy(TestLoadUnicodeDummy):
    def result(self, out: Any) -> str:
        if isinstance(out, Exception):
            datafile = self.args.datadir / "unicode" / "unicode.toml"
            with open(datafile, "rb") as f:
                try:
                    loaded = self.api.load(f)
                except Exception as e:
                    loaded = e

            return (
                f"```{out.__class__.__name__}: {out} ```<br />"
                "**When load with:**<br />"
                "`with open(datafile, 'rb') as f:`<br />"
                "`　   loaded = self.api.load(f)`<br />"
                "**Raises:**<br />"
                f"`{loaded!r}`"
            )
        return super().result(out)
