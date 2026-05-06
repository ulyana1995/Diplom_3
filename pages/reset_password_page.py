from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    def _get_password_field_class(self):
        element = self.find_visible_element(ResetPasswordPageLocators.PASSWORD_FIELD)
        return element.get_attribute("class")

    def wait_for_load_reset_password_page(self):
        return self.wait_for_url_contains("/reset-password")

    def password_field_displayed(self):
        return self.find_visible_element(ResetPasswordPageLocators.PASSWORD_FIELD).is_displayed()

    def click_show_password_icon(self):
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_ICON)

    def password_field_active(self):
        return "input_status_active" in self._get_password_field_class()
