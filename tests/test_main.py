import pytest
from playwright.sync_api import Page, expect


def test_main_page(page: Page):
    text_locator = page.locator("h2", has_text="Welcome")
    expect(text_locator, "Welcome found").to_be_visible()

