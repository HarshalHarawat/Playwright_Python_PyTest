# Alert :- Confirm Alert, Dismiss Alert, Prompt Alert
from playwright.sync_api import Playwright, expect, Page


def test_alerthandling(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Confirm
    page.locator("input[value='Confirm']").click()
    page.on("dialog", lambda d:d.Confirm())

def test_alert(page:Page):
    page.goto("https://demoqa.com/alerts")

    #accept
    page.locator("#alertButton").click()
    page.on("dialog", lambda d:d.accept())

    #accept
    page.locator("#timerAlertButton").click()
    page.on("dialog", lambda d: d.accept())

    #dismiss
    page.get_by_role("button",name="Click me").nth(3).click()
    page.on("dialog", lambda d:d.dismiss())

    #prompt
    page.locator("#promtButton").click()
    page.on("dialog",lambda d:d.accept("Harshal"))
