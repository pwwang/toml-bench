from pathlib import Path
from importlib import import_module

for path in Path(__file__).parent.glob("*.py"):
    if path.name.startswith("_"):
        continue

    import_module(f".{path.stem}", package=__package__)
