from playwright.sync_api import Page

def intercept_response(route):
    route.fulfill(
        json = {"data":[],"message":"No Orders"}   
    )

def test_network01(page: Page):
    page.goto("https://rahulshettyacademy.com/client/",
                wait_until="domcontentloaded",
                timeout=60000)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    # Login
    page.get_by_placeholder("email@example.com").fill("soumendra096@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Silu@0045")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    print(page.locator(".mt-4").text_content())