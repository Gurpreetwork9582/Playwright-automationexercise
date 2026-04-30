from playwright.sync_api import expect, Page
import re
import requests
import pytest


def test_login(page: Page):
    page.get_by_placeholder('username').fill("Admin")
    page.get_by_placeholder('Password').fill('admin123')
    page.get_by_role("button", name="Login").click()
    response = requests.get('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    assert response.status_code == 200
    
    
@pytest.mark.xfail
def test_Wrong_login(page:Page):
    page.get_by_placeholder('username').fill("Admin234")
    page.get_by_placeholder('Password').fill('admin123341')
    page.get_by_role("button", name="Login").click()


def test_logout(logged_in:Page):
    logged_in.get_by_alt_text("profile picture").click()
    logged_in.get_by_text("Logout")
    response = requests.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert response.status_code == 200
