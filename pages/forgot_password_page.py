from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from config import FORGOT_PASSWORD_URL

class ForgotPage(BasePage):
    _URL = FORGOT_PASSWORD_URL

    def open(self):
        self.open_page(self._URL)

    def wait_for_load_forgot_password_page(self):
        return self.wait_for_url_contains("/forgot-password")
    
    def recovery_button_displayed(self):
        return self.find_visible_element(ForgotPasswordLocators.RECOVERY_BUTTON).is_displayed()   

    def click_recovery_button(self):
        self.click_element(ForgotPasswordLocators.RECOVERY_BUTTON)

    def fill_email_input(self, text):
        self.enter_text(ForgotPasswordLocators.EMAIL_INPUT, text)
