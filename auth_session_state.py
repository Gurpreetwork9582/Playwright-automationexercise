from playwright.sync_api import sync_playwright

def create_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        page.get_by_placeholder('username').fill("Guri9582")
        page.get_by_placeholder('Password').fill("admin123")
        page.get_by_role("button", name="Login").click()
        
        # SAVE LOGIN STATE(as auth.json)
        page.context.storage_state(path="auth.json")
        browser.close()


if __name__ == "__main__":
    create_state()