import pyautogui
import datetime
import time
from utilities.config import get_config


class DownloadData:
    def __init__(self):
        self.resolution = pyautogui.size()

    def resolve_task(self):
        try:
            download_btn = pyautogui.center(
                pyautogui.locateOnScreen(
                    f"assets/tasks/download_data/main.png", confidence=0.7))
            pyautogui.click(download_btn[0], download_btn[1])
            time.sleep(int(get_config("task_sec_delay", "download_data")))

            return True
        except Exception as e:
            print(e)

    def log(self):
        time = datetime.datetime.now()
        print(
            f"[{time.hour}:{time.minute}][ZADANIE] Rozwiązauje pobieranie danych"
        )

    def run(self):
        self.resolve_task()
