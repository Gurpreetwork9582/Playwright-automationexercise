from playwright.sync_api import Page
import pytest
from pages.login_page import Login
from pages.logout import Logout

#page is also a fixture which works under the hood which does 
#@pytest.fixture
#def page():
#    browser = launch_browser()
#    context = browser.new_context()
#    page = context.new_page()
#    yield page
#    context.close()
#    browser.close()


@pytest.fixture()
def login(page:Page) -> Login:
    return Login(page)

@pytest.fixture
def logout(page:Page) -> Logout:
    return Logout(page)

