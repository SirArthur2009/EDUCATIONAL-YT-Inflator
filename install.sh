#!/usr/bin/env bash
set -e

if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    echo "Python is not installed. Please install Python 3.x first." >&2
    exit 1
fi

$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt

echo "Installed runtime dependencies."

echo "If you want to build an executable, run './build.sh' or use 'pyinstaller'."
