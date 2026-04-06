import os
import time
import webbrowser
import pyautogui
import random
import getGUIinputs

def saveURL(url):
    try:
        with open("C:\\Program Files\\YouTube Looper\\last_url.txt", "w") as file:
            file.write(url)
    except FileNotFoundError:
        directory = "C:\\Program Files\\YouTube Looper"
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        print(f"Error saving URL: {e}")
def loadURL():
    try:
        with open("C:\\Program Files\\YouTube Looper\\last_url.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def main():
    print("\nWelcome to the YouTube view bot! ")

    open_url = loadURL()  # Load the last saved URL
    data = getGUIinputs.submit_gui(open_url)
    print(data)

    # Get new URL from GUI, using the last one as default
    open_url = data[0] #type: ignore

    # Get number of views from GUI
    viewsWanted = data[1]  #type: ignore

    # Get paused state from GUI
    startingPaused = data[2] #type: ignore

    saveURL(open_url)  # Save the current URL for future use

    # Path to Chrome executable
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update this path if Chrome is installed elsewhere

    # Register and use Chrome
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    views = 0
    print(viewsWanted)
    while views < int(viewsWanted):
        try:
            client = webbrowser.get("chrome")
            client.open(open_url)
            time.sleep(5)       #give it a couple seconds to load

            pyautogui.press("space")
            time.sleep(4)
            pyautogui.press("space")     #unpause the video
            
            if startingPaused:
                pyautogui.press('space')

            
            time.sleep(random.normalvariate(30, 10))      #wait for the video to finish

            pyautogui.press('space')
            #close the tab
            pyautogui.hotkey('ctrl', 'w')
            views += 1
        except webbrowser.Error as e:
            print(e)
            break

if __name__ == "__main__":
    main()
