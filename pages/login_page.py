from pages.locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print(self.browser.current_url)
        assert (
            "login" in self.browser.current_url
        ), 'The url should contain "login" word'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTARTION_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)

        register_email.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        register_btn.click()
