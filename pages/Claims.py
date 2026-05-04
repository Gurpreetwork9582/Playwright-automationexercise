
import pytest
from playwright.sync_api import Page ,expect

class Claim():
    def __init__(self,page:Page):
        self.page=page
        self.claim_tab=self.page.get_by_role("link", name="Claim", exact=True)
        self.assign_claim=self.page.get_by_role("button", name=" Assign Claim")
        self.employee_name=self.page.get_by_role("option", name="gu s")
        self.event=self.page.get_by_role("option", name="Medical Reimbursement")
        self.currency=self.page.get_by_role("option", name="Canadian Dollar")
        self.remarks=self.page.locator("textarea")
        self.create_button=self.page.get_by_role("button", name="Create")
        self.submit_button=self.page.get_by_role("button", name="Submit")
        self.my_claims=self.page.get_by_role("listitem").filter(has_text="Employee Claims")
        
            
    def claim(self,page:Page):
        self.claim_tab.click()
        self.assign_claim.click()
        self.employee_name.click()
        self.event.click()
        self.currency.click()
        self.remarks.fill("test")
        self.create_button.click()
        self.submit_button.click()
        
        
    def Check_claim(self,page:Page):
        self.my_claims.click()
        expect(page.get_by_text("gu s")).to_be_visible()