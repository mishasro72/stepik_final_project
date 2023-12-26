from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, "//a[@class = 'btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
   # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    NO_SUCH_ELEMENT = (By.CSS_SELECTOR, "#login_link_1") # для проверки негатвного теста - отсутсвия элемента на странице 
    BASKET_BUTTON = (By.XPATH, "//a[@class = 'btn btn-default']")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_LOGIN_FIELD = (By.XPATH, "//input[@name='registration-email']")
    REG_PASSWORD= (By.XPATH, "//input[@name='registration-password1']")
    REG_CONFIRM_PASSWORD= (By.XPATH, "//input[@name='registration-password2']")
    RETISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/h1")
    BOOK_PRICE = (By.XPATH, "//div[@class = 'col-sm-6 product_main']/p[1]")
    BOOK_NAME_IN_BASKET = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-success  fade in'][1]/div[@class = 'alertinner ']/strong")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@class = 'alert alert-safe alert-noicon alert-info  fade in']/div[@class = 'alertinner ']/p/strong")

class BasketPageLocators():
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[@class = 'btn btn-lg btn-primary btn-block']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")

