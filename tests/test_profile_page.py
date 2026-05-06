from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage 
from pages.profile_page import ProfilePage
from pages.header import Header
from pages.order_history_page import OrderHistoryPage  
import allure

class TestProfilePage:
    @allure.title("Переход на страницу логина при клике на 'Личный кабинет'")
    def test_click_profile_opens_login_page(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step("Открываем страницу конструктора"):
            constructor_page.open()

        header = Header(driver)

        with allure.step("Кликаем по кнопке профиля"):
            header.click_profile_button()

        login_page = LoginPage(driver)
        with allure.step("Проверяем, что открыта страница логина"):
            assert login_page.wait_for_load_login_page(), "URL не содержит login"

        with allure.step("Проверяем, что отображается поле 'Email'"):
            assert login_page.email_field_displayed(), "Поле 'Email' не отобразилось"

    @allure.title("Переход в раздел 'История заказов'")
    def test_user_can_open_order_history_page(self, driver, created_user):
        login_page = LoginPage(driver)
        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Логинимся пользователем"):
            login_page.login_as_user(created_user["email"], created_user["password"]) 

        header = Header(driver)

        with allure.step("Кликаем по кнопке профиля"):
            header.click_profile_button()

        profile_page = ProfilePage(driver)

        with allure.step("Открываем раздел 'История заказов'"):
            profile_page.click_order_history_button()   

        order_history_page = OrderHistoryPage(driver)

        with allure.step("Проверяем, что открыта страница истории заказов"):
            assert order_history_page.wait_for_load_order_history_page, "URL не содержит 'order-history'"

    @allure.title("Выход пользователя из аккаунта через профиль")
    def test_user_can_logout_from_profile(self, driver, created_user):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()
        
        with allure.step("Логинимся пользователем"):
            login_page.login_as_user(created_user["email"], created_user["password"]) 

        header = Header(driver)

        with allure.step("Кликаем по кнопке профиля"):
            header.click_profile_button()                  

        profile_page = ProfilePage(driver)

        with allure.step("Нажимаем кнопку 'Выход'"):
            profile_page.click_logout_button()

        login_page = LoginPage(driver)
        
        with allure.step("Проверяем, что произошёл редирект на страницу логина"):
            assert login_page.wait_for_load_login_page(), "URL не содержит 'login'"

        with allure.step("Проверяем, что отображается поле 'Email'"):
            assert login_page.email_field_displayed(), "Поле 'Email' не отобразилось" 
