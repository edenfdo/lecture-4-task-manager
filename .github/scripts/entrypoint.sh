#!/bin/bash
set -euo pipefail

cd /workspace

python3 .github/scripts/todo.py | tee /tmp/tasks.txt
python3 .github/scripts/todo-test.py 2>&1 | tee /tmp/tests.txt

bash .github/scripts/update_index.sh /tmp/tasks.txt /tmp/tests.txt