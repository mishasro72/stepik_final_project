from .base_page import BasePage  
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators as MPL
from .login_page import LoginPage



class MainPage(BasePage):

    # def go_to_login_page(self):
    #     login_link = self.driver.find_element(*MPL.LOGIN_LINK)
    #     login_link.click()
    
    def should_be_login_link(self):
        assert self.is_element_present(MPL.LOGIN_LINK), "Login link is not present"

    def go_to_login_page(self):
        self.driver.find_element(*MPL.LOGIN_LINK).click()


