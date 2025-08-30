from playwright.sync_api import Page


def test_SingleUpload(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#singleFileInput").set_input_files("/Users/harshal/Desktop/Python!/PW.pages")


def test_MultipleUpload(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    (page.locator("#multipleFilesInput").set_input_files
        ( ["/Users/harshal/Desktop/Python!/PW.pages",
         "/Users/harshal/Desktop/Python!/Python!.docx"]))