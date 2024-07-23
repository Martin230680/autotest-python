from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def primenenie_kupona(driver, wait, kupon):
    elem = driver.find_element(By.XPATH, '//input[@id = "coupon_code"]')
    wait.until(EC.element_to_be_clickable(elem)).click()
    elem.send_keys(kupon)
    elem = driver.find_element(By.XPATH, '//button[@name="apply_coupon"]')
    wait.until(EC.element_to_be_clickable(elem)).click()
