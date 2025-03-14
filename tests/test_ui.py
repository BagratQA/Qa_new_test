import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pages.base_page



@pytest.mark.usefixtures("driver")
class TestUI:
    def test_login_page_elements(self, driver):
      #stugum enq wor bolor himnakan elementnery glxavor ejum logini arkaya
        driver.get("https://practicetestautomation.com/practice-test-login/")

        assert driver.find_element(By.ID, "username").is_displayed(), "Your username is invalid!"
        assert driver.find_element(By.ID, "password").is_displayed(), "Your password is invalid!"
        assert driver.find_element(By.ID, "submit").is_displayed(), "The Login button is missing!"
        assert driver.find_element(By.TAG_NAME, "h2").text == "Test login", "The title text is incorrect!"
