import time
import logging
from selenium.webdriver.common.by import By


def validation_phone(driver):
    count = 0
    list_phone_error = ['1', '0123456789', '012345678901', '01234567890123456789', 'AAbb2223698', 'asdvbЧВАКЫВ']
    logging.info("Проверка поля ТЕЛЕФОН, на значения: одна цифра, меньше на 1 диапазона, больше на один диапазона, "
                 "много больше диапазона, вперемешку 11 позиций цифры/буквы, вместо 11 цифр буквы")
    for i in list_phone_error:
        elem_input = driver.find_element(By.XPATH, '//input[@id = "bonus_phone"]')
        elem_input.click()
        elem_input.clear()
        elem_input.send_keys(i)
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//input[@id = "bonus_phone"]')
        color = elem.get_attribute("style")
        if color == 'border-color: red;':
            count += 1
    assert count != 6
    logging.info("Валидация прошла успешно")
    return
