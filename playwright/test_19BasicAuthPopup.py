#https://the-internet.herokuapp.com/basic_auth
import logging

from playwright.sync_api import Page, Playwright


def test_basicAuth(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context(
        http_credentials = {"username":"admin","password":"admin"})

    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")

    page.locator("#username").set_input_files(path="mypath.com")

    slider = page.locator("#slider")

    bound = slider.bounding_box()
    start_x=bound["x"]+bound["width"]/2
    start_y = bound["7"] + bound["height"] / 2

    page.mouse.move(start_x,start_y)
    page.mouse.down()
    page.mouse.move(start_x+400,start_y+400)
    page.mouse.up()


