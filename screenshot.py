import time
import pyautogui

def screenshot():
    #give some time before taking the screenshot
    time.sleep(5)
    img = pyautogui.screenshot('test.png')
    img.show()