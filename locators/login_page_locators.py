from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    LOGIN_BUTTON = (By.XPATH, f"//button[text()='Войти']")
    PASSWORD_INPUT = (By.NAME, "Пароль")
