from playwright.sync_api import Page


def test_xpath(page:Page):

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("//input[@id='autocomplete']").fill("Data")
    print(page.locator("//*[text()='Suggession Class Example']").inner_text())

    page.locator("//input[contains(@id,'Option1')]").click()
    page.locator("//label[@for='benz']/input[1]")

    page.locator("//input[@class='btn-style'][@id='confirmbtn']")

    page.locator("//button[text()='Home']/parent::a/parent::div/parent::header/following-sibling::div[2]/div/fieldset/child::buttonx")

