#!/bin/bash

cd "$(dirname "$0")/backend" || exit 1

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

echo "Done! Now select the interpreter in VSCode: .venv/bin/python"