from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def push_to_card_from_slider(driver):
    wait = WebDriverWait(driver, timeout=10)
    elem = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(5) a.add_to_cart_button ')
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
    elem = driver.find_element(By.CSS_SELECTOR, 'ul.new-prod-slide li:nth-of-type(8) a.add_to_cart_button ')
    ActionChains(driver).move_to_element(elem).perform()
    wait.until(EC.element_to_be_clickable(elem)).click()
