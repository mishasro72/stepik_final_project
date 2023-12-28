from .base_page import BasePage
from .locators import LoginPageLocators as LPL
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.fill_the_field(LPL.REG_LOGIN_FIELD, email)
        self.fill_the_field(LPL.REG_PASSWORD, password)
        self.fill_the_field(LPL.REG_CONFIRM_PASSWORD, password)
        self.click_button(LPL.RETISTER_BUTTON)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, "Подстроки login нет в текущем url браузера"

    def should_be_login_form(self):
        assert self.is_element_present(LPL.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(LPL.REGISTER_FORM), "Register form is not present"

