
from playwright.sync_api import expect
class Login():
    def __init__(self,page):
        self.page =page
        self.username = self.page.get_by_placeholder('username')
        self.password = self.page.get_by_placeholder('Password')
        self.login_button=self.page.get_by_role("button", name="Login")
        self.login_successful= self.page.get_by_role("heading", name="Dashboard")
        self.base_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def Base_url(self):
        self.page.goto(self.base_url)

    def Login_user(self):
        self.username.fill("Guri9582")
        self.password.fill('admin123')
        self.login_button.click()

    def Check_login(self):
        expect(self.login_successful).to_be_visible()
        

