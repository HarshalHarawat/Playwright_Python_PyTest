import os.path

from ConfigReader.readConfig import  readConfig
from playwright.sync_api import Page


#config.ini file is present in Utilities directory

# move this file to ConfigReader.readConfig.py director check on left

# def readConfig(section,key):
#     config = ConfigParser()
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # used to get the absolute path
#     config_path = os.path.join(BASE_DIR, "..", "Utilities", "config.ini")
#
#     config.read(config_path)
#     return config.get(section,key)


def test_login_ConfigIni(page:Page):
    page.goto(readConfig("basicInfo", "url"))
    page.locator(readConfig("locator","username"))
    page.locator(readConfig("locator", "password"))


