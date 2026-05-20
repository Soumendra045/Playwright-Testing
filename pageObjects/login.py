from pageObjects.dashboard import DashboardPage
class LoginPage:
    def __init__(self, page):
        self.page = page
        

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/",
                        wait_until="domcontentloaded",
                        timeout=60000) 
    
    def login(self, user_credentials):
        self.page.get_by_placeholder("email@example.com").fill(user_credentials['userEmail'])
        self.page.get_by_placeholder("enter your passsword").fill(user_credentials['userPassword'])
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage