from playwright.sync_api import Playwright
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}
# import json

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_context  = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = api_context.post(
            url="/api/ecom/auth/login",
            data={
               "userEmail": "soumendra096@gmail.com",
               "userPassword": "Silu@0045" 
            }
        )
        assert response.ok
        print(response.json())
        token = response.json()['token']
        return token


    def createOrder(self, playwright: Playwright):

        token = self.getToken(playwright)
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