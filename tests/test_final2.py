import time
import logging
import allure
import random
from selenium.webdriver.common.by import By
from src.actions.input_reg_form_data import input_reg_form_data
from src.actions.proverka_skidki import proverka_skidki
from src.actions.push_product_to_card import push_product_to_card
from src.actions.registration import registration
from src.fixtures.set_up_browser import set_up_browser
from selenium.webdriver.support.ui import WebDriverWait


class TestClass3:

    @allure.feature('тест сьют Сайт Pizzeria, flou 3')
    @allure.description('Выбор товаров в корзину, переход на страницу авторизации, оформление заказа, проверка работы бонусной карты')
    def test_bonus_card(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        num = str(random.randrange(1, 999999))
        order_list = ['username', 'lastname', 'Казанская 52 - 64', 'Казань', 'Татарстан', '420000',
                      '78435555555', 'ex' + num + '@inbox.ru']
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(8)
        logging.info('Заполнение корзины:')
        push_product_to_card(driver)
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//a[text() = "Мой аккаунт"]')
        elem.click()
        logging.info('Процедура регистрации')
        elem = driver.find_element(By.XPATH, '//button[@class="custom-register-button"]')
        elem.click()
        time.sleep(2)
        registration(driver, num, order_list)
        elem = driver.find_element(By.XPATH, '//li[@ id = "menu-item-363"]/a[text() = "Бонусная программа"]')
        elem.click()
        time.sleep(5)
        elem = driver.find_element(By.XPATH, '//input[@id = "bonus_username"]')
        elem.click()
        elem.send_keys(order_list[0])
        elem = driver.find_element(By.XPATH, '//input[@id = "bonus_phone"]')
        elem.click()
        elem.send_keys(order_list[6])
        elem = driver.find_element(By.XPATH, '//button[@name = "bonus"]')
        elem.click()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        logging.info('Переход к корзину')
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        logging.info('Переход к оплате')
        driver.find_element(By.XPATH, '//a[@class="checkout-button button alt wc-forward"]').click()
        logging.info('Ввод реквизитов доставки: Имя, Фамилия, Адрес, Город, Обл, Индекс, Телефон, Дата заказа...')
        input_reg_form_data(2, driver, order_list)
        price = driver.find_element(By.XPATH, '//tr/th[contains(text(), "Subtotal:")]//following::span[1]').text
        total_price = driver.find_element(By.XPATH, '//tr/th[contains(text(), "Total:")]//following::span[1]').text
        proverka_skidki(3, price, total_price)
        time.sleep(10)
