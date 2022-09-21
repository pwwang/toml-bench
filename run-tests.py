"""Run tests and replace latest report"""
import os
from pathlib import Path

REPORTS = {
    "latest": "1.2.0",
    "v1.1.0": "1.1.0",
    "v1.0.0": "1.0.0",
}


def run_test(comver):
    print("Running with toml-test version:", comver)

    outfile = f"reports/with_toml-test_{comver}.md"

    cmd = f"python -m toml_bench --comver {REPORTS[comver]} --report {outfile}"
    os.system(cmd)


def render_readme():
    print("Rendering README file")
    report = []
    rptfile = Path(f"reports/with_toml-test_latest.md")
    outfile = Path("./README.md")
    rawfile = Path("./README.raw.md")

    with rptfile.open("r") as f:
        for line in f:
            if line.startswith("#"):
                line = f"#{line}"
            report.append(line)

    readme = rawfile.read_text().replace("{{latest-report}}", "".join(report))
    outfile.write_text(readme)


if __name__ == "__main__":
    # for key in REPORTS:
    #     run_test(key)

    render_readme()
