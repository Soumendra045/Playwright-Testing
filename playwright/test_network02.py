from utils.apiBase import APIUtils
from playwright.sync_api import Page,  Playwright, expect
import time

def intercept_request(route):
    route.continue_(
            url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0"
            
    )

def test_network02(page: Page):
    page.goto("https://rahulshettyacademy.com/client/",
                wait_until="domcontentloaded",
                timeout=60000)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    # Login
    page.get_by_placeholder("email@example.com").fill("soumendra096@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Silu@0045")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()

    # time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_stroge(playwright: Playwright):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)
    print(token)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject insession local stroge
    page.add_init_script(f"""
        localStorage.setItem('token', '{token}');
    """)
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()