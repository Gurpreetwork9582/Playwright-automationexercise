import pytest
from playwright.sync_api import Page
from pages.Claims import Claim


@pytest.mark.claim
def test_claim(page:Page):
    claim=Claim(page)
    
    claim.claim(page)
    claim.Check_claim(page)