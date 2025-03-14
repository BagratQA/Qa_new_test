from New_Test.pages.base_page import BasePage
from New_Test.pages.locators import HomePageLocators


class HomePage(BasePage):
    def logout(self):
        self.click_element(HomePageLocators.LOGOUT_BUTTON)
