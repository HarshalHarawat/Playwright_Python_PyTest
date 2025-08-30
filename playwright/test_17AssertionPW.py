from playwright.sync_api import Page, expect


def test_assertionsPw(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    print(page.locator("//input[@id='male']").is_enabled())
    print(page.locator("#monday").is_checked())

    print(page.title())
    expect(page.get_by_text("Name:")).to_have_text("Name:")
    expect(page).to_have_title("Automation Testing Practice")
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")
    expect(page.locator("#Wikipedia1_wikipedia-search-input")).to_have_id("Wikipedia1_wikipedia-search-input")