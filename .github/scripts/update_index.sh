#!/bin/bash
set -euo pipefail

python3 - "$1" "$2" <<'PY'
import html
import re
import sys
from pathlib import Path

task_output = Path(sys.argv[1]).read_text()
test_output = Path(sys.argv[2]).read_text()

todo = task_output.split("ToDo Tasks:\n", 1)[1].split(
    "Done Tasks:\n", 1
)[0].strip()

done = task_output.split("Done Tasks:\n", 1)[1].strip()

page_path = Path("index.html")
page = page_path.read_text()

for section, content in [
    ("todo", todo),
    ("done", done),
    ("tests", test_output.strip()),
]:
    pattern = rf'(<pre id="{section}">).*?(</pre>)'
    page, replacements = re.subn(
        pattern,
        lambda match: (
            match.group(1)
            + html.escape(content)
            + match.group(2)
        ),
        page,
        flags=re.DOTALL,
    )

    if replacements != 1:
        raise SystemExit(f"Expected one HTML section: {section}")

page_path.write_text(page)
print("HTML report updated.")
PY