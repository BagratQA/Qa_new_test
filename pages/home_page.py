from pages.base_page import BasePage
from pages.locators import HomePageLocators

class HomePage(BasePage):
    def logout(self):
        self.click_element(HomePageLocators.LOGOUT_BUTTON)
