import inspect

from playwright.sync_api import sync_playwright

def current_line_number():
        return inspect.currentframe().f_back.f_lineno

# Example usage

def test_multiple_tabs():
    with sync_playwright() as p:
        # Launch the browser (visible mode)
        browser = p.chromium.launch(headless=False)

        # Create a browser context (allows you to open multiple tabs)
        context = browser.new_context()

        # Open the first tab and navigate to the first URL
        page1 = context.new_page()
        page1.goto("https://demo.automationtesting.in/Windows.html")
        lab=page1.text_content('//h1[text() = "Automation Demo Site "]')
        assert "Automation Demo Site" in page1.text_content('//h1[text() = "Automation Demo Site "]')
         # h1[text() = "Automation Demo Site "]
        # Click on the button that says 'click'. //button[@class="btn btn-info"]
        # Prepare to catch the new tab
        with context.expect_page() as new_page_info:
        # Click on the button that is expected to open a new tab
            page1.click('//button[@class="btn btn-info"]')
        # new_page represents the new tab
        new_page = new_page_info.value

        # Ensure the new page has loaded
        new_page.wait_for_load_state()
        print("This is line", current_line_number())
        # Capture and print the URL of the new page
        print(f"New URL: {new_page.url}")
        print("This is line", current_line_number())
        # Open the second tab and navigate to the second URL
        page2 = context.new_page()
        page2.goto("https://www.wikipedia.org")
        # page.wait_for_selector('//button[(text()="    click   ")]')
        lable1=page2.wait_for_selector('//strong[text()="The Free Encyclopedia"]')
        # assert lable1.get_attribute("class") == "search-input-text"
        assert lable1.inner_text() =="The Free Encyclopedia"
        assert lable1.get_attribute("class")=="jsl10n localized-slogan"
        assert lable1.is_visible()==True
        page2.wait_for_timeout(2000)
        search_box=page2.wait_for_selector('//input[@id="searchInput"]')
        search_box.fill("reference")
        print("This is line", current_line_number())

        search_box.click()



        # Open the third tab and navigate to the third URL
        page3 = context.new_page()
        page3.goto("https://www.github.com")

        # The browser will remain open and the program will pause here
        #input("Press Enter to exit and close the browser...")

        # Optionally, you can close the browser after pressing Enter
        # browser.close()

# Run the function
# if __name__ == "__main__":
#     main()main
# if open_multiple_tabs()
if __name__ == '__main__':
    test_multiple_tabs()