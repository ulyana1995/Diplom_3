from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPage
from pages.reset_password_page import ResetPasswordPage
from utils.helpers import generate_random_email
import allure

class TestRecoveryPasswordPage:
    @allure.title("Переход на страницу восстановления пароля при клике на ссылку 'Восстановить пароль'")
    def test_forgot_password_page_opens_from_login(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Кликаем по ссылке 'Восстановить пароль'"):
            login_page.click_forgot_password_link()

        forgot_page = ForgotPage(driver)

        with allure.step("Проверяем, что открыта страница восстановления пароля"):
            assert forgot_page.wait_for_load_forgot_password_page(), "URL не содержит 'forgot-password'"

        with allure.step("Проверяем, что кнопка 'Восстановить' отображается"):
            assert forgot_page.recovery_button_displayed(), "Кнопка 'Восстановить' не отобразилось"

    @allure.title("Переход на страницу сброса пароля после ввода email и клика на кнопку 'Восстановить'")
    def test_forgot_password_opens_reset_password_page(self, driver):
        user_email = generate_random_email()
        forgot_page = ForgotPage(driver)
        with allure.step("Открываем страницу восстановления пароля"):
            forgot_page.open()
        
        with allure.step("Вводим email пользователя"):
            forgot_page.fill_email_input(user_email)
        
        with allure.step("Кликаем по кнопке 'Восстановить'"):
            forgot_page.click_recovery_button()

        reset_password_page = ResetPasswordPage(driver)
        with allure.step("Проверяем, что произошёл переход на страницу сброса пароля"):
            assert reset_password_page.wait_for_load_reset_password_page(), "URL не содержит 'reset-password'"
        
        with allure.step("Проверяем, что поле ввода пароля отображается"):
            assert reset_password_page.password_field_displayed(), "Поле 'Пароль' не отобразилось"

    @allure.title("Поле пароля становится активным и подсвечивается при клике на иконку показать/скрыть")
    def test_show_password_icon_highlights_password_field(self, driver):
        user_email = generate_random_email()
        forgot_page = ForgotPage(driver)
        with allure.step("Открываем страницу восстановления пароля"):
            forgot_page.open()
            
        with allure.step("Вводим email пользователя"):
            forgot_page.fill_email_input(user_email)

        with allure.step("Нажимаем кнопку восстановления пароля"):
            forgot_page.click_recovery_button()

        reset_page = ResetPasswordPage(driver)

        with allure.step("Кликаем на иконку глаза"):
            reset_page.click_show_password_icon()

        with allure.step("Проверяем, что поле пароля стало активным"):
            assert reset_page.password_field_active(), "Поле пароля не стало активным после клика на иконку глаза"
