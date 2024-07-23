import time
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.actions.chenche_char import chenche_char
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def choose_desert(driver):
    select_list = []
    action_chains = ActionChains(driver)
    wait = WebDriverWait(driver, timeout=10)
    elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-389"]')
    action_chains.move_to_element(elem).perform()
    elem = driver.find_element(By.XPATH, '//li[@id = "menu-item-391"]/a')
    action_chains.move_to_element(elem).perform()
    elem.click()
    time.sleep(3)
    logging.info('Задаем диапазон цен для десертов не более 135 р, нажимаем "Применить"')
    elem2 = driver.find_element(By.XPATH, '//span[@style="left: 100%;"]')
    action_chains = ActionChains(driver)
    action_chains.click_and_hold(elem2).move_by_offset(xoffset=-200, yoffset=0).perform()
    action_chains.release().perform()
    elem = driver.find_element(By.XPATH, '// button[text() = "Применить"]')
    elem.click()
    time.sleep(3)
    logging.info('Помещаем двух десертов с id 437 и 433 в корзину')
    elem = driver.find_element(By.XPATH, '//a[text()="В корзину"] [@data-product_id="437"]')
    wait.until(EC.element_to_be_clickable(elem)).click()
    item = driver.find_element(By.XPATH,
                               '//a[@data-product_id="437"]/ancestor::div[@class="collection_desc clearfix"]//h3')
    logging.info('Замена символов "«", "»" на в названиb десертa с id 437')
    remove_item_text = chenche_char(item, ["«", "»"])
    logging.info("Добавляем элемент к эталонному списку прокликанных элементов")
    select_list.append(remove_item_text)
    time.sleep(1)
    elem = driver.find_element(By.XPATH, '//a[text()="В корзину"] [@data-product_id="433"]')
    wait.until(EC.element_to_be_clickable(elem)).click()
    item = driver.find_element(By.XPATH,
                               '//a[@data-product_id="433"]/ancestor::div[@class="collection_desc clearfix"]//h3')
    logging.info('Замена символов "«", "»" на в названиb десертa с id 433')
    remove_item_text = chenche_char(item, ["«", "»"])
    logging.info("Добавляем элемент к эталонному списку прокликанных элементов")
    select_list.append(remove_item_text)
    time.sleep(1)
    return select_list
