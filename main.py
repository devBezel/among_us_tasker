import pyautogui
import time
import keyboard


from tasks.cables import Cables
from utilities.read_tasks import ReadTasks

SCREEN_RESOLUTION = pyautogui.size()
START_FREEZE_SECONDS = 2


def main():
    print(f"Amongtasker.. Poczekaj {START_FREEZE_SECONDS} sekund na wlączenie zadań")
    time.sleep(START_FREEZE_SECONDS)

    # read_tasks = ReadTasks()
    # read_tasks.task_to_json()
    while True:
    	if(keyboard.is_pressed("1")):
    		cable_task = Cables(SCREEN_RESOLUTION)
    		cable_task.run()
    	elif(keyboard.is_pressed("esc")):
    		break
    		

if __name__ == "__main__":
    main()