from configparser import ConfigParser


class Config:

	CONFIG_PATH = "config.ini"

	def __init__(self, section, text):
		self.section = section
		self.text = text


	def get(self):
		config = ConfigParser()
		config.read(self.CONFIG_PATH)

		return config[self.section][self.text]
