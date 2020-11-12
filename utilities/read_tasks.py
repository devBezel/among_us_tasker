import pyautogui
import pytesseract

from PIL import Image
from utilities.config import Config

class ReadTasks:

	# def __init__(self):
	# 	self.grab_tasks()

	def grab_tasks(self):
		screen = pyautogui.screenshot(region=(0,100, 800, 300))
		screen.save(r"cache/tasks.png")

	def task_to_json(self):
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		image = Image.open(r"cache/tasks.png")
		text = pytesseract.image_to_string(image, lang="eng")
		print(text)

