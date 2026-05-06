from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage 
from pages.header import Header
from pages.order_feed_page import OrderFeedPage
import allure

class TestConstructorPage:
    @allure.title("Переход на страницу конструктора при клике на линк 'Конструктор'")
    def test_click_constructor_opens_constructor_page(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step("Открываем страницу конструктора"):
            constructor_page.open()

        header = Header(driver)

        with allure.step("Кликаем по линк 'Конструктор' в хедере"):
            header.click_constuctor_button()

        with allure.step("Проверяем, что открыта страница конструктора"):
            assert constructor_page.wait_for_load_constructor_page(), "Переход на страницу Конструктора не выполнен"
       
        with allure.step("Проверяем, что отображается кнопка 'Войти в аккаунт'"):
            assert constructor_page.login_button_displayed(), "Кнопка 'Войти в аккаунт' не отобразилась" 

    @allure.title("Переход на страницу 'Лента заказов' при клике на кнопку в хедере")
    def test_click_order_feed_opens_feed_page(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем страницу конструктора"):
            constructor_page.open()

        header = Header(driver)  

        with allure.step("Кликаем по кнопке 'Лента заказов'"):     
            header.click_order_feed_button()

        feed_page = OrderFeedPage(driver)

        with allure.step("Проверяем, что открыта страница ленты заказов"):
            assert feed_page.wait_for_feed_page(), "Переход на страницу 'Лента заказов' не выполнен"
        
        with allure.step("Проверяем, что отображается список заказов"):
            assert feed_page.orders_list_displayed(), "Список заказов не отобразился"

    @allure.title("Открытие всплывающего окна с деталями ингредиента при клике на ингредиент")
    def test_ingredient_click_opens_details_popup(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем страницу конструктора"):
            constructor_page.open()

        with allure.step("Кликаем по ингредиенту"):
            constructor_page.click_ingredient()

        with allure.step("Проверяем, что открыто окно с деталями ингредиента"):
            assert constructor_page.ingredient_details_popup_displayed(), "Окно с деталями ингредиента не отобразилось"

    @allure.title("Закрытие всплывающего окна с деталями ингредиента по клику на крестик")
    def test_close_ingredient_details_popup_by_close_button(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step("Открываем страницу конструктора"):
            constructor_page.open()

        with allure.step("Кликаем по ингредиенту"):            
            constructor_page.click_ingredient()

        with allure.step("Закрываем всплывающее окно по клику на крестик"):    
            constructor_page.click_close_button()

        with allure.step("Проверяем, что всплывающее окно закрыто"):
            assert constructor_page.ingredient_details_popup_closed(), "Модальное окно с деталями ингредиента не закрылось"

    @allure.title("Увеличение каунтера ингредиента при добавлении в заказ")
    def test_add_ingredient_increases_counter(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step("Открываем страницу конструктора"):
            constructor_page.open()  

        with allure.step("Получаем начальное значение счётчика ингредиента"):
            initial_value = constructor_page.get_ingredient_counter_value()

        with allure.step("Добавляем ингредиент в заказ"):
            constructor_page.drag_and_drop_ingredient()

        with allure.step("Получаем текущее значение счётчика ингредиента"):
            current_count = constructor_page.get_ingredient_counter_value()

        with allure.step("Проверяем, что счётчик увеличился"):
            assert initial_value < current_count, "Счётчик не увеличился"

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_create_order_by_authenticated_user(self, driver, created_user):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Логинимся пользователем"):    
            login_page.login_as_user(created_user["email"], created_user["password"]) 

        constructor_page = ConstructorPage(driver)

        with allure.step("Добавляем ингредиент в заказ"):
            constructor_page.drag_and_drop_ingredient()

        with allure.step("Нажимаем кнопку 'Оформить заказ'"):   
            constructor_page.click_create_order()

        with allure.step("Проверяем, что появилось окно с номером заказа"):
            assert constructor_page.order_modal_displayed(), "Окно с номером заказа не появилось"
