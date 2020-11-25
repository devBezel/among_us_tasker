from configparser import ConfigParser

CONFIG_PATH = "config.ini"


def get_config(section, text):
    config = ConfigParser()
    config.read(CONFIG_PATH)

    return config[section][text]
