# YouTube Looper

A simple cross-platform Python YouTube view automation tool. It uses a Tkinter GUI for input, remembers your last-used URL, and opens videos in a browser while using PyAutoGUI to control playback.

## Features

- **Cross-platform support**: Works on Windows, macOS, and Linux.
- **Graphical interface**: Tkinter GUI for URL, view count, and paused-state input.
- **URL persistence**: Saves the last entered URL in a user-specific configuration folder.
- **Browser detection**: Automatically finds Chrome, Chromium, Edge, Brave, or Safari where available.
- **Randomized view time**: Simulates viewing duration with a randomized delay.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `pyautogui`

### Linux prerequisites

On many Linux systems, install the GUI dependencies before `pyautogui`:

```bash
sudo apt install python3-tk python3-dev python3-xlib scrot
```

### macOS prerequisites

If you have installation issues, install these packages:

```bash
pip install pyobjc-core pyobjc
```

## Installation

1. Clone or download this repository.
2. Install runtime dependencies:

```bash
pip install -r requirements.txt
```

If you want to build a standalone executable, install the development dependency:

```bash
pip install -r requirements-dev.txt
```

## Helper scripts

On macOS/Linux:

```bash
./install.sh
./build.sh
```

On Windows PowerShell:

```powershell
.\build.ps1
```

## Usage

Run the script:

```bash
python main.py
```

In the GUI:

- Enter the YouTube video URL.
- Enter the number of views to generate.
- Check the box if the video starts paused.
- Click **Submit**.

The bot will open the video in a detected browser, play it, wait a randomized amount of time, pause it, and close the tab.

## Notes

- On Windows, the script stores settings in `%LOCALAPPDATA%\YouTube Looper\last_url.txt`.
- On macOS, it stores settings in `~/Library/Application Support/YouTube Looper/last_url.txt`.
- On Linux, it stores settings in `~/.youtube_looper/last_url.txt`.

## Disclaimer

Using bots to artificially inflate views may violate YouTube's terms of service and could lead to penalties. Use this tool responsibly and at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
