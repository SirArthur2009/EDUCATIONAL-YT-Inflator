# YouTube Looper

A simple Python-based YouTube view bot that automates viewing videos by opening them in Google Chrome and simulating key presses to play and pause the video. This tool allows users to specify a YouTube URL and the number of views to generate.

## Features

- **Graphical User Interface (GUI)**: Easy-to-use Tkinter-based interface for inputting the YouTube URL, desired number of views, and whether the video starts paused.
- **URL Persistence**: Automatically saves and loads the last used URL for convenience.
- **Randomized Viewing Time**: Simulates realistic viewing by waiting a random duration (based on a normal distribution) before closing the video.
- **Chrome Integration**: Opens videos in a specified Chrome browser instance.

## Requirements

- Python 3.x
- Google Chrome installed at `C:\Program Files\Google\Chrome\Application\chrome.exe` (or update the path in `main.py` if different)
- Required Python packages:
  - `pyautogui`
  - `tkinter` (usually included with Python)

## Installation

1. Clone or download this repository.
2. Install the required Python packages:
   ```
   pip install pyautogui
   ```
3. Ensure Google Chrome is installed and the path in `main.py` is correct.

## Usage

1. Run the script:
   ```
   python main.py
   ```
2. In the GUI:
   - Enter the YouTube video URL.
   - Specify the number of views you want to generate.
   - Check the box if the video starts paused.
3. Click "Submit" to start the automation.

The bot will open the video in Chrome, play it for a random duration, and then close the tab, repeating the process for the specified number of views.

## Disclaimer

Using bots to artificially inflate views may violate YouTube's terms of service and could lead to penalties on your account, including suspension or termination. To avoid detection, consider using an unsigned Chrome profile and a VPN to change your IP address. Use this tool responsibly and at your own risk. The authors are not responsible for any consequences arising from its use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project is for educational purposes only. Please check YouTube's terms of service before use. 
