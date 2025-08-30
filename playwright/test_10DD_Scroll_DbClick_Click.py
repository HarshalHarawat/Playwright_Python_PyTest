import time

from playwright.sync_api import Playwright


def test_playwright_ClickActions(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    #Double Click two-way
    page.dblclick("text=Double Click")
    time.sleep(2)
    page.locator("#field1").dblclick()

    #Righ Click
    page.locator("#textarea").click(button="right")

    #drag and drop
    page.drag_and_drop("#draggable","#droppable")

    #other way drag and drop
    src = page.locator("#draggable")
    trg = page.locator("#droppable")
    src.drag_to(trg)

    #scrolling two-ways
    page.mouse.wheel(0,6000)
    page.get_by_text("Footer Links").scroll_into_view_if_needed()
    time.sleep(3)




