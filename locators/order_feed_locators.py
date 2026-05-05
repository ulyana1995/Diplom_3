from selenium.webdriver.common.by import By

class OrderFeedLocators:
    DAILY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    FIRST_ORDER = (By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits-default')][1]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class,'Modal_orderBox')]/p[contains(@class,'digits')]")
    ORDERS_LIST = (By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits-default')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    ORDER_LIST_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//li")   
