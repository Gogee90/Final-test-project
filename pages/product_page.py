from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        btn.click()
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        self.solve_quiz_and_get_code()
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_in_basket_name = self.browser.find_element(
            *ProductPageLocators.BOOK_IN_BASKET_NAME
        )
        assert book_name.text == book_in_basket_name.text, f"{book_in_basket_name.text}"
