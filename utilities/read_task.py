
import pyautogui

from tasks.cables import Cables
from tasks.swipe_card import SwipeCard
from tasks.unlock_reactor import UnlockReactor
from utilities.config import get_config

class ReadTask:
	def __init__(self):
		self.resolution = pyautogui.size()
		self.task_performance = False

	def resolve_read_task(self):
		colour = self.check_colour()

		if(self.task_performance is False):
			print("wykonuje sie")
			if(colour == eval(get_config("task", "cables"))):
				cables = Cables()

				self.task_performance = cables.run()
				cables.log()
			elif(colour == eval(get_config("task", "reactor"))):
				reactor = UnlockReactor()

				self.task_performance = reactor.run()
				reactor.log()
			elif(colour == eval(get_config("task", "swipe_card"))):
				swipe_card = SwipeCard()

				self.task_performance = swipe_card.run()
				swipe_card.log()

		self.task_performance = False

	def check_colour(self):
		pixel_color = pyautogui.pixel(int(self.resolution[0]/2), int(self.resolution[1]/2))
		print(pixel_color)
		return pixel_color