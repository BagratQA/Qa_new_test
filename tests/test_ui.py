import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


@pytest.mark.usefixtures("driver")
class TestUI:
    def test_login_page_elements(self, driver):
        """Проверяем, что все ключевые элементы есть на странице логина"""
        driver.get("https://practicetestautomation.com/practice-test-login/")

        assert driver.find_element(By.ID, "username").is_displayed(), "Поле Username отсутствует!"
        assert driver.find_element(By.ID, "password").is_displayed(), "Поле Password отсутствует!"
        assert driver.find_element(By.ID, "submit").is_displayed(), "Кнопка Login отсутствует!"
        assert driver.find_element(By.TAG_NAME, "h2").text == "Test login", "Текст заголовка некорректен!"
