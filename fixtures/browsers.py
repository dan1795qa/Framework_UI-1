import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_button = page.get_by_test_id('registration-form-email-input').locator('input')
    email_button.fill('test.name@gmail.com')

    username_button = page.get_by_test_id('registration-form-username-input').locator('input')
    username_button.fill('username')

    password_button = page.get_by_test_id('registration-form-password-input').locator('input')
    password_button.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='./browser-state-HW.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='./browser-state-HW.json')
    yield context.new_page()
    browser.close()
