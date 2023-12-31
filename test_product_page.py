import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators as PPL
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_add_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_book_name_in_basket(book_name)
    page.should_be_book_price_in_the_basket(book_price)

def test_add_to_basket_NY2019(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_book_name_in_basket(book_name)
    page.should_be_book_price_in_the_basket(book_price)

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason = "link has a bug")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(driver, link):
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_book_name_in_basket(book_name)
    page.should_be_book_price_in_the_basket(book_price)

@pytest.mark.negative
@pytest.mark.xfail(reason="Guest can see success message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message(PPL.BOOK_NAME_IN_BASKET)

@pytest.mark.negative
def test_guest_cant_see_success_message (driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message(PPL.BOOK_NAME_IN_BASKET)

@pytest.mark.xfail(reason="Message didn't desappeare after adding product")
@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    time.sleep(3)
    page.should_be_disappeared(PPL.BOOK_NAME_IN_BASKET)

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()

@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(driver, driver.current_url)
    page.check_basket_empty()
    page.check_basket_empty_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture (scope='function', autouse=True)
    def setup(self, driver):
        email = str(time.time()) + "@fakemail.org"
        password = "1324528Qw"
        link = "http://selenium1py.pythonanywhere.com/"
        user_page = LoginPage(driver, link)
        user_page.open()
        user_page.go_to_login_page()
        user_page.register_new_user(email, password)
        user_page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(driver, link)
        page.open()
        book_name = page.get_book_name(PPL.BOOK_NAME)
        book_price = page.get_book_price(PPL.BOOK_PRICE)
        page.add_to_basket()
        page.should_be_book_name_in_basket(book_name)
        page.should_be_book_price_in_the_basket(book_price)

    def test_user_cant_see_success_message (self, driver):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(driver, link, 1)
        page.open()
        page.should_not_be_success_message(PPL.BOOK_NAME_IN_BASKET)
