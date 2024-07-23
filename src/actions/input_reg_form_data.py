import logging
import time
from selenium.webdriver.common.by import By
from datetime import timedelta, date


def input_reg_form_data(flag, driver, order_list):
    username = driver.find_element(By.XPATH, '//input[@id = "billing_first_name"]')
    username.click()
    username.send_keys(order_list[0])
    lastname = driver.find_element(By.XPATH, '//input[@id = "billing_last_name"]')
    lastname.click()
    lastname.send_keys(order_list[1])
    adress = driver.find_element(By.XPATH, '//input[@id = "billing_address_1"]')
    adress.click()
    adress.send_keys(order_list[2])
    city = driver.find_element(By.XPATH, '//input[@id = "billing_city"]')
    city.click()
    city.send_keys(order_list[3])
    obl = driver.find_element(By.XPATH, '//input[@id = "billing_state"]')
    obl.click()
    obl.send_keys(order_list[4])
    postcode = driver.find_element(By.XPATH, '//input[@id = "billing_postcode"]')
    postcode.click()
    postcode.send_keys(order_list[5])
    phone = driver.find_element(By.XPATH, '//input[@id = "billing_phone"]')
    phone.click()
    phone.send_keys(order_list[6])
    radio = driver.find_element(By.XPATH, '//*/label[contains(text(),"Оплата при")]')
    radio.click()
    today = date.today()
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%d.%m.%Y")
    date_input = driver.find_element(By.XPATH, '//input[@id="order_date"]')
    date_input.click()
    date_input.clear()
    date_input.send_keys(tomorrow_str)
    check = driver.find_element(By.CSS_SELECTOR, 'label.woocommerce-form__label.woocommerce-form__label-for-checkbox.checkbox')
    check.click()
    if flag == 2:
        elem = driver.find_element(By.XPATH, '//textarea[@id = "order_comments"]')
        elem.click()
        elem.send_keys(order_list[6])
    logging.info("Нажимаем кнопку подтвердить заказ")
    elem = driver.find_element(By.XPATH, '//button[@id = "place_order"]')
    elem.click()
    time.sleep(10)
    return tomorrow_str
