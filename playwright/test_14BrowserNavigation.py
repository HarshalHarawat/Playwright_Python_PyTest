import time

from playwright.sync_api import Page


def test_browserNavigate(page:Page):

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)
    page.go_back()
    time.sleep(2)
    page.go_forward()
    time.sleep(2)
    page.reload()