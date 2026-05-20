from pageObjects.ordersHistory import OrderHistryPage
class DashboardPage:
    def __init__(self, page):
        self.page = page
        
    def selectOrderNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistryPage = OrderHistryPage(self.page)
        return orderHistryPage

    