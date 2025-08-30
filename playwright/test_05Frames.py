from playwright.sync_api import Page


def test_FrameHanding(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    child_frame = page.frame_locator("#courses-iframe")
    child_frame.get_by_role("button",name = "JOIN NOW")

    page.locator("#name").fill("Harshal")