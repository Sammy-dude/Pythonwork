import logging
import sys
from pkgutil import get_data

from playwright.sync_api import Page

class AutomationDemoPage:
    def __init__(self, context):
        self.page = context.new_page()
        self.url = "https://demo.automationtesting.in/Windows.html"
        self.heading_locator = '//h1[text() = "Automation Demo Site "]'
        self.new_tab_button = '//button[@class="btn btn-info"]'

    def open(self):
        self.page.goto(self.url)

    def validate_heading(self):
        return "Automation Demo Site" in self.page.text_content(self.heading_locator)

    def click_new_tab_button(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.click(self.new_tab_button)
        return new_page_info.value

class WikipediaPage:
    def __init__(self, context):
        self.page = context.new_page()
        self.url = "https://www.wikipedia.org"
        self.heading_locator = '//strong[text()="The Free Encyclopedia"]'
        self.search_box = '//input[@id="searchInput"]'

    def open(self):
        self.page.goto(self.url)

    def validate_heading(self):
        heading = self.page.wait_for_selector(self.heading_locator)
        return heading.inner_text() == "The Free Encyclopedia" and heading.is_visible()

    def search(self, query):
        search_box = self.page.wait_for_selector(self.search_box)
        search_box.fill(query)
        search_box.press("Enter")
class Github:
    def __init__(self, context):
        self.page = context.new_page()
        self.url = "https://github.com/"
        self.price_able = "a[href='/pricing']"
        # self.search_box = '//input[@id="searchInput"]'
        # get_by_role("button", name="Product")

    def open(self):
        self.page.goto(self.url)

    def validate_price_lable(self):
        pricing_label = self.page.wait_for_selector("a[href='/pricing']")
        return pricing_label.inner_text()

    def validate_security(self):
            # Click on the "Product" link
        # product_link = self.page.locator("summary[aria-label='Product']")
        product_link = self.page.get_by_role("button", name="Product")
        product_link.click()
        print(product_link.all)
        print(product_link.all.count)
        print(product_link.count)

        all_texts = []
        for item in product_link.all():  # `.all()` returns all matching elements as a list
            text = item.inner_text()
            # Print and log each item
            print("Product item:", text)
            logging.info("Product item: %s", text)
            sys.stdout.flush()  # Ensure immediate output in the console
            all_texts.append(text)
            # Locate the "Security" label
        security_label = self.page.get_by_role("link", name="Security Find and fix")
            # page.get_by_role("link", name="Security Find and fix")

            # Validate that the Security label is visible and has the correct text
        is_visible = security_label.is_visible()
        # text_correct = security_label.inner_text().contains("Security")
        text_correct = "Security" in security_label.inner_text()
            # page.get_by_role("link", name="Security Find and fix").click()

            # Return True if both conditions are met, otherwise False
        return is_visible, text_correct