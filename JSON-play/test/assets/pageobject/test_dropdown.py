import pytest
from playwright.sync_api import sync_playwright

def test_dropdown_labels_and_click():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the website
        page.goto("https://demo.automationtesting.in/Alerts.html")

        # Click on the 'SwitchTo' menu to open the dropdown
        page.click('//a[text()="SwitchTo"]')

        # Wait for the dropdown to be visible and select only the 3 items under 'SwitchTo'
        dropdown_items1 = page.locator('//ul[@class="dropdown-menu"]/li/a')
        dropdown_itemsname = [dropdown_items1.nth(i).inner_text() for i in range(3)]
        dropdown_itemsnamefilter =[]
        for OSA in dropdown_itemsname:
            dropdown_itemsnamefilter.append(OSA)

        print(dropdown_itemsnamefilter)
        dropdown_items = page.locator('//ul[@class="dropdown-menu"]//li/a[contains(@href, "Alerts") or contains(@href, "Windows") or contains(@href, "Frames")]')

        # Verify we have exactly 3 items
        assert dropdown_items.count() == 3, f"Expected 3 dropdown items, but found {dropdown_items.count()}"

        # Extract the text from the dropdown items
        dropdown_labels = [dropdown_items.nth(i).inner_text() for i in range(dropdown_items.count())]

        # Expected dropdown labels
        expected_labels = ["Alerts", "Windows", "Frames"]

        # Assert that the actual dropdown labels match the expected labels
        assert dropdown_labels == dropdown_itemsnamefilter, f"Expected {expected_labels}, but got {dropdown_itemsnamefilter}"

        # Optionally, click each dropdown item and perform further actions
        for i in range(dropdown_items.count()):
            dropdown_items.nth(i).click()
            page.wait_for_timeout(1000)  # Add delay to observe the click
            page.click('//a[text()="SwitchTo"]')  # Reopen the dropdown after each click

        # Close the browser
        browser.close()

# Run the test using pytest
# pytest -v
