from playwright.sync_api import sync_playwright


def test_yahoo2():
    with sync_playwright() as p:
        # Launch the browser (visible mode)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.get_by_label("Search", exact=True).click()
        page.get_by_label("Search", exact=True).fill("hi")
        page.goto("https://demo.automationtesting.in/Register.html")
        page.get_by_placeholder("First Name").click()
        page.get_by_placeholder("First Name").fill("sam")
        page.get_by_placeholder("First Name").press("Tab")
        page.get_by_placeholder("Last Name").fill("Salo")
        page.locator("textarea").click()
        page.locator("textarea").fill("HI")
        page.locator("textarea").press("Tab")
        page.locator("input[type=\"email\"]").fill("Yes")
        page.locator("input[type=\"email\"]").press("Tab")
        page.locator("input[type=\"tel\"]").fill("617-686-2876")
        page.get_by_label("Male", exact=True).check()
        page.locator("#checkbox2").check()
        page.locator("#checkbox3").check()


        # ---------------------
        context.close()
        browser.close()


if __name__ == "__main__":
     test_yahoo2()
