import time
import logging
import allure
import random
from selenium.webdriver.common.by import By
from src.actions.input_reg_form_data import input_reg_form_data
from src.actions.primenenie_kupona import primenenie_kupona
from src.actions.proverka_skidki import proverka_skidki
from src.actions.push_product_to_card import push_product_to_card
from src.actions.push_to_card_from_slider import push_to_card_from_slider
from src.actions.registration import registration
from src.fixtures.set_up_browser import set_up_browser
from src.actions.interceptor import interceptor
from selenium.webdriver.support.ui import WebDriverWait


class TestClass1:

    @allure.feature('тест сьют Сайт Pizzeria, flou 2')
    @allure.description('Проверка применения действующего купона')
    def test_kupon(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        wait = WebDriverWait(driver, timeout=10)
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(5)
        logging.info('Выбор товаров из сладера в корзину')
        push_to_card_from_slider(driver)
        logging.info('Переход в корзину')
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        logging.info('Применение купона')
        primenenie_kupona(driver, wait, 'GIVEMEHALYAVA')
        time.sleep(2)
        logging.info('Проверка применения скидки')
        price = driver.find_element(By.XPATH, '//div[@class="cart_totals"]//td[@data-title="Общая стоимость"]//bdi').text
        total_price = driver.find_element(By.XPATH, '//td[@data-title="Сумма"]//bdi').text
        proverka_skidki(1, price, total_price)
        time.sleep(6)

    @allure.feature('тест сьют Сайт Pizzeria, flou 2')
    @allure.description('Проверка применения недействующего купона')
    def test_kupon2(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        wait = WebDriverWait(driver, timeout=10)
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(5)
        logging.info('Выбор товаров из сладера в корзину')
        push_to_card_from_slider(driver)
        logging.info('Переход в корзину')
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        logging.info('Применение купона')
        primenenie_kupona(driver, wait, 'DC120')
        time.sleep(2)
        logging.info('Проверка применения скидки')
        price = driver.find_element(By.XPATH,
                                    '//div[@class="cart_totals"]//td[@data-title="Общая стоимость"]//bdi').text
        total_price = driver.find_element(By.XPATH, '//td[@data-title="Сумма"]//bdi').text
        proverka_skidki(2, price, total_price)
        logging.info('Проверка прошла!')
        time.sleep(6)

    @allure.feature('тест сьют Сайт Pizzeria, flou 2')
    @allure.description('Блокировка применения купона. Блокировка web запроса.')
    def test_kupon_block(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        wait = WebDriverWait(driver, timeout=10)
        driver.request_interceptor = interceptor
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(5)
        logging.info('Выбор товаров из сладера в корзину')
        push_to_card_from_slider(driver)
        logging.info('Переход в корзину')
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        logging.info('Применение купона')
        primenenie_kupona(driver, wait, 'GIVEMEHALYAVA')
        time.sleep(2)
        logging.info('Проверка применения скидки')
        price = driver.find_element(By.XPATH,
                                    '//div[@class="cart_totals"]//td[@data-title="Общая стоимость"]//bdi').text
        total_price = driver.find_element(By.XPATH, '//td[@data-title="Сумма"]//bdi').text
        proverka_skidki(2, price, total_price)
        logging.info('Проверка прошла!')
        time.sleep(6)

    @allure.feature('тест сьют Сайт Pizzeria, flou 2')
    @allure.description('Выбор товаров в корзину, переход на страницу авторизации, оформление заказа')
    def test_second_kupon(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        num = str(random.randrange(1, 999999))
        wait = WebDriverWait(driver, timeout=10)
        order_list = ['username', 'lastname', 'Казанская 52 - 64', 'Казань', 'Татарстан', '420000',
                      '78435555555', 'ex' + num + '@inbox.ru']
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(8)
        logging.info('Заполнение корзины - первый заказ:')
        push_product_to_card(driver)
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//a[text() = "Мой аккаунт"]')
        elem.click()
        logging.info('Процедура регистрации')
        elem = driver.find_element(By.XPATH, '//button[@class="custom-register-button"]')
        elem.click()
        time.sleep(2)
        registration(driver, num, order_list)
        logging.info('Переход к корзину')
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        logging.info('Применение купона')
        primenenie_kupona(driver, wait, 'GIVEMEHALYAVA')
        time.sleep(2)
        logging.info('Проверка применения скидки в первый раз')
        price = driver.find_element(By.XPATH,
                                    '//div[@class="cart_totals"]//td[@data-title="Общая стоимость"]//bdi').text
        total_price = driver.find_element(By.XPATH, '//td[@data-title="Сумма"]//bdi').text
        proverka_skidki(1, price, total_price)
        logging.info('Проверка прошла!')
        logging.info('Переход к оплате')
        driver.find_element(By.XPATH, '//a[@class="checkout-button button alt wc-forward"]').click()
        logging.info('Ввод реквизитов доставки: Имя, Фамилия, Адрес, Город, Обл, Индекс, Телефон, Дата заказа...')
        input_reg_form_data(1, driver, order_list)
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-26"]/a')
        elem.click()
        time.sleep(5)
        logging.info('Заполнение корзины - второй заказ:')
        push_product_to_card(driver)
        logging.info('Переход к корзину')
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        time.sleep(3)
        logging.info('Применение купона')
        primenenie_kupona(driver, wait, 'GIVEMEHALYAVA')
        time.sleep(2)
        logging.info('Проверка применения скидки в второй раз')
        price = driver.find_element(By.XPATH,
                                    '//div[@class="cart_totals"]//td[@data-title="Общая стоимость"]//bdi').text
        total_price = driver.find_element(By.XPATH, '//td[@data-title="Сумма"]//bdi').text
        proverka_skidki(2, price, total_price)
        time.sleep(10)
