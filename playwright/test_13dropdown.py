from playwright.sync_api import Playwright


def test_Playwrightpracticepage(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Syntax --> value - label - index
    #  <option value="japan">
    #     Japan
    #  </option>

    # Select by value
    # page.locator("#country").select_option(value="japan")

    # Select by label (visible text)
    # page.locator("#country").select_option(label="Japan")

    # Select by index
    # page.locator("#country").select_option(index=3)

    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")

    page.locator("select[name='country']").select_option("AD")

    page.locator("select[name='Month']").select_option(['March','May'])

    page.locator("select[name='Month']").select_option(value='Oct')

    page.locator("select[name='Month']").select_option(index=5,value='Oct',label='December')

    page.locator("select[name='Month']").select_option(['March', 'May'],label='December')