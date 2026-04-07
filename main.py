import os
import random
import shutil
import subprocess
import sys
import time
import webbrowser
from pathlib import Path
from typing import Optional

import pyautogui
import getGUIinputs


def get_data_dir() -> Path:
    if sys.platform == "win32":
        local_app = os.getenv("LOCALAPPDATA")
        if local_app:
            return Path(local_app) / "YouTube Looper"
        return Path.home() / "AppData" / "Local" / "YouTube Looper"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "YouTube Looper"
    return Path.home() / ".youtube_looper"


def get_last_url_file() -> Path:
    config_dir = get_data_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "last_url.txt"


def save_url(url: str) -> None:
    try:
        last_url_file = get_last_url_file()
        last_url_file.write_text(url, encoding="utf-8")
    except Exception as e:
        print(f"Error saving URL: {e}")


def load_url() -> str:
    try:
        last_url_file = get_last_url_file()
        return last_url_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error loading URL: {e}")
        return ""


def find_browser_command() -> Optional[str]:
    if sys.platform == "win32":
        candidates = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        ]
    elif sys.platform == "darwin":
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        ]
    else:
        candidates = [
            "google-chrome-stable",
            "google-chrome",
            "chromium-browser",
            "chromium",
            "chrome",
            "microsoft-edge",
            "brave-browser",
        ]

    for candidate in candidates:
        if os.path.isabs(candidate):
            if Path(candidate).exists():
                return candidate
        else:
            full_path = shutil.which(candidate)
            if full_path:
                return full_path

    return None


def open_in_browser(url: str) -> bool:
    browser_cmd = find_browser_command()
    if browser_cmd:
        try:
            subprocess.Popen([browser_cmd, url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except Exception as exc:
            print(f"Could not open URL with browser {browser_cmd!r}: {exc}")

    if sys.platform == "darwin":
        try:
            subprocess.Popen(["open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except Exception as exc:
            print(f"Could not open URL with default browser: {exc}")

    try:
        webbrowser.open(url, new=2)
        return True
    except Exception as exc:
        print(f"Could not open URL in the system browser: {exc}")
        return False


def close_tab_hotkey() -> None:
    if sys.platform == "darwin":
        pyautogui.hotkey("command", "w")
    else:
        pyautogui.hotkey("ctrl", "w")


def main() -> None:
    print("\nWelcome to the YouTube view bot!")

    open_url = load_url()
    data = getGUIinputs.submit_gui(open_url)
    if not data:
        return

    open_url = data[0]  # type: ignore
    views_wanted = max(1, int(float(data[1])))  # type: ignore
    starting_paused = data[2]  # type: ignore

    save_url(open_url)

    views = 0
    print(views_wanted)
    while views < views_wanted:
        if not open_in_browser(open_url):
            break

        time.sleep(5)
        pyautogui.press("space")
        time.sleep(4)

        if starting_paused:
            pyautogui.press("space")

        watch_time = max(15, min(60, random.normalvariate(30, 10)))
        time.sleep(watch_time)

        pyautogui.press("space")
        time.sleep(0.3)
        close_tab_hotkey()
        views += 1

if __name__ == "__main__":
    main()
