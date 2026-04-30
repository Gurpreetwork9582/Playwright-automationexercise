from playwright.sync_api import Page
import pytest


@pytest.fixture(autouse=True)
def open_url(page:Page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield
