
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios
# pyre-ignore [missing-import]
from utils.apiBaseFramework import APIUtils
# pyre-ignore [missing-import]
from pageObjects.login import LoginPage


scenarios("../features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    """
    Fixture to share data between steps.
    """
    return {}

@given(parsers.parse("Place the item order with {username} and {password}"))
def place_item_order(playwright: Playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = orderId
    
@given("the user is on landing page")
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)  ##Object for login page
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse("I login to portal with {username} and {password}"))
def login_to_portal(username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(user_credentials)
    shared_data['dashboard_page'] = dashboardPage

@when("navigate to orders page")
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_page']
    orderHistryPage = dashboardPage.selectOrderNavLink()
    shared_data['order_history_page'] = orderHistryPage

@when("select the OrderId")
def select_the_orderId(shared_data):
    orderHistryPage = shared_data['order_history_page']
    orderDetailsPage = orderHistryPage.selectOrder(shared_data['order_id'])
    shared_data['order_details_page'] = orderDetailsPage

@then("order message is successfully displayed")
def order_message_is_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['order_details_page']
    orderDetailsPage.verifyOrder()
