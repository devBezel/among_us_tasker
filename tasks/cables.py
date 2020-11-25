import pyautogui
import time
import datetime

from entities.cable import Cable

class Cables:

    START_TASK_POS = [584, 270]
    START_RESOLVE_TASK_POS = [1300, 270]
    CABLE_COUNT = 4

    def resolve_task(self):
        right_cables = self.get_cable_color_and_position(self.START_TASK_POS[0] - 20, self.START_TASK_POS[1])
        left_cables = self.get_cable_color_and_position(self.START_RESOLVE_TASK_POS[0] + 20, self.START_RESOLVE_TASK_POS[1])
        for x in right_cables:
            for y in left_cables:
                if(x.get_colour() == y.get_colour()):
                    self.drag_cable(x.get_position(), y.get_position())

        return True

    def drag_cable(self, start_pos, end_pos):

        pyautogui.moveTo(start_pos[0], start_pos[1])
        pyautogui.mouseDown(button="left")
        
        pyautogui.moveTo(end_pos[0], end_pos[1])
        pyautogui.click()

    def get_cable_color_and_position(self, start_pos, end_pos):
        cables_data = []

        for x in range(self.CABLE_COUNT):
            pyautogui.moveTo(start_pos, end_pos)
            cables_data.append(Cable(pyautogui.pixel(start_pos, end_pos), [start_pos, end_pos]))
            end_pos += 187

        return cables_data

    def log(self):
        time = datetime.datetime.now()
        print(f"[{time.hour}:{time.minute}][ZADANIE] Rozwiązauje kabelki")

    def run(self):
        return self.resolve_task()
