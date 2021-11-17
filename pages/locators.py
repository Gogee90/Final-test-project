from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTARTION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BOOK_NAME = (By.TAG_NAME, "h1")
