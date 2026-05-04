from playwright.sync_api import Page, expect


DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


def test_logout(page:Page):
    page.goto(DASHBOARD_URL)
    dashboard = page.get_by_role("heading", name="Dashboard")
    expect(dashboard).to_be_visible()

    page.get_by_alt_text("profile picture").click()
    page.get_by_role("menuitem", name="Logout").click()

    expect(page.get_by_role("heading", name="Login")).to_be_visible()
