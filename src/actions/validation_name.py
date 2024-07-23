import time
import logging
from selenium.webdriver.common.by import By


def validation_name(driver):
    list_errors = []
    count = 0
    list_name_error = [' ', 'Проверка длины строки Проверка длины строки', 'MartinМартин', '~@#$%^&*', 'éèêëîïôûùüÿN'
                                                                                                       'ÑOéàòù의中国的日本の']
    logging.info("Проверка поля ИМЯ, на значения: Пробел, Длинное ИМЯ, Разные языки, Спецсимволы и Иероглифы")
    for i in list_name_error:
        elem_input = driver.find_element(By.XPATH, '//input[@id = "bonus_username"]')
        elem_input.click()
        elem_input.clear()
        elem_input.send_keys(i)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, '//button[@name = "bonus"]')
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//input[@id = "bonus_username"]')
        color = elem.get_attribute("style")
        if color != 'border-color: red;':
            list_errors.append('0')
            count += 1
    assert count == 0
    return
