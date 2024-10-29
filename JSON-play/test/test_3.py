from os import login_tty

from playwright.sync_api import sync_playwright
import time

def test_yahoo():
    with sync_playwright() as p:
        # Launch the browser (visible mode)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to Yahoo homepage
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Wait until the search bar element is available


        # '//button[text()="Submit"]'.//p [text()="Forgot your password? "]
        forget_password = page.wait_for_selector('//p[text()="Forgot your password? "]')
        forget_password.click()
        cancel_password = page.wait_for_selector('//button[@type="button"]')
        cancel_password.click()
        username= page.wait_for_selector('//input[@name="username"]')
        username.type('Admin')
        password=page.wait_for_selector('//input[@placeholder="Password"]')
        password.type('admin123')
        login=page.wait_for_selector('// button[ @ type = "submit"]')
        login.click()
        # time.sleep(3)

        # Type "welcome to my world" in the search bar
        # page.fill('//button[@type="button"]', "welcome to my world")

        page.wait_for_timeout(5000)

        page.goto('https://demo.automationtesting.in/Register.html')

        #//input[@placeholder="First Name"]. //textarea[@ng-model="Adress"]
        first_name = page.wait_for_selector('//input[@placeholder="First Name"]')
        first_name.type('Samm')
        last_name = page.wait_for_selector('//input[@placeholder="Last Name"]')
        last_name.type('Smith')
        text_name = page.wait_for_selector('//textarea[@ng-model="Adress"]')
        text_name.type('here is my address')
        email = page.wait_for_selector('//input[@ng-model="EmailAdress"]')
        email.type('sammy@kk.com')
        page.wait_for_timeout(5000)
        phone = page.wait_for_selector('//input[@ng-model="Phone"]')
        phone.type('617-888-33')
        page.wait_for_timeout(5000)
        #// input[ @ value = "Male"]
        gender = page.wait_for_selector('//input[@value="Male"]')
        gender.click()
        gender.check()
        page.wait_for_timeout(5000)
        # radio_button = page.query_selector('//input[@value="FeMale"]')
        # radio_button.click()
        # radio_button.check()check

        select_dropdown = page.query_selector('//select[@id="Skills"]')
        # 2. Select the option
        select_dropdown.select_option(label='Art Design')
        page.select_option('//select[@id="Skills"]', label='AutoCAD')
        page.wait_for_timeout(5000)
        # Press Enter to submit the search
        page.keyboard.press("Enter")

        # Wait for a while to observe the results
        page.wait_for_timeout(5000)

        # Close the browser
        browser.close()
def test_dialog():
    assert "Sammy" == "Sammy"

def test_label():
    assert "2"=="2"
if __name__ == "__main__":
    test_yahoo()
