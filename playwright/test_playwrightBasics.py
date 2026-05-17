from playwright.sync_api import Page, Playwright, expect
import time

def test_playwrightBasics(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

# chromium headless mode , 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com/")


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    # page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_label("Password:").fill("Learning@830$3mK288")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(4)

def test_fireforBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    # page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_label("Password:").fill("Learning@830$3mK288")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(4)