from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.pinterest.co.uk/login/
    page.goto("https://www.pinterest.co.uk/login/")

    # Click [placeholder="Email"]
    page.locator("[placeholder=\"Email\"]").click()

    # Fill [placeholder="Email"]
    page.locator("[placeholder=\"Email\"]").fill("osaloum@gmail.com")

    # Click [placeholder="Password"]
    page.locator("[placeholder=\"Password\"]").click()

    # Fill [placeholder="Password"]
    page.locator("[placeholder=\"Password\"]").fill("ppp")

    # Click button:has-text("Log in")
    # with page.expect_navigation(url="https://www.pinterest.co.uk/"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Log in\")").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)