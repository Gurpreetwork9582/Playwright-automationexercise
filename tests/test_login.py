from playwright.sync_api import expect, Page
import re

def test_login(page: Page):
    page.get_by_role("link", name=" Signup / Login").click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    page.get_by_placeholder("Name").fill("admin")
    page.get_by_placeholder("Email Address").fill("admin@admin.com")
    page.get_by_role("button", name="Signup").click()
    page.locator('[data-qa="title"]').click()
    expect(page.locator('[data-qa="name"]')).to_have_text(re.compile("gurpreet",re.IGNORECASE))
    expect(page.locator('[data-qa="email"]')).not_to_be_empty()
    expect(page.get_by_role("input", name = "password")).fill("Gurpreet")    
    expect(page.locator('[data-qa="days"]')).to_have_value("6")
    


    