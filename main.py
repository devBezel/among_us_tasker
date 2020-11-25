import keyboard
import pyautogui
import time

from utilities.read_task import ReadTask

START_FREEZE_SECONDS = 2


def main():

    print(f"Amongtasker.. Poczekaj {START_FREEZE_SECONDS} sekund na wlączenie zadań")
    time.sleep(START_FREEZE_SECONDS)


    while True:
        time.sleep(0.5)
        ReadTask().resolve_read_task()


if __name__ == "__main__":
    main()