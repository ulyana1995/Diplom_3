from actions.api_actions import create_order_by_api
from pages.login_page import LoginPage 
from pages.order_feed_page import OrderFeedPage
from pages.header import Header
import allure

class TestOrderFeedPage:
    @allure.title("Открытие модального окна с деталями заказа при клике на заказ")
    def test_click_order_opens_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Открываем страницу ленты заказов"):
            order_feed_page.open()
        
        with allure.step("Кликаем по первому заказу в списке"):
            order_feed_page.click_first_order()

        with allure.step("Проверяем, что открыто модальное окно с деталями заказа"):
            assert order_feed_page.order_details_modal_displayed(), "Детали заказа не отобразились в модальном окне"

    @allure.title("Отображение заказа пользователя в ленте заказов")
    def test_created_order_is_visible_in_order_feed(self, driver, created_user, order_number):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Логинимся пользователем"):
            login_page.login_as_user(created_user["email"], created_user["password"])

        header = Header(driver)

        with allure.step("Открываем ленту заказов"):
            header.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Проверяем, что заказ отображается в ленте заказов"):
            assert order_feed_page.is_order_in_feed(order_number), "Заказ не найден в ленте заказов"

    @allure.title("Увеличение счётчика 'Выполнено за всё время' при создании заказа")
    def test_total_orders_counter_increases_after_order(self, driver, created_user, ingredients_list):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Логинимся пользователем"):
            login_page.login_as_user(created_user["email"], created_user["password"])

        header = Header(driver)

        with allure.step("Открываем ленту заказов"):
            header.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Получаем текущее значение счётчика 'Выполнено за всё время'"):
            initial_count = order_feed_page.get_total_orders_count()

        with allure.step("Создаём новый заказ через API"):
            create_order_by_api(created_user["token"], ingredients_list)

        with allure.step("Ожидаем обновление счётчика 'Выполнено за всё время'"):
            order_feed_page.wait_for_total_counter_to_change(initial_count)  

        with allure.step("Получаем новое значение счётчика 'Выполнено за всё время'"):    
            current_count = order_feed_page.get_total_orders_count()

        with allure.step("Проверяем, что счётчик увеличился"):
            assert current_count > initial_count, "Счётчик заказов 'Выполнено за всё время' не увеличился"

    @allure.title("Увеличение счётчика 'Выполнено за сегодня' при создании заказа")
    def test_daily_orders_counter_increases_after_order(self, driver, created_user, ingredients_list):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Логинимся пользователем"):
            login_page.login_as_user(created_user["email"], created_user["password"])

        header = Header(driver)

        with allure.step("Открываем ленту заказов"):
            header.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step("Получаем текущее значение счётчика 'Выполнено за сегодня'"):
            initial_count = order_feed_page.get_daily_orders_count()

        with allure.step("Создаём новый заказ через API"):
            create_order_by_api(created_user["token"], ingredients_list)

        with allure.step("Ожидаем обновление счётчик 'Выполнено за сегодня'"):
            order_feed_page.wait_for_daily_counter_to_change(initial_count) 

        with allure.step("Получаем новое значение счётчика 'Выполнено за сегодня'"):     
            current_count = order_feed_page.get_daily_orders_count()

        with allure.step("Проверяем, что счётчик увеличился"):
            assert current_count > initial_count, "Счётчик заказов 'Выполнено за сегодня' не увеличился"

    @allure.title("Отображение нового заказа в статусе 'В работе' после создания")
    def test_new_order_appears_in_progress(self, driver, created_user, ingredients_list):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()
        
        with allure.step("Логинимся пользователем"):
            login_page.login_as_user(created_user["email"], created_user["password"])

        header = Header(driver)

        with allure.step("Открываем ленту заказов"):
            header.click_order_feed_button()

        with allure.step("Создаём новый заказ через API"):
            order_numb = create_order_by_api(created_user["token"], ingredients_list)

        order_feed_page = OrderFeedPage(driver)
        
        with allure.step("Ожидаем появления заказа в разделе 'В работе'"):
            assert order_feed_page.wait_until_order_appears_in_progress(order_numb), "Заказ не появился в разделе 'В работе'"
