import SearchPage
from playwright.sync_api import sync_playwright
# in the test
def test_yahoo():
    with sync_playwright() as p:
    # Launch the browser (visible mode)
        browser = p.chromium.launch(headless=False)
    # page = browser.new_page()
        page =  browser.new_page()
        page.goto('https://demo.automationtesting.in/Windows.html')
        #search_page = SearchPage(page)
        # search_page.navigate()
        # page.wait_for_timeout(5000)
        # search_page.search("search query")