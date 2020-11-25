import pyautogui
import datetime


class UnlockReactor:
    def resolve_task(self):
        try:
            for num in range(1, 11):
                number_square = pyautogui.center(
                    pyautogui.locateOnScreen(f"assets/tasks/numbers/{num}.png",
                                             confidence=0.8))
                if (number_square is None):
                    continue
                pyautogui.click(number_square[0], number_square[1])

                return True
        except Exception as e:
            print(e)

    def log(self):
        time = datetime.datetime.now()
        print(f"[{time.hour}:{time.minute}][ZADANIE] Rozwiązauje reaktor")

    def run(self):
        return self.resolve_task()
