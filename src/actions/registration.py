
import logging
from selenium.webdriver.common.by import By


def registration(driver, num, order_list):
    elem_name = driver.find_element(By.XPATH, '//input[@id = "reg_username"]')
    elem_name.click()
    user_name = 'ex' + num
    elem_name.send_keys(user_name)
    logging.info(f'user_name = {user_name}')
    elem = driver.find_element(By.XPATH, '//input[@id = "reg_email"]')
    elem.click()
    elem.send_keys(order_list[7])
    elem = driver.find_element(By.XPATH, '//input[@id = "reg_password"]')
    elem.click()
    logging.info(f'password = {num}')
    elem.send_keys(num)
    elem = driver.find_element(By.XPATH, '// button[ @ name = "register"]')
    elem.click()
    return user_name
