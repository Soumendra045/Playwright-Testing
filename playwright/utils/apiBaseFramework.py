from playwright.sync_api import Playwright
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}
# import json

class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        userEmail = user_credentials['userEmail']
        userPassword = user_credentials['userPassword']
        api_context  = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = api_context.post(
            url="/api/ecom/auth/login",
            data={
               "userEmail": userEmail,
               "userPassword": userPassword 
            }
        )
        assert response.ok
        print(response.json())
        token = response.json()['token']
        return token


    def createOrder(self, playwright: Playwright, user_credentials):

        token = self.getToken(playwright, user_credentials)
        # print(token)

        api_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = api_context.post(
            url="/api/ecom/order/create-order",
            data=ordersPayload,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )

        print(response.json())
        response_data = response.json()
        orderId = response_data["orders"][0]
        return orderId