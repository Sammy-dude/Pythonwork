from os import login_tty

from playwright.sync_api import sync_playwright
import time

def test_4():
    with (sync_playwright() as p):
        # Launch the browser (visible mode)
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # Navigate to Yahoo homepage
        page.goto("https://demo.automationtesting.in/Register.html")

        # Wait until the search bar element is available


        # '//button[text()="Submit"]'.//p [text()="Forgot your password? "]
        # forget_password = page.wait_for_selector('//p[text()="Forgot your password? "]')
        header_text =page.get_by_role("heading", name="Automation Demo Site").text_content()
        print(header_text)
        page.wait_for_selector("//input[@placeholder ='First Name']")
        firstname_seelctor=page.wait_for_selector("//input[@placeholder ='First Name']")
        firstname_text=page.get_by_placeholder("First Name").inner_text()
        firstname_leble=page.get_by_placeholder("First Name").text_content()
        Myineervalue=firstname_seelctor.input_value()
        Myineervalue1=firstname_seelctor.get_attribute("placeholder")
        print(Myineervalue1 + "--------" * 20)
        print(firstname_text +"--------"*20)
        print(firstname_leble + "--------" * 20)
        # Wait for the input field to appear
        firstname_selector = page.wait_for_selector("//input[@placeholder='First Name']")

        # Get the input's current value (which might be pre-filled in some cases)
        firstname_value = firstname_selector.input_value()
        print("Input value:", firstname_value)

        # Get the placeholder text directly from the attribute
        firstname_placeholder = firstname_selector.get_attribute("placeholder")
        print("Placeholder text:", firstname_placeholder)

        # Example assertion if the default value is expected to be 'First Name'
        # assert firstname_value == "First Name", "The initial value is not 'First Name'"

        # assert page.get_by_placeholder(
        #     "First Name").input_value() == "First Name", "The initial value of the input is not 'First Name'"
        page.get_by_placeholder("First Name").click()
        page.get_by_placeholder("First Name").fill("sam")
        page.get_by_placeholder("Last Name").click()
        page.get_by_placeholder("Last Name").fill("salo")
        page.locator("textarea").click()
        page.locator("textarea").fill("88 marshal")
        page.locator("input[type=\"email\"]").click()
        page.locator("input[type=\"email\"]").fill("osalo@gmail.com")
        page.locator("input[type=\"tel\"]").click()
        page.locator("input[type=\"tel\"]").fill("617-112-112")
        page.get_by_text("Male", exact=True).click()
        malelable=page.get_by_text("Male", exact=True).text_content()
        print(malelable)
        femalelable = page.get_by_text("FeMale", exact=True).text_content()
        print(femalelable)
        page.get_by_text("Cricket").click()
        page.locator("#checkbox1").check()
        page.locator("#checkbox2").check()
        page.locator("#checkbox3").check()
        page.locator("#checkbox2").uncheck()
        page.locator("#msdd").click()
        # all_languages = page.locator(".ui-corner-all")
        # for lang in all_languages.all_text_contents():
        #     print(lang)
        # # lanpage.get_by_text("Arabic").click()
        page.locator("//select[ @ id = 'countries']").click()
        all_countries = page.locator("//select[@id='countries']/option")

        # Print each country name
        for country in all_countries.all_text_contents():
            print(country)


        # context.close()
        browser.close()


if __name__ == "__main__":
    test_4()