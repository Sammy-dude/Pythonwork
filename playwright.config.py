from playwright.config import PlaywrightConfig

config = PlaywrightConfig(
    use={
        "headless": False,  # Set to True to run tests in headless mode
        "viewport": { "width": 1280, "height": 720 },
        "locale": "en-US",
        "timezone_id": "America/New_York"
    },
    projects=[
        {
            "name": "chromium",
            "use": {
                "browser_name": "chromium",
                "channel": "chrome"
            }
        },
        {
            "name": "firefox",
            "use": {
                "browser_name": "firefox"
            }
        },
        {
            "name": "webkit",
            "use": {
                "browser_name": "webkit"
            }
        }
    ],
    retries=2,  # Number of times to retry a failed test
    timeout=30000,  # Timeout for each test in milliseconds (30 seconds)
)