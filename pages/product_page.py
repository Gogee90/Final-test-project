from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    def should_be_right_book_name(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        btn.click()
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        self.solve_quiz_and_get_code()
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_in_basket_name = self.browser.find_element(
            *ProductPageLocators.BOOK_IN_BASKET_NAME
        )
        assert (
            book_name.text == book_in_basket_name.text
        ), f"{book_in_basket_name.text} is not equal to {book_name.text}"

    def should_not_be_success_message_after_adding_item_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        btn.click()
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_not_see_success_message_after_page_open(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def success_message_should_disappear_after_adding_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        btn.click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
