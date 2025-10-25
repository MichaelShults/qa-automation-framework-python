import pytest
from playwright.sync_api import sync_playwright, Browser

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
        page = context.new_page()
        page.goto("localhost:5000")
        yield page
        page.close()