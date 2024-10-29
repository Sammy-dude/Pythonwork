import asyncio
from wsgiref.validate import assert_

from playwright.async_api import async_playwright
import asyncio
from playwright.async_api import async_playwright
import playwright

def main():
    with playwright.playwright.start() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")

        # Find the search box and enter "Hi"
        search_box = page.locator("#lst-ib")
        search_box.fill("Hi")

        # Submit the search
        search_box.press("Enter")

        # Make an assertion to ensure the search results page is loaded
        assert "Hi" in page.title()

        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()