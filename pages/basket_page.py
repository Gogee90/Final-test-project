from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS)

    def should_be_text_that_basket_is_not_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY_TEXT)
