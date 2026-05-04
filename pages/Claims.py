
import re

from playwright.sync_api import Page, expect

class Claim():
    def __init__(self,page:Page):
        self.page=page
        self.base_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.claim_tab=self.page.get_by_role("link", name="Claim", exact=True)
        self.assign_claim=self.page.get_by_role("button", name=re.compile("Assign Claim"))
        self.employee_name=self.page.get_by_placeholder("Type for hints...")
        self.employee_option=self.page.get_by_role("option", name="Ranga Akunuri")
        self.event_dropdown=self.page.locator(".oxd-select-text").nth(0)
        self.event=self.page.get_by_role("option", name="Medical Reimbursement")
        self.currency_dropdown=self.page.locator(".oxd-select-text").nth(1)
        self.currency=self.page.get_by_role("option", name="Canadian Dollar")
        self.remarks=self.page.locator("textarea")
        self.create_button=self.page.get_by_role("button", name="Create")
        self.submit_button=self.page.get_by_role("button", name="Submit")
        self.employee_claims=self.page.get_by_role("listitem").filter(has_text="Employee Claims")
        
            
    def claim(self,page:Page):
        self.page.goto(self.base_url)
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()
        self.claim_tab.click()
        self.assign_claim.click()
        self.employee_name.fill("Ranga")
        self.employee_option.click()
        self.event_dropdown.click()
        self.event.click()
        self.currency_dropdown.click()
        self.currency.click()
        self.remarks.fill("test")
        self.create_button.click()
        self.submit_button.click()
        
        
    def Check_claim(self,page:Page):
        self.employee_claims.click()
        expect(page.get_by_role("heading", name="Employee Claims")).to_be_visible()
