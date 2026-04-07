$ErrorActionPreference = 'Stop'

if (Get-Command py -ErrorAction SilentlyContinue) {
    $python = 'py -3'
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $python = 'python'
} else {
    Write-Error 'Python is not installed. Please install Python 3.x first.'
    exit 1
}

& $python -m pip install --upgrade pip
& $python -m pip install pyinstaller
& $python -m pyinstaller --onefile --windowed --name YoutubeLooper main.py

Write-Host 'Build complete. Output binary is in the dist folder.'
