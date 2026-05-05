from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def click_order_history_button(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    def click_logout_button(self):
        element = self.find_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.scroll_to_element(element)
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)  
