from playwright.sync_api import Page, expect


def test_windowhandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    with page.expect_popup() as pageinfo:
        page.locator(".blinkingText").first.click()

    childwindow = pageinfo.value
    print(childwindow.title())
    textwrap = childwindow.locator(".red").text_content()
    # Please email us at mentor@rahulshettyacademy.com with below template to receive response

    if textwrap and "at " in textwrap:
        word = textwrap.split("at ")
        if len(word) > 1:
            myemail = word[1].split(" ")[0]
            assert myemail == "mentor@rahulshettyacademy.com"