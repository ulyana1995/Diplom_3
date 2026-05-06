from pages.base_page import BasePage

class OrderHistoryPage(BasePage):
    def wait_for_load_order_history_page(self):
        return self.wait_for_url_contains("/order-history")
    