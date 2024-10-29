from playwright.sync_api import sync_playwright


# def test_yahoo():
#     with sync_playwright() as p:
#         # Launch the browser (visible mode)
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
class SearchPage:
        def __init__(self, page):
            self.page = page
            self.search_term_input = page.locator('[aria-label="Enter your search term"]')

        def navigate(self):
            self.page.goto("https://bing.com")

        def search(self, text):
            self.search_term_input.fill(text)
            self.search_term_input.press("Enter")