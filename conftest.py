from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from api.ingredient_api import get_ingredients
from api.order_api import create_order
from api.user_api import delete_user, create_user
from data.user_data import generate_user_data, build_order_payload
from utils.helpers import generate_random_email
import pytest
import allure

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    with allure.step(f"Запуск браузера: {request.param}"):
        if request.param == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        else:
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        driver.maximize_window()

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()

@pytest.fixture
def user_email():
    return generate_random_email()

@pytest.fixture
def created_user():
    with allure.step("Генерация данных пользователя"):
        user_data = generate_user_data()
        email = user_data["email"]
        password = user_data["password"]
        name = user_data["name"]

    with allure.step("Создание пользователя через API"):    
        response = create_user(user_data)
        response_data = response.json()
        token = response_data.get("accessToken")
    yield {
        "email": email,
        "password": password,
        "name": name,
        "token": token       
    }
    with allure.step("Удаление пользователя"):
        delete_user(token)

@pytest.fixture
def ingredients_list():
    with allure.step("Получение списка ингредиентов"):
        response = get_ingredients()
        response_data = response.json()

    ingredients = []
    for ingredient in response_data["data"]:
        ingredients.append(ingredient["_id"])
    return ingredients  

@pytest.fixture
def order_number(created_user, ingredients_list):
    ingredient = ingredients_list[0]
    payload = build_order_payload([ingredient])
    with allure.step("Создание заказа"):
        response = create_order(payload, created_user["token"])
        response_data = response.json()
        number_ingredient = response_data["order"]["number"]
    return str(number_ingredient)
