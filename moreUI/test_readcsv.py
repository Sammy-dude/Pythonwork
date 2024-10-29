import csv
import pytest
from playwright.sync_api import sync_playwright


# Function to read data from the CSV file
def read_test_data():
    data = []
    with open("test_data.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


# Parametrize the test with data from the CSV file
@pytest.mark.parametrize("data", read_test_data())
def test_login(data):
    username = data["username"]
    password = data["password"]
    expected_result = data["expected_result"]

    # Run Playwright test with the given data
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.wait_for_timeout(3000)
        # Fill in the login form with data from the CSV
        myusername=page.locator("[data-test=\"username\"]")
        myusername.fill(username)
        # page.fill("[data-test=\"username\"]", username)
        page.fill("[data-test=\"password\"]", password)
        page.click("[data-test=\"login-button\"]")
        # page.locator("[data-test=\"username\"]").click()
        # page.locator("[data-test=\"username\"]").fill("a")
        # page.locator("[data-test=\"password\"]").click()
        # page.locator("[data-test=\"password\"]").fill("pass")
        # page.locator("[data-test=\"login-button\"]").click() //h3[@data-test='error']

        # Example: check if login was successful or failed based on expected_result
        #//span[@class='title']
        if expected_result == "success":
            # Assert that the title "Products" is visible on successful login
            assert page.locator("span.title").is_visible(), "Login should be successful"
            assert page.locator("span.title").text_content() == "Products", "Expected 'Products' title on success"
        else:
            # Assert that the error message is visible on failed login
            error_message = page.locator("h3[data-test='error']")
            assert error_message.is_visible(), "Login should fail with an error message"
            # Customize the error message content check based on expected failure scenario
            assert error_message.text_content() == "Epic sadface: Username and password do not match any user in this service", "Unexpected error message"

        browser.close()
