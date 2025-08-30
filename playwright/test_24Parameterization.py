import pytest
from playwright.sync_api import Page

def data():
    return [
        ("rahulshettyacademy","learning"),
        ("rahulshettyacademy", "learning"),
        ("rahulshettyacademy", "learning")
    ]


@pytest.mark.parametrize("username,password",data())
def test_parametrization_url(page:Page,username,password):

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.locator("#username").fill(username)
    page.locator("#password").fill(username)