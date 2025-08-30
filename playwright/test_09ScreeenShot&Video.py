from playwright.sync_api import Page, Playwright


def test_screenAndvideo(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #page.locator("").screenshot()   element level ss
    page.screenshot(path="screenshot.png", full_page=False)


def test_with_video(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/"
    )
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.screenshot(path="image.png", full_page=True)
