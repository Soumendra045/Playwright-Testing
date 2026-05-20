import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import json
from playwright.sync_api import Playwright, expect
from utils.apiBaseFramework import APIUtils
from pageObjects.login import LoginPage
# from pageObjects.dashboard import DashboardPage

file_path = os.path.join(os.path.dirname(__file__), "data", "credentials.json")


# json file -> util -> access into test

with open(file_path) as f:
    test_data = json.load(f)
    print(test_data)
    user_cerdentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials",user_cerdentials_list)
def test_ete_web_api(playwright: Playwright,browserInstance, user_credentials):
    

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)


    loginPage = LoginPage(browserInstance)  ##Object for login page
    loginPage.navigate()

    # Login
    dashboardPage = loginPage.login(user_credentials)
    # dashboard Page
    orderHistryPage = dashboardPage.selectOrderNavLink()

    # order is present (api)
    orderDetailsPage = orderHistryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrder()
