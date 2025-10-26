from playwright.sync_api import Page
from pages.base_page import BasePage
import logging



class MainPage(BasePage):
    def __init__(self, page: Page):
        logging.info("Initializing MainPage.")
        super().__init__(page)
        