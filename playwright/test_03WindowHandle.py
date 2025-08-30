from playwright.sync_api import Playwright, expect


def test_windowhandle(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    with page.expect_popup() as pageinfo:
        page.locator(".blinkingText").click()

        childwindow = pageinfo.value
        print(childwindow.title())
        textwrap = childwindow.locator(".red").text_content()
        #Please email us at  mentor@rahulshettyacademy.com with below template to receive response

        word =textwrap.split("at ")
        myemail = word[1].split(" ")[0]
        assert myemail == "mentor@rahulshettyacademy.com"