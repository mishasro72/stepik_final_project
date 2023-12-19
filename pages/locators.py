from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    BOOK_PRICE = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/p[1]")
    BOOK_NAME_IN_BASKET = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-success  fade in'][1]/div[@class = 'alertinner ']/strong")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-info  fade in']/div[@class = 'alertinner ']/p/strong")

