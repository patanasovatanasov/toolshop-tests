from playwright.sync_api import Page
class LoginPage:
    URL = "https://practicesoftwaretesting.com/auth/login"
    def __init__(self, page: Page):
        self.page = page
        self.mail = page.get_by_placeholder("Your email")
        self.pwd = page.get_by_placeholder("Your password")
        self.login_button = page.locator(".btnSubmit")
        self.mail_alert = page.locator("#email-error")
        self.pwd_alert = page.locator("#password-error")
        self.alert_danger = page.locator(".alert-danger")

    def open(self):
        self.page.goto(self.URL)

    def login(self, email, password):
        self.mail.fill(email)
        self.pwd.fill(password)
        self.login_button.click()