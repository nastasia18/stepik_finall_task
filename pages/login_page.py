from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password, browser):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_email.send_keys(email)

        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password)

        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_AGAIN)
        input_password2.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button.click()
