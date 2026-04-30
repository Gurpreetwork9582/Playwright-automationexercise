from playwright.sync_api import Page
import pytest


@pytest.fixture(autouse=True)
def open_url(page:Page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield

@pytest.fixture
def logged_in(page: Page):
    page.get_by_placeholder('username').fill("Admin")
    page.get_by_placeholder('Password').fill('admin123')
    page.get_by_role("button", name="Login").click()
    return page
    
@pytest.fixture
def log_out(page:Page):
    page.get_by_alt_text("profile picture").click()
    page.get_by_text("Logout")
    