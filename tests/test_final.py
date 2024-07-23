import time
import logging
import allure
from selenium.webdriver.common.by import By
from src.actions.add_product_from_slider import add_product_from_slider
from src.actions.choose_bort_of_pizza import choose_bort_of_pizza_and_col
from src.actions.choose_desert import choose_desert
from src.actions.compare_list import compare_list
from src.actions.get_attr import get_attr
from src.actions.compare_list1 import compare_list1
from src.actions.input_reg_form_data import input_reg_form_data
from src.actions.push_product_to_card import push_product_to_card
from src.actions.registration import registration
from src.actions.switch_to_card_of_product_click_img import switch_to_card_of_product_click_img
from src.fixtures.set_up_browser import set_up_browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class TestClass:

    @allure.feature('тест сьют Сайт Pizzeria, flou 1')
    @allure.description('Проверка работы слайдера главной страницы, перемещение выбранного товара в корзину, проверка корзины')
    def test_select_to_card_from_slider(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(5)
        logging.info('Заполнение корзины из сладера:')
        select_list = add_product_from_slider(driver)
        logging.info('Переход к корзину')
        driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]').click()
        basket_list = driver.find_elements(By.XPATH, '//*/td[@data-title="Товар"]')
        logging.info('Сравнение содержимого корзины с эталонным списком, сформированным при клике карточек слайдера')
        compare_list(0, basket_list, select_list)

    @allure.feature('тест сьют Сайт Pizzeria, flou 1')
    @allure.description('Переход на карточку товара, проверка соответствия выбранной карточки из слайдера')
    def test_description_product(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(5)
        assert_list = switch_to_card_of_product_click_img(driver)
        logging.info('Проверка перехода на карточку товара:')
        logging.info('Проверка соответствие названия товара в слайдере "Пицца «4 в 1»"с названием товара в карточке с описанием')
        logging.info(f'Название товара в сладере - {assert_list[0]}, Название товара в карточке - {assert_list[1]}')
        assert assert_list[0] == assert_list[1]
        logging.info('OK')
        logging.info('Проверка соответствие названия товара в слайдере Пицца «Рай» с названием товара в карточке с описанием')
        logging.info(f'Название товара в сладере - {assert_list[2]}, Название товара в карточке - {assert_list[3]}')
        assert assert_list[2] == assert_list[3]
        logging.info('OK')

    @allure.feature('тест сьют Сайт Pizzeria, flou 1')
    @allure.description('Выбор борта пиццы, количества пицы, проверка заказа в корзине')
    def test_bort_of_pizza(self, set_up_browser):
        driver = set_up_browser
        wait = WebDriverWait(driver, timeout=10)
        driver.maximize_window()
        logging.info('Открыие сайта в карточке "Пицца Рай"')
        driver.get("http://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9//")
        time.sleep(5)
        logging.info('Выбор борта обычный, сырный, колбасный:')
        bort_list1, col_list1 = choose_bort_of_pizza_and_col(driver)
        logging.info('Сравнение названия выбранных значений с названиями соответствующих товаров в корзине:')
        logging.info('Переход в корзину считываем список выбранных продуктов "bort_list"')
        driver.find_element(By.XPATH, '// li[ @ id = "menu-item-29"] / a[contains(text(), "Корзина")]').click()
        logging.info('Сравнение НАЗВАНИЙ выбранных продуктов с эталоном')
        bort_list = driver.find_elements(By.XPATH, '//dd[@class="variation-"]/p')
        compare_list(1, bort_list, bort_list1)
        logging.info('Сравнение КОЛИЧЕСТВА выбранных значений с количеством соответствующих товаров в корзине')
        count_list = driver.find_elements(By.XPATH, '//input[@type="number"]')
        count1_list = get_attr(count_list)
        compare_list(2, count1_list, col_list1)
        logging.info('Увеличения N-ой  позиции в корзине на 1 шт N: random: от 1 до 3')
        index = random.randrange(1, 3)
        logging.info(f'увеличиваем cтроку - {index}')
        num = driver.find_element(By.CSS_SELECTOR, f'body tr:nth-of-type({index}) td.product-quantity input')
        num.click()
        num.clear()
        logging.info(f"Количество {index} позиции было: {col_list1[index - 1]}")
        col_list1[index - 1] = str(int(col_list1[index - 1]) + 1)
        logging.info(f"Количество {index} позиции стало: {col_list1[index - 1]}")
        num.send_keys(col_list1[index - 1])
        logging.info('Обновление корзины')
        update_cart = driver.find_element(By.NAME, 'update_cart')
        wait.until(EC.element_to_be_clickable(update_cart)).click()
        time.sleep(5)
        elem = driver.find_elements(By.XPATH, '//input[@type="number"]')
        col_pizza = get_attr(elem)
        logging.info(f'Проверка увелечения {index} позиции на 1 шт')
        logging.info(f"Количество считанное из корзины {col_pizza[index - 1]}, rколичество должно быть: {col_list1[index - 1]}")
        logging.info('Удаление N-ой позиции из корзины, N random от 1 до 3: ')
        num = random.randrange(1, 3)
        logging.info(f"удаляем {num} позицию")
        delete_second_line_card = driver.find_element(By.CSS_SELECTOR, f'tbody tr:nth-of-type({num}) td.product-remove a')
        wait.until(EC.element_to_be_clickable(delete_second_line_card)).click()
        time.sleep(5)
        bort_list = driver.find_elements(By.XPATH, '//dd[@class="variation-"]/p')
        if num != 1:
            del bort_list1[num - 2]
        compare_list(1, bort_list, bort_list1)
        time.sleep(5)

    @allure.feature('тест сьют Сайт Pizzeria, flou 1')
    @allure.description('Выбор десерта стоимость которого не более 135 р, добавление в корзину, проверка корзины')
    def test_add_desert(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc")
        logging.info('Переход в меню Десерты, выбираем десерты не более 135 руб:')
        select_list = choose_desert(driver)
        logging.info("Переход в корзину для проверки ее содержимого")
        elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]')
        elem.click()
        basket_list = driver.find_elements(By.XPATH, '//*/td[@data-title="Товар"]')
        logging.info('Проверка списка прокликанных десертов со списком десертов в корзине')
        compare_list(1, basket_list, select_list)
        time.sleep(7)

    @allure.feature('тест сьют Сайт Pizzeria, flou 1')
    @allure.description('Выбор товаров в корзину, переход на страницу авторизации, оформление заказа')
    def test_authorization_making_an_order(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        num = str(random.randrange(1, 999999))
        order_list = ['username', 'lastname', 'Казанская 52 - 64', 'Казань', 'Татарстан', '420000',
                      '78435555555', 'ex' + num + '@inbox.ru']
        logging.info('Открыие сайта Pizzeria')
        driver.get("http://pizzeria.skillbox.cc/")
        time.sleep(5)
        logging.info('Заполнение корзины:')
        push_product_to_card(driver)
        logging.info('Переход к корзину')
        driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]').click()
        sum = driver.find_element(By.XPATH, '//td[@data-title = "Сумма"]//bdi').text
        logging.info('Переход к оплате')
        driver.find_element(By.XPATH, '//a[@class="checkout-button button alt wc-forward"]').click()
        driver.find_element(By.XPATH, '//a[@class="showlogin"]').click()
        logging.info('Переход на вкладку мой аккаунт')
        driver.find_element(By.XPATH, '//a[text() = "Мой аккаунт"]').click()
        logging.info('Процедура регистрации')
        driver.find_element(By.XPATH, '//button[@class="custom-register-button"]').click()
        time.sleep(2)
        user_name = registration(driver, num, order_list)
        logging.info('Проверка регистрации')
        driver.find_element(By.XPATH, '//a[text() = "Мой аккаунт"]').click()
        compare_name = driver.find_element(By.XPATH, '//*/p[contains(text(),"Привет")]/strong')
        assert compare_name.text == user_name
        logging.info('Регистрация прошла успешно!')
        logging.info('Переход к корзину')
        driver.find_element(By.XPATH, '//li[@id = "menu-item-29"]/a[contains(text(), "Корзина")]').click()
        logging.info('Переход к оплате')
        driver.find_element(By.XPATH, '//a[@class="checkout-button button alt wc-forward"]').click()
        logging.info('Ввод реквизитов доставки: Имя, Фамилия, Адрес, Город, Обл, Индекс, Телефон, Дата заказа...')
        date_order = input_reg_form_data(1, driver, order_list)
        date_from_orderlist = driver.find_element(By.XPATH, '//li[@class = "woocommerce-order-overview__date date"]/strong').text
        assert date_order == date_from_orderlist
        logging.info("Проверяем личные данные и сумму заказа в карточке заказа")
        elem = driver.find_element(By.XPATH, '//address')
        total = driver.find_element(By.XPATH, '//th[contains(text(),"Total")]/following::span[1]').text

        time.sleep(1)
        compare_list1(elem, order_list, sum, total)
        time.sleep(10)
