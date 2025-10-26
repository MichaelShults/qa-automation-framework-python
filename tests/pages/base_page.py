
from playwright.sync_api import Page, Locator, expect
import logging


class BasePage:
    def __init__(self, page: Page):
        logging.info("Initializing BasePage.")
        self.page = page
    
    def click_element(self, locator: Locator):
        logging.info(f"Clicking element {locator}")
        locator.click()
    
    def is_text_visible(self, element_selector: str, element_text:str):
        logging.info(f"Checking if element visible: '{element_selector}' with text '{element_text}'")
        locator = self.page.locator(selector=element_selector, has_text=element_text)
        locator_count = locator.count()
        logging.info(f"Counted {locator_count} match{'es' if (locator_count > 1 or locator_count == 0) else ""}.")
        return locator_count > 0
            