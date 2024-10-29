import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def handle_browser():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)

        yield browser # this is like after method
        browser.close()
    # context = browser.new_context()
    #
    # # Open new page
    # page = context.new_page()

@pytest.fixture(scope="function")
def page_handler(handle_browser):
    page=handle_browser.new_page()
    yield page
    page.close()


@pytest.mark.parametrize('invalid_username , invalid_password', [("admin","password"),("user","password")])
def test_invalidation(page_handler, invalid_username, invalid_password):
    page_handler.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page_handler.wait_for_selector('//input[@name="username"]')
    username.type(invalid_username)
    password = page_handler.wait_for_selector('//input[@placeholder="Password"]')
    password.type(invalid_password)
    login = page_handler.wait_for_selector('// button[ @ type = "submit"]')
    login.click()
    page_handler.wait_for_timeout(2000)
    error_massage= page_handler.wait_for_selector('//p[text()="Invalid credentials"]').text_content()
    assert error_massage == 'Invalid credentials'

# //p [(text(),"Invalid credentials")]. or //p[text()="Invalid credentials"] or //p[contains(text(), "Invalid credentials")]