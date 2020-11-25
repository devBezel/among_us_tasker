import pyautogui
import time


class SwipeCard:
    def __init__(self):
        self.resolution = pyautogui.size()

    def resolve_task(self):
        try:
            hide_card_position = pyautogui.center(
                pyautogui.locateOnScreen(f"assets/tasks/swipe_card/main.png",
                                         confidence=0.7))
            pyautogui.click(hide_card_position[0], hide_card_position[1])

            time.sleep(1)
            card_position = pyautogui.center(
                pyautogui.locateOnScreen(f"assets/tasks/swipe_card/card.png",
                                         confidence=0.8))

            pyautogui.moveTo(card_position[0], card_position[1])
            pyautogui.mouseDown(button="left")

            mouse_pos_x = card_position[0]
            while (mouse_pos_x < 1450):
                pyautogui.moveTo(mouse_pos_x, card_position[1])
                mouse_pos_x += 60

            pyautogui.click()

            return True
        except Exception as e:
            print(e)

    def log(self):
        time = datetime.datetime.now()
		print(f"[{time.hour}:{time.minute}][ZADANIE] Rozwiązauje kartę w adminie")

    def run(self):
        return self.resolve_task()