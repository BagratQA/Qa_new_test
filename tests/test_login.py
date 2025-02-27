from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.login("student", "Password123")

    assert login_page.get_success_message() == "Logged In Successfully", "Login failed!"


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.login("wronguser", "wrongpassword")

    assert login_page.get_error_message() == "Your username is invalid!", "Error message is incorrect!"


def test_logout(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open("https://practicetestautomation.com/practice-test-login/")
    login_page.login("student", "Password123")

    home_page.logout()

    assert login_page.get_text(("tag name", "h2")) == "Test login", "Logout failed!"
