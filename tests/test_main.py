import pytest
from playwright.sync_api import Page, expect
from pages.main_page import MainPage


def test_main_page(page: Page):
    main_page = MainPage(page)
    assert main_page.is_text_visible("h2", "Welcome")

    

