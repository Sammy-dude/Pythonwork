import pytest
from playwright.sync_api import playwright, sync_playwright


@pytest.fixture(scope="class")
def browser(request):
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser # this is like after method
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
        page = browser.new_page()
        yield page
        page.close()

# def test1_goto_google(page):
#     page.goto("https://www.google.com")
#     assert "Google" == page.title()
#     # assert "https://www.google.com"== page.url()
#     #

@pytest.mark.usefixtures('browser')
class Test_tilteclas:
    def test_goto_google(self, page):
        page.goto("https://www.google.com")
        assert 'Google' == page.title()
        assert  'https://www.google.com/'== page.url

    def test1_goto_google(self, page):
        # Navigate to Google
        page.goto("https://www.google.com")

        # Verify the page title is 'Google'
        assert page.title() == "Google"

        # Verify the URL is correct
        assert page.url == "https://www.google.com/"

    def test_goto_redbus1(self, page):
        page.goto("https://www.redbus.com")
        assert "Book Bus Tickets Online with redBus!" == page.title()
        # assert page.url == "https://www.redbus.com"

# def test_goto_redbus(page):
#     page.goto("https://www.redbus.com")
#     assert "Book Bus Tickets Online with redBus!"== page.title()
#     # assert page.url == "https://www.redbus.com"