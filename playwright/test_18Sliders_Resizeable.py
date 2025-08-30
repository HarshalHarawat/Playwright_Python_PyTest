from playwright.sync_api import Page


def test_handlingSlider(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    slider = page.locator("#slider-range")

    bound = slider.bounding_box()

    start_x = bound["x"] + bound["width"]/2
    starty = bound["y"] + bound["height"]/2

    page.mouse.move(start_x,starty)
    page.mouse.down()
    page.mouse.move(start_x+400,starty)
    page.mouse.up()

def test_Resizeable(page:Page):
    page.goto("https://jqueryui.com/resizable/")

    frame = page.frame_locator(".demo-frame")
    resize = frame.locator("#resizable")
    resize_bond = resize.bounding_box()

    startx = resize_bond["x"] + resize_bond["width"]/2
    starty = resize_bond["y"] + resize_bond["height"]/2

    page.mouse.move(startx,starty)
    page.mouse.down()
    page.mouse.move(startx+400,starty+400)
    page.mouse.up()