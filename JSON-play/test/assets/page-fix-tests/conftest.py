import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        # Initialize the browser and context
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        yield context  # Provide the context to the test
        browser.close()  # Close the browser after the test
