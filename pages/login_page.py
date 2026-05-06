from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config import LOGIN_URL

class LoginPage(BasePage):
    _URL = LOGIN_URL

    def open(self):
        self.open_page(self._URL)

    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def wait_for_load_login_page(self):
        return self.wait_for_url_contains("/login")
    
    def email_field_displayed(self):
        return self.find_visible_element(LoginPageLocators.EMAIL_INPUT).is_displayed() 

    def fill_email_input(self, text):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, text)

    def fill_password_input(self, text):
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, text)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login_as_user(self, email, password):
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_login_button()    
