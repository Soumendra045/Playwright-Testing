from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils

def test_ete_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/",
                wait_until="domcontentloaded",
                timeout=60000)
    # Login
    page.get_by_placeholder("email@example.com").fill("soumendra096@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Silu@0045")
    page.get_by_role("button", name="Login").click()
    
    # order is present (api)
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    page.get_by_role("button", name="ORDERS").click()

    # Oredrhistory validation
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()