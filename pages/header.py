from pages.base_page import BasePage
from locators.header_page_locators import HeaderLocators

class Header(BasePage):
    def click_profile_button(self):
        self.click_element(HeaderLocators.PROFILE_LINK)

    def click_constuctor_button(self):
        self.click_element(HeaderLocators.CONSTUCTOR_BUTTON)    

    def click_order_feed_button(self):
        self.click_element(HeaderLocators.FEED_BUTTON)