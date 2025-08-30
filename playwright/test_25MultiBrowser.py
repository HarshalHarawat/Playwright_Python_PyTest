import pytest
from playwright.sync_api import Playwright

# MultiBrowser this fixture present in conftest file

def test_MultiBrowserLogin(MultiBrowser):

    page = MultiBrowser
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")

    assert page.locator("#username").input_value() == "rahulshettyacademy"
