import logging
import time
from selenium.webdriver.common.by import By


def authorization(driver):
    logging.info("Ввод имя в форме авторизации: tututu")
    elem = driver.find_element(By.XPATH, '//input[@id = "username"]')
    elem.click()
    elem.send_keys('tututu')
    logging.info("Ввод пароля в форме авторизации: tututu123456")
    elem = driver.find_element(By.XPATH, '//input[@id = "password"]')
    elem.click()
    elem.send_keys('tututu123456')
    logging.info("Нажатие кнопки ВХОД")
    driver.find_element(By.XPATH, '//button[@name ="login"]').click()
    time.sleep(5)
    return
