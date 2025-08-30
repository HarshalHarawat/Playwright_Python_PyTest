import os
from configparser import ConfigParser


def readConfig(section,key):
    config = ConfigParser()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # used to get the absolute path
    config_path = os.path.join(BASE_DIR, "..", "Utilities", "config.ini")

    config.read(config_path)
    return config.get(section,key)

#ConfigParser
#get the path
#read
#get
