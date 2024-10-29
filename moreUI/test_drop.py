from os import wait3

from playwright.sync_api import sync_playwright

def test_drop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo="1000")  # Set headless to True to run without opening a browser window
        page = browser.new_page()

        # Go to the website
        page.goto("https://demo.automationtesting.in/")

        # Click on 'Skip Sign In' to access the registration page directly
        page.click('text=Skip Sign In')
        page.wait_for_timeout(2000)
        # Wait for the page to load fully
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000)
        # Print all values in the "Skills" dropdown
        skills_dropdown = page.locator("select#Skills")
        skill_options = skills_dropdown.locator("option")
        page.wait_for_timeout(2000)
        print("Skills Dropdown Options:")
        for option in skill_options.all_text_contents():
            print(option)

        # Select "India" in the "Select Country" dropdown
        country_dropdown = page.locator("span[role='combobox']")
        country_dropdown.click()
        page.locator("li", has_text="India").click()

        # Validate that "United States" is part of the selection options
        country_options = page.locator("ul.select2-results__options li")
        country_names = country_options.all_text_contents()

        if "United States" in country_names:
            print("Validation Passed: 'United States' is in the country selection options.")
        else:
            print("Validation Failed: 'United States' is NOT in the country selection options.")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_drop()
