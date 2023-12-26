from .base_page import BasePage
from .locators import BasketPageLocators as BasketPL

class BasketPage(BasePage):

    def check_basket_empty(self):
        assert self.is_element_not_present(BasketPL.PROCEED_TO_CHECKOUT, 1)

    def check_basket_empty_message(self):
        assert "Your basket is empty" in self.get_text(BasketPL.EMPTY_BASKET_MESSAGE)




