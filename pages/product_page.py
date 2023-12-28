from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators as PPL
import math

class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        self.driver.find_element(*PPL.ADD_TO_BASKET).click()

    def get_book_name(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text
    
    def get_book_price(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text
    
    def should_be_book_name_in_basket(self, book_name: str):
        assert book_name == self.get_book_name(PPL.BOOK_NAME_IN_BASKET), "The titile of the book doesn't match"
        
    def should_be_book_price_in_the_basket(self, book_price: str):
        assert book_price == self.get_book_price(PPL.BOOK_PRICE_IN_BASKET), "The price doesn't match"



