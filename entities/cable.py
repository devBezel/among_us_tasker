class Cable:
	def __init__(self, colour_rgb, position):
		self.colour_rgb = colour_rgb
		self.position = position

	def get_position(self):
		return self.position

	def get_colour(self):
		return self.colour_rgb 