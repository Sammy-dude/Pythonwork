import pytest
from playwright.sync_api import playwright, sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        yield browser # this is like after method
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
        page = browser.new_page()
        yield page
        page.close()

def test_goto_google(page):
    page.goto("https://www.google.com")
    assert "Google" == page.title()
    # assert "https://www.google.com"== page.url()


def test_goto_redbus(page):
    page.goto("https://www.redbus.com")
    assert "Book Bus Tickets Online with redBus!"== page.title()
    # assert page.url == "https://www.redbus.com"