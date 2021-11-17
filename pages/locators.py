from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTARTION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD1 = (By.NAME, "registration-password1")
    PASSWORD2 = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BOOK_NAME = (By.TAG_NAME, "h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
