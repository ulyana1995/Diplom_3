from pages.base_page import BasePage
from config import BASE_URL
from locators.constructor_page_locators import ConstructorPageLocators

class ConstructorPage(BasePage):
    _URL = BASE_URL

    def open(self):
        self.open_page(self._URL)

    def wait_for_load_constructor_page(self):
        return self.wait_for_url_contains(self._URL)

    def login_button_displayed(self):
        return self.find_visible_element(ConstructorPageLocators.LOGIN_BUTTON).is_displayed() 

    def click_ingredient(self):
        self.click_element(ConstructorPageLocators.FIRST_INGREDIENT)

    def ingredient_details_popup_displayed(self):
        return self.find_visible_element(ConstructorPageLocators.INGREDIENT_DETAILS_TITLE).is_displayed()

    def click_close_button(self):
        self.click_element(ConstructorPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    def ingredient_details_popup_closed(self):
        return self.wait_for_element_invisibility(ConstructorPageLocators.INGREDIENT_DETAILS_TITLE)
    
    def drag_and_drop_ingredient(self):
        source = self.find_visible_element(ConstructorPageLocators.FIRST_INGREDIENT)
        target = self.find_visible_element(ConstructorPageLocators.BASKET_CONTAINER)

        self._drag_and_drop_js(source, target)

    def get_ingredient_counter_value(self):
        return int(self.find_visible_element(ConstructorPageLocators.INGREDIENT_COUNTER).text)

    def _drag_and_drop_js(self, source, target):
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            const fireEvent = (type, element) => {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                element.dispatchEvent(event);
            };

            fireEvent('dragstart', source);
            fireEvent('dragenter', target);
            fireEvent('dragover', target);
            fireEvent('drop', target);
            fireEvent('dragend', source);
        """, source, target) 

    def click_create_order(self):
        self.click_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    def order_modal_displayed(self):
        return self.find_visible_element(ConstructorPageLocators.ORDER_SUCCESS_MODAL).is_displayed()
    
    def get_order_number(self):
        return self.find_visible_element(ConstructorPageLocators.ORDER_NUMBER).text
