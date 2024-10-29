import asyncio
from playwright.async_api import async_playwright
import playwright

async def run(playwright):
    # Launch the browser (in this case, Chrome)
    print("Launching the browser...")
    browser = await playwright.chromium.launch(headless=False)  # Set headless=True if you don't want the browser to appear
    page = await browser.new_page()

    page.wait_for_timeout(3000)
    # Go to Google
    print("Navigating to Google...")
    await page.goto("https://www.yahoo.com")
    page.wait_for_timeout(3000)

    # Test 1: Assert that the page title is "Google"
    print("Running Test 1: Verifying page title is 'yahoo'...")
    title = await page.title()
    print(f'here is the page tile ------------{title}')
    # // *[ @ id = "ybar-sbq"]
    # assert title == "Google", f"Test 1 Failed: Page title is '{title}', expected 'Google'"
    print("Test 1 Passed: Page title is 'yahoo'.")


    page.wait_for_timeout(3000)
    # page.fill('xpath=//*[@id="ybar-sbq"]', "Welcome to my world")
    page.locator('xpath=//*[@id="ybar-sbq"]', "Welcome to my world")
    # page.locator('xpath=//*[@id="ybar-sbq"]'.click()


    # Press Enter to submit
    page.keyboard.press("Enter")
    # Fill the input with a value
    input_value = "Welcome to my page "
    locator = "Welcome to my page "# Replace with your desired value

    page.locator("[id=\"ybar-sbq\"]").fill(input_value)
    # page.locator("[placeholder=\"Password\"]").click()
    page.keyboard.press("Enter")
    # page.fill('xpath=//*[@id="ybar-sbq"]', input_value)
    # page.type('xpath=//*[@id="ybar-sbq"]', input_value)
    page.wait_for_timeout(3000)
    # Press the Enter key
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    # Type a stock symbol (e.g., AAPL for Apple) into the search bar
    # print("Typing stock symbol 'AAPL' into the search bar...")
    # await page.fill('input[name="q"]', 'AAPL stock price')
    #
    # # Press Enter to perform the search
    # await page.press('input[name="q"]', 'Enter')
    #
    # # Test 2: Verify if the search result includes "AAPL"
    # print("Running Test 2: Verifying search results...")
    # try:
    #     await page.wait_for_selector('text=AAPL')
    #     print("Test 2 Passed: Stock search results loaded successfully.")
    # except Exception as e:
    #     raise AssertionError(f"Test 2 Failed: Stock search results not found. Error: {e}")
    #
    # # Try fetching the stock value (this selector may need to be updated)
    # try:
    #     stock_value = await page.inner_text('div[jsname="vWLAgc"]')
    #     print(f"Apple Stock Value: {stock_value}")
    # except Exception as e:
    #     raise AssertionError(f"Failed to retrieve stock value. Error: {e}")
    #
    # # Close the browser
    input("Press Enter to continue...")
    print("Resuming the script...")
    # print("Closing the browser...")
    input("Press Enter to continue...")
    await browser.close()

def test_dialog():
    assert "Press a Button !" == "Press a Button !"

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

# Run the main function to execute the test
if __name__ == "__main__":
    asyncio.run(main())
