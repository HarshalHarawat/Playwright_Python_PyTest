import logging

import allure
import pytest
import requests
from playwright.sync_api import Playwright, Page, expect
from ConfigReader.readConfig import readConfig

def test_Basics(playwright:Playwright):
    browser_use = playwright.chromium.launch(headless=False)
    context= browser_use.new_context()
    page = context.new_page()

    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    print(page.locator(".navbar-logo.fg-text-dark.ffb-logo").inner_text())

    page.get_by_role("link",name="Home").nth(1).click()
    page.go_back()
    textwrap = page.get_by_text("Dummy ticket booking").inner_text()
    print(textwrap)

    content =page.get_by_text("Please complete the below form and follow instructions in order to make your Dummy ticket").text_content()
    print(content)
    section = page.locator("#opc-product-selection")

    radiobutton =section.locator("input[type='radio']").count()
    print(radiobutton)

    page.get_by_placeholder("first and middle name as on passport").fill("Harshal")

    page.locator("#travlastname").fill("Harawat")

    page.locator("//button[@id='place_order']/parent::div/parent::div/parent::div/parent::form/parent::div/child::div[2]/ul/li[1]").click()


def test_table(page:Page):

    page.goto("https://demoqa.com/browser-windows")

    with page.expect_popup() as pop_info:
        page.get_by_role("button",name="New Tab").click()
        child = pop_info.value

        intext = child.locator("#sampleHeading").inner_text()
        print(intext)

        assert intext , "This is a sample page"

def test_alert(page:Page):
    page.goto("https://demoqa.com/alerts")

    page.locator("#alertButton").click()
    page.on("dialog", lambda d:d.accept())

    page.locator("#timerAlertButton").click()
    page.on("dialog", lambda d: d.accept())

    page.get_by_role("button",name="Click me").nth(3).click()
    page.on("dialog", lambda d:d.dismiss())

    page.locator("#promtButton").click()
    page.on("dialog",lambda d:d.accept("Harshal"))


def test_frame(page:Page):

    page.goto("https://demoqa.com/frames")

    fr1 = page.frame_locator("#frame1")
    ins =fr1.locator("#sampleHeading").inner_text()
    print(ins)

    frame1 = page.frame_locator("iframe[name='goog_topics_frame']")
    frame2 = frame1.frame_locator("#google_esf")

def test_mousehover(page:Page):

    page.goto("https://demoqa.com/frames")

    page.locator("#id").hover()

@pytest.fixture(params=["chrome","firefox"])
def Multi_browser(playwright:Playwright,request):
    browser_use = request.param
    if browser_use== "chrome":
        return playwright.chromium.launch(headless=False)
    elif browser_use== "firefox":
        return playwright.firefox.launch(headless=False)
    else:
        raise ValueError("Invalid browser")


def test_MB(Multi_browser):

    page = Multi_browser

    context = page.new_context(
        http_credentials=({"username":"admin","password":"admin"})
    )
    page = context.new_page()
    page.goto("https://demoqa.com/frames")


def mydata():
    return [
        ("username1","pwd1"),
        ("username2","pwd2")
    ]

@allure.feature("Login using Multiple username and password")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize("username,password",mydata())
def test_parameterization(page:Page,username,password):
    page.goto("https://demoqa.com/frames")
    with allure.step(f"login{username},{password}"):
        page.locator("#username").fill(username)
        page.locator("#password").fill(password)
        page.locator("#username").set_input_files("")

def test_GenerateLogs():
    logging.basicConfig(
        filename="",
        format="",
        datefmt=""
    )

    return logging.getLogger()
logs = test_GenerateLogs()
logs.info("")
logs.debug(" ")
logs.fatal("")


def test_LogiPage(page:Page):

    page.goto(readConfig("basicInfo","url"))






