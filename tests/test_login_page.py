import pytest
from playwright.sync_api import Browser, Page, expect


DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.mark.smoke
def test_login(page:Page):
    page.goto(DASHBOARD_URL)
    dashboard = page.get_by_role("heading", name="Dashboard")
    expect(dashboard).to_be_visible()
        

@pytest.mark.negative
def test_Wrong_login(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto(LOGIN_URL)
    page.get_by_placeholder("Username").fill("Admin234")
    page.get_by_placeholder("Password").fill("admin123341")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Invalid credentials")).to_be_visible()
    context.close()
