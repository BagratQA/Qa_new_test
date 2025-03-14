import pytest
import logging

from New_Test.pages.home_page import HomePage
from New_Test.pages.login_page import LoginPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("username, password, expected_error", [
    ("wronguser", "wrongpassword", "Your username is invalid!"),
    ("student", "wrongpassword", "Your password is invalid!"),
    ("wronguser", "Password123", "Your username is invalid!"),
    ("", "Password123", "Your username is invalid!"),
    ("student", "", "Your password is invalid!")
])
def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.login(username, password)

    assert login_page.get_error_message() == expected_error, "Your username is invalid!"

def test_valid_login(driver):
# stugum chisht daninerov mutqi
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.login("student", "Password123")

    assert login_page.get_success_message() == "Logged In Successfully", "Login failed!"


def test_logout(driver):
#stugum durs gal
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open("https://practicetestautomation.com/practice-test-login/")
    login_page.login("student", "Password123")

    home_page.logout()

    assert login_page.get_text(("tag name", "h2")) == "Test login", "Exit failed!"
