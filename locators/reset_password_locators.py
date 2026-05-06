from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    SHOW_PASSWORD_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]") 
    PASSWORD_FIELD = (By.XPATH, "//div[contains(@class,'input__container')]/div[contains(@class,'input_type_text')]")  
