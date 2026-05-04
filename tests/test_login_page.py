import pytest
from playwright.sync_api import Page,expect
import requests


@pytest.mark.smoke
def test_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.get_by_placeholder('username')
    page.get_by_placeholder('Password')
    page.get_by_role("button", name="Login")
    Dashboard=page.get_by_role("heading", name="Dashboard")
    expect(Dashboard).to_be_visible()
        

@pytest.mark.xfail
def test_Wrong_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.get_by_placeholder('username').fill("Admin234")
    page.get_by_placeholder('Password').fill('admin123341')
    page.get_by_role("button", name="Login").click()


