import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)
