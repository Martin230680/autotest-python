import time
import logging
from selenium.webdriver.common.by import By


def validation_empty(driver):
    elem = driver.find_element(By.XPATH, '//li[@ id = "menu-item-363"]/a[text() = "Бонусная программа"]')
    elem.click()
    time.sleep(5)
    logging.info("Валидация пустых полей")
    elem = driver.find_element(By.XPATH, '//button[@name = "bonus"]')
    elem.click()
    elem = driver.find_element(By.XPATH, '//input[@id = "bonus_username"]')
    color = elem.get_attribute("style")
    assert color == 'border-color: red;'
    elem = driver.find_element(By.XPATH, '//input[@id = "bonus_phone"]')
    color = elem.get_attribute("style")
    assert color == 'border-color: red;'
    logging.info("Проверка пустых полей прошла успешно!")
    return
