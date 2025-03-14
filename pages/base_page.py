import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)  # Logeri stextsum

    def open(self, url):
        self.logger.info(f" Open page: {url}")
        self.driver.get(url)
        time.sleep(1)

    def find_element(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f" Element found {locator}")
            return element
        except Exception as e:
            self.logger.error(f" Element search error {locator}: {e}")
            return None

    def click_element(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()
            self.logger.info(f" Clicking on an element {locator}")

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            self.logger.info(f" The text is entered in {locator}: {text}")

    def get_text(self, locator):
        element = self.find_element(locator)
        if element:
            text = element.text
            self.logger.info(f"Text received: {text}")
            return text
        return None
