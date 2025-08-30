import time

from playwright.sync_api import Page


def test_keyboardActions(page:Page):

    #Types text
    page.goto("https://www.google.com/")
    page.locator("#APjFqb").type("Welcome to India")

    #Press
    page.keyboard.press("Enter")
    time.sleep(2)

    page.keyboard.down("Shift")