import random
import time

from playwright.sync_api import Playwright, Page


def test_checkboxes(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    checkboxes = page.locator("input[type='checkbox']")
    checkbox = checkboxes.count()
    print(checkbox)

    for i in range(checkbox):
        checkboxes.nth(i).click()

def test_checkboxAssignment(page:Page):
    page.goto("http://www.tizag.com/htmlT/htmlcheckboxes.php")
    checkboxes =page.locator("(//div[@class='display'])[1]")
    checkbox = checkboxes.locator("input[name='sports']")
    chk = checkbox.count()

    for i in range(chk):
        checkbox.nth(i).click()

    area = page.locator("//div[@class='display']").nth(0)
    checkbox = area.locator("input[type='checkbox']")
    print(checkbox.count())
    value = page.locator("(//input[@value='soccer'])[1]").is_checked()
    print(value)