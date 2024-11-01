import pytest
from page_objects import AutomationDemoPage, WikipediaPage, Github

@pytest.mark.usefixtures("browser_context")
class TestMultipleTabs:

    def test_multiple_tabs(self, browser_context):
        # Initialize the page objects with the context
        demo_page = AutomationDemoPage(browser_context)
        wikipedia_page = WikipediaPage(browser_context)
        github_page = Github(browser_context)

        # Open and validate the Automation Demo Site
        demo_page.open()
        assert demo_page.validate_heading(), "Failed to validate Automation Demo Site heading"
        new_page = demo_page.click_new_tab_button()

        # Validate new page URL after clicking the button
        new_page.wait_for_load_state()
        # Adjusted assertion to check the actual URL opened by the button
        assert "selenium.dev" in new_page.url, "New page URL did not contain expected text."

        # Open and validate the Wikipedia page
        wikipedia_page.open()
        assert wikipedia_page.validate_heading(), "Failed to validate Wikipedia heading"
        wikipedia_page.search("reference")

        github_page.open()
        assert github_page.validate_price_lable() =="Pricing", "Pricing label text does not match expected text."
        is_visible, text_correct = github_page.validate_security()

        # Assert both visibility and correctness of the text
        assert is_visible, "Security label is not visible."
        assert text_correct, "Security label text is incorrect."
