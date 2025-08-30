import pytest
from playwright.sync_api import Playwright, sync_playwright

# Fixture to launch Playwright itself
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright
        # Automatically closes when context ends


# Fixture for browser page
@pytest.fixture(scope="function")
def page(playwright_instance: Playwright):
    browser = playwright_instance.chromium.launch(headless=False)  # Use chromium, headless=False for visibility
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

# Multiple browser invokae
@pytest.fixture(params=["chrome", "firefox"])
def MultiBrowser(playwright: Playwright, request):
    browser_type = request.param

    if browser_type == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_type == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError("Wrong browser")

    page = browser.new_page()
    yield page   # ✅ return the page object to the test
    browser.close()  # ✅ teardown after test