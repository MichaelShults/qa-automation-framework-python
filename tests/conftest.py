import pytest
from playwright.sync_api import sync_playwright, Browser
import logging

MAIN_URL = "localhost:5000"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        logging.info("Creating browser")
        browser = pw.chromium.launch(headless=False)
        yield browser
        logging.info("Closing browser")
        browser.close()

@pytest.fixture
def context(browser: Browser):
    logging.info("Creating context")
    context = browser.new_context()
    yield context
    logging.info("Closing context")
    context.close()

@pytest.fixture
def page(context):
        logging.info(f"Creating page")
        page = context.new_page()
        logging.info(f"Navigating to '{MAIN_URL}'")
        page.goto(MAIN_URL)
        yield page
        logging.info(f"Closing page")
        page.close()