import time

from playwright.sync_api import Page, expect, Playwright


def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False) #like double-clicking Chrome.
    context = browser.new_context()                      #like a fresh user (no history, no cookies).
    page = context.new_page()                            #like opening a new tab.
    page.goto("https://rahulshettyacademy.com/")         #type the website address and press Enter.

def test_pw_shortcut(page:Page):                         #Default runs on Chrome browser
    page.goto("https://rahulshettyacademy.com/")

def test_locatorsPW(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("Harshaljain830@gmail.com")
    page.get_by_label("Password:").fill("Harshal1!")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefox_browser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/locatorspractice/")
    page.locator("#inputUsername").fill("Harshaljain830@gmail.com")
    page.get_by_placeholder("Password").fill("Haghjkl")
    page.locator("#chkboxTwo").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("* Incorrect username or password")).to_be_visible()