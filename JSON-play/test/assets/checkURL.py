import inspect

from playwright.sync_api import sync_playwright
import requests


def current_line_number():
    return inspect.currentframe().f_back.f_lineno


def check_links(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        # Get cookies from the browser session
        cookies = page.context.cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
            print(cookie['name'], cookie['value'])
            print("This is line", current_line_number())

        # Set User-Agent from the browser to the session
        user_agent = page.evaluate("() => navigator.userAgent")
        session.headers.update({'User-Agent': user_agent})
        print(session.cookies)
        print("This is line", current_line_number())
        # Extract all hyperlinks from the page
        links = page.query_selector_all('a')
        for link in links:
            print(link.get_attribute('href'))
        print("Here are the counts for all a links :", len(links))
        urls = [link.get_attribute('href') for link in links if link.get_attribute('href')]
        myinteger=0
        for url in urls:
            print(" All URLs found on the page:", url)
            myinteger += 1
        print("Here are the counts of all the URLs:"+ str(myinteger))
        print("Here are the counts of all the URLs using the len :"+  str(len(urls)))

        # Close the browser
        browser.close()

    # Check each URL
    broken_links = []
    for link in urls:
        try:
            # Check using the session with cookies and headers
            response = session.get(link, allow_redirects=True, timeout=10)
            if response.status_code >= 400:
                broken_links.append((link, response.status_code))
        except requests.RequestException as e:
            broken_links.append((link, str(e)))

    return broken_links


# Example usage
broken_links = check_links("https://hyannisportresearch.com/?gh_src=6430bca63us")
for link, status in broken_links:
    print(f"Broken link: {link} - Status: {status}")
