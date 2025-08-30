from playwright.sync_api import Page, expect


def test_mousehover(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()

def test_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_role("button",name='Point Me').hover()
    expect(page.get_by_role("link",name="Mobiles")).to_be_visible()