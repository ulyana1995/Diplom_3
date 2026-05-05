from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BASKET_CONTAINER = (By.CSS_SELECTOR, '[class^="BurgerConstructor_basket__list"]')
    CREATE_ORDER_BUTTON = (By.XPATH, f"//button[text()='Оформить заказ']")
    LOGIN_BUTTON = (By.XPATH, f"//button[text()='Войти в аккаунт']")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")   
    INGREDIENT_DETAILS_TITLE = (By.XPATH, f"//h2[text()='Детали ингредиента']")  
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.CSS_SELECTOR, '[class^="Modal_modal__close"]')
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, '[class^="counter_counter__num"]')
    ORDER_SUCCESS_MODAL = (By.XPATH, f"//p[text()='идентификатор заказа']") 
    ORDER_NUMBER = (By.XPATH, "(//a[contains(@class, 'Modal_modal__title')])[1]")
