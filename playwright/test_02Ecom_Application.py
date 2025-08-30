from playwright.sync_api import Playwright, expect


def test_application_UIValidation(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()

    #
    iphone_prod = page.locator("app-card").filter(has_text="Blackberry")
    iphone_prod.get_by_role("button").click()
    page.get_by_text("Checkout").click()

    expect(page.locator(".col-sm-8.col-md-6")).to_have_count(1)
    page.get_by_text("₹. 50000")