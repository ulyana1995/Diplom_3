from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from config import FEED_URL

class OrderFeedPage(BasePage):
    _URL = FEED_URL

    def open(self):
        self.open_page(self._URL)

    def wait_for_feed_page(self):
        return self.wait_for_url_contains("/feed")

    def orders_list_displayed(self):
        return self.find_visible_element(OrderFeedLocators.ORDERS_LIST).is_displayed()
    
    def click_first_order(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER)

    def order_details_modal_displayed(self):
        return self.find_visible_element(OrderFeedLocators.ORDER_DETAILS_MODAL).is_displayed()

    def is_order_in_feed(self, order_number):
        elements = self.find_elements(OrderFeedLocators.ORDERS_LIST)
        order_texts = []
        for element in elements:
                text_value = element.text.replace("#", "")
                order_texts.append(text_value)
        return any(order_number in text for text in order_texts)
    
    def wait_for_order_in_feed(self, order_number):
        self.wait_until(lambda _: self.is_order_in_feed(order_number))

    def get_total_orders_count(self):
        element = self.find_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(element.text)
    
    def get_daily_orders_count(self):
        element = self.find_element(OrderFeedLocators.DAILY_ORDERS_COUNTER)
        return int(element.text)

    def wait_for_total_counter_to_change(self, old_value):
        return self.wait_for_text_to_change(OrderFeedLocators.TOTAL_ORDERS_COUNTER, str(old_value))

    def wait_for_daily_counter_to_change(self, old_value):
        return self.wait_for_text_to_change(OrderFeedLocators.DAILY_ORDERS_COUNTER, str(old_value))

    def wait_until_order_appears_in_progress(self, order_number):
        target = int(order_number)

        return self.wait_until(
            lambda _: any(
                int(''.join(symbol for symbol in element.text if symbol.isdigit()) or "0") == target
                for element in self.find_elements(OrderFeedLocators.ORDER_LIST_IN_PROGRESS)
            )
        )
