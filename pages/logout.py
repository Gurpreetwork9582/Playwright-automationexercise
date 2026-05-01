import re
from playwright.sync_api import expect, Page

class Logout():
    def __init__(self,page:Page):
        self.page=page
        self.user_Hamburger = self.page.get_by_role("banner").get_by_text("manda user")
        self.logout_button = self.page.get_by_role("menuitem", name="Logout")
        self.logout_successful = self.page.get_by_role("heading", name="Login")
        

    def logout(self):
        self.user_Hamburger.click()
        self.logout_button.click()

    def is_logout_Successful(self):
        expect(self.logout_successful).to_be_visible()


