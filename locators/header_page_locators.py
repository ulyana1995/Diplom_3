from selenium.webdriver.common.by import By

class HeaderLocators:
    CONSTUCTOR_BUTTON = (By.XPATH, f"//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, f"//p[text()='Лента Заказов']")
    PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    