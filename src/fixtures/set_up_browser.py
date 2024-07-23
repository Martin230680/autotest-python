import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
# from seleniumwire.webdriver import Chrome
import logging


@pytest.fixture()
def set_up_browser():
    logging.info('Prepare browser')
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    logging.info('browser has been started')
    yield driver
    driver.quit()
