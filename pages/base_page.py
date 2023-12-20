from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import BasePageLocators as BPL
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

class BasePage():

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def go_to_login_page(self):
        self.driver.find_element(*BPL.LOGIN_LINK).click()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No alert is present")
    
    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, locator: tuple):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
    
    def is_element_not_present(self, locator: tuple, timeout = 4):
        try:
            wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return True
        return False    
    
    def is_desappeared (self, locator: tuple, timeout = 4):
        try:
            wait(self.driver, timeout).until_not(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True 
    
    def should_be_login_link(self):
        assert self.is_element_present(BPL.LOGIN_LINK), "Login link is not present"

    def should_not_be_success_message(self, locator: tuple):
        assert  self.is_element_not_present(locator), "The massage is present, but should not be"
   
    @property
    def current_url(self) -> str:
        return self.driver.current_url
    

    
