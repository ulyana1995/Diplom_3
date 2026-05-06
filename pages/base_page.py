from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    TIMEOUT = 10
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)        

    def find_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
            )

    def find_elements(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator)
            )
    
    def find_visible_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
    
    def click_element(self, locator, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
            )
        element.click()

    def enter_text(self, locator, text, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        element.send_keys(text)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_invisibility(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator))
        
    def wait_for_url_contains(self, url_part, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(url_part))
    
    def wait_for_text_to_change(self, locator, old_text, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.text_to_be_present_in_element(locator, old_text))
    
    def wait_until(self, condition, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(condition)
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    