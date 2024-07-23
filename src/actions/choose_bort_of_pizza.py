import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def choose_bort_of_pizza_and_col(driver):
    col_list = []
    bort_list = []
    wait = WebDriverWait(driver, timeout=10)
    logging.info('Выбор борта - обычный')
    elem = driver.find_element(By.XPATH, '//input[@type="number"]')
    elem.click()
    elem.clear()
    logging.info('Устанавливаем количество пиц с обычным бортом (random от 1 до 5)')
    num = str(random.randrange(1, 5))
    elem.send_keys(num)
    col_list.append(num)
    elem = driver.find_element(By.XPATH, '// button[ @ name = "add-to-cart"]')
    elem.click()
    logging.info('Выбор борта - сырный')
    elem = driver.find_element(By.XPATH, '// select[ @ id = "board_pack"]')
    wait.until(EC.element_to_be_clickable(elem)).click()
    elem = driver.find_element(By.XPATH, '//option[contains(text(),"Сырный - 55.00 р.")]')
    if elem.text == "Сырный - 55.00 р.":
        bort_list.append('Сырный борт')
    wait.until(EC.element_to_be_clickable(elem)).click()
    time.sleep(4)
    elem = driver.find_element(By.XPATH, '//input[@type="number"]')
    elem.click()
    elem.clear()
    logging.info('Устанавливаем количество пиц с сырным бортом (random от 1 до 5)')
    num = str(random.randrange(1, 5))
    elem.send_keys(num)
    col_list.append(num)
    elem = driver.find_element(By.XPATH, '// button[ @ name = "add-to-cart"]')
    elem.click()
    logging.info('Выбор борта - колбасный')
    elem = driver.find_element(By.XPATH, '//option[contains(text(),"Колбасный - 65.00 р.")]')
    if elem.text == "Колбасный - 65.00 р.":
        bort_list.append('Колбасный борт')
    wait.until(EC.element_to_be_clickable(elem)).click()
    elem = driver.find_element(By.XPATH, '//input[@type="number"]')
    elem.click()
    elem.clear()
    logging.info('Устанавливаем количество пиц с колбасным бортом (random от 1 до 5)')
    num = str(random.randrange(1, 5))
    elem.send_keys(num)
    col_list.append(num)
    elem = driver.find_element(By.XPATH, '// button[@name = "add-to-cart"]')
    elem.click()
    return (bort_list, col_list)
