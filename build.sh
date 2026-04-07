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
$PYTHON -m pip install pyinstaller
$PYTHON -m pyinstaller --onefile --windowed --name YoutubeLooper main.py

echo "Build complete. Output binary is in the 'dist' folder."
