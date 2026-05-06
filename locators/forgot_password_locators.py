from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[contains(@class,'input__textfield')]")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]") 
