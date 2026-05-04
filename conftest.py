import pytest
from auth_session_state import create_state


#page is also a fixture which works under the hood which does 
#@pytest.fixture
#def page():
#    browser = launch_browser()
#    context = browser.new_context()
#    page = context.new_page()
#    yield page
#    context.close()
#    browser.close()

'''
from playwright.sync_api import Page
from pages.login_page import Login
from pages.logout import Logout
from pages.Claims import Claim

@pytest.fixture
def login(page:Page) -> Login:
    return Login(page)


@pytest.fixture
def logout(page:Page) -> Logout:
    return Logout(page)

def claim(page)->Claim:
    return Claim(page)

'''

@pytest.fixture(scope="session")
def context(browser):
    return browser.new_context(storage_state="auth.json")


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(autouse=True)
def open_dashboard(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")