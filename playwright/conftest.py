import pytest
from playwright.sync_api import Playwright

# import sys
# import os

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser name"
    )

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    match browser_name:
        case "Chrome":
            browser = playwright.chromium.launch(headless=False)
        case "Firefox":
            browser = playwright.firefox.launch(headless=False)
        case "WebKit":
            browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

    