from playwright.sync_api import Page
import pytest
from pages.login_page import Login


@pytest.fixture()
def login(page:Page):
    return Login(page)

