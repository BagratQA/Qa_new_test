from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def login(self, username, password):
        self.enter_text(LoginPageLocators.USERNAME, username)
        self.enter_text(LoginPageLocators.PASSWORD, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def get_success_message(self):
        return self.get_text(LoginPageLocators.SUCCESS_MESSAGE)

    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)
