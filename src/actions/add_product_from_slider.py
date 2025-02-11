import time
import logging
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from src.actions.chenche_char import chenche_char
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_product_from_slider(driver):
    select_list = []
    wait = WebDriverWait(driver, timeout=10)
    logging.info('Добавление крайнего левого товара из открытого слайдера в корзину')
    elem = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(5) a.add_to_cart_button ')
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
    item = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(5) a h3')
    logging.info('замена >> на " в названии товара')
    remove_item_text = chenche_char(item, ["«", "»"])
    logging.info('добавление элемента в эталонный список для сравнения со списком формируемый в корзине')
    select_list.append(remove_item_text)
    logging.info('Добавление 3 элемента из открытого слайдера в корзину')
    elem = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(7) a.add_to_cart_button ')
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
    item = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(7) a h3')
    logging.info('замена >> на " в названии товара')
    remove_item_text = chenche_char(item, ["«", "»"])
    logging.info('добавление элемента в эталонный список для сравнения со списком формируемый в корзине')
    select_list.append(remove_item_text)
    logging.info('Прокрутка сладера на 1 клика вправо, добавление в корзину крайнего правого товара')
    next_but = driver.find_element(By.CSS_SELECTOR, 'a.slick-next')
    next_but.click()
    time.sleep(1)
    logging.info('Добавление крайнего правого товара из открытого слайдера в корзину')
    elem = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(9) a.add_to_cart_button ')
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
    logging.info('замена >> на " в названии товара')
    item = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(9) a h3')
    remove_item_text = chenche_char(item, ["«", "»"])
    logging.info('добавление элемента в эталонный список для сравнения со списком формируемый в корзине')
    select_list.append(remove_item_text)
    logging.info('Прокрутка сладера на 3 клика влево, добавление в корзину крайнего левого товара')
    prev_but = driver.find_element(By.CSS_SELECTOR, 'a.slick-prev')
    prev_but.click()
    time.sleep(1)
    prev_but.click()
    time.sleep(1)
    prev_but.click()
    time.sleep(1)
    elem = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(8) a.add_to_cart_button ')
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
    logging.info('замена >> на " в названии товара')
    item = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(8) a h3')
    remove_item_text = chenche_char(item, ["«", "»"])
    logging.info('добавление элемента в эталонный список для сравнения со списком формируемый в корзине')
    select_list.append(remove_item_text)
    time.sleep(2)
    return (select_list)
