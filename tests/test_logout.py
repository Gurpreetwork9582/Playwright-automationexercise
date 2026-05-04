from playwright.sync_api import Page,expect
import requests


def test_logout(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.get_by_placeholder('username')
    page.get_by_placeholder('Password')
    page.get_by_role("button", name="Login")
    Dashboard=page.get_by_role("heading", name="Dashboard")
    expect(Dashboard).to_be_visible()
    page.get_by_alt_text("profile picture").click()
    page.get_by_text("Logout")
    response = requests.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert response.status_code == 200