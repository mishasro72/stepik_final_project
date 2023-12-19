from .base_page import BasePage  
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import MainPageLocators as MPL
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException



class MainPage(BasePage):
    
    def should_be_login_link(self):
        assert self.is_element_present(MPL.LOGIN_LINK), "Login link is not present"

    def go_to_login_page(self):
        self.driver.find_element(*MPL.LOGIN_LINK).click()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No alert is present")


