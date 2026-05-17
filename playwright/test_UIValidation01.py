from playwright.sync_api import Page, expect

def test_UIValidationScript(page: Page):
    #iphone X , Nokia Edge
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button", name="Add ").click()

    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="Add ").click()

    page.get_by_text("Checkout").click()

    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandles(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        childPage = popup_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
        # print(childPage.title())