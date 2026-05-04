import os

from playwright.sync_api import sync_playwright


LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
AUTH_FILE = "auth.json"
USERNAME = os.getenv("ORANGEHRM_USERNAME", "Admin")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD", "admin123")


def create_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(LOGIN_URL)
        page.get_by_placeholder('Username').fill(USERNAME)
        page.get_by_placeholder('Password').fill(PASSWORD)
        page.get_by_role("button", name="Login").click()
        page.wait_for_url("**/dashboard/index")

        page.context.storage_state(path=AUTH_FILE)
        browser.close()


if __name__ == "__main__":
    create_state()
