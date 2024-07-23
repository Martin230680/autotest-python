import time
import logging
import allure
from src.actions.validation_empty import validation_empty
from src.actions.validation_name import validation_name
from src.actions.validation_phone import validation_phone
from src.fixtures.set_up_browser import set_up_browser


class TestClass4:

    @allure.feature('тест сьют Сайт Pizzeria, flou 4')
    @allure.description('Валидация формы - Бонусная карта')
    def test_validation_empty(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        logging.info('Открыие страницы оформления бонусной карты')
        driver.get("http://pizzeria.skillbox.cc/bonus/")
        time.sleep(5)
        validation_empty(driver)
        time.sleep(5)

    @allure.feature('тест сьют Сайт Pizzeria, flou 4')
    @allure.description('Валидация формы - Бонусная карта')
    def test_validation_name(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        logging.info('Открыие страницы оформления бонусной карты')
        driver.get("http://pizzeria.skillbox.cc/bonus/")
        time.sleep(5)
        validation_name(driver)
        time.sleep(5)

    @allure.feature('тест сьют Сайт Pizzeria, flou 4')
    @allure.description('Валидация формы - Бонусная карта')
    def test_validation_phone(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        logging.info('Открыие страницы оформления бонусной карты')
        driver.get("http://pizzeria.skillbox.cc/bonus/")
        time.sleep(5)
        validation_phone(driver)
        time.sleep(5)
