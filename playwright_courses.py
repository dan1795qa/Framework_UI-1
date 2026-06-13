from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
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

    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state='./browser-state-HW.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title_text).to_be_visible()
    expect(courses_title_text).to_have_text('Courses')

    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(view_title_text).to_be_visible()
    expect(view_title_text).to_have_text('There is no results')

    description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_be_visible()
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)
