import allure
from playwright.sync_api import Page
import allure_pytest

@allure.feature("Login Page")
@allure.severity(allure.severity_level.MINOR)
def test_AllureReport_Generation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with allure.step("Login page username and password"):
        page.locator("#username").fill("rahulshettyacademy")
        page.locator("#password").fill("#learning")