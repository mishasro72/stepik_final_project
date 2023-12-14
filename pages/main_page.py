from .base_page import BasePage  
from selenium import webdriver
from selenium.webdriver.common.by import By



class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
