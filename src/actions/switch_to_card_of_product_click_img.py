import time
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def switch_to_card_of_product_click_img(driver):
    assert_list = []
    wait = WebDriverWait(driver, timeout=10)
    logging.info('Переход на карточку товара из слайдера "Пицца «4 в 1»", клик на изображении слайдера')
    elem = driver.find_element(By.XPATH, '//li[@data-slick-index="0"]/div/a[@title="Пицца «4 в 1»"]')
    elem2 = elem.get_attribute("title")
    assert_list.append(elem2)
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
    elem3 = driver.find_element(By.CSS_SELECTOR, 'h1.product_title').text
    assert_list.append(elem3)
    logging.info('Переход на главную страницу')
    driver.find_element(By.XPATH, '//li[@id="menu-item-26"]/a[contains(text(),"Главная")]').click()
    time.sleep(5)
    logging.info('Переход на карточку товара из слайдера "Пицца «Рай»", клик на изображении слайдера')
    elem4 = driver.find_element(By.XPATH, '//li[@data-slick-index="2"]/div/a[@title="Пицца «Рай»"]')
    elem5 = elem4.get_attribute("title")
    assert_list.append(elem5)
    ActionChains(driver).move_to_element(elem4).perform()
    wait.until(EC.element_to_be_clickable(elem4)).click()
    elem6 = driver.find_element(By.CSS_SELECTOR, 'h1.product_title').text
    assert_list.append(elem6)
    return assert_list
