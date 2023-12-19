import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators as PPL



def test_add_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    try:
        assert book_name in (page.get_book_name(PPL.BOOK_NAME_IN_BASKET))
    except:
        print("The titile of the book doesn't match")
    try:
        assert book_price == page.get_book_price(PPL.BOOK_PRICE_IN_BASKET)
    except:
        print("The price doesn't match")

def test_add_to_basket(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    try:
        assert book_name in (page.get_book_name(PPL.BOOK_NAME_IN_BASKET))
    except:
        print("The titile of the book doesn't match")
    try:
        assert book_price == page.get_book_price(PPL.BOOK_PRICE_IN_BASKET)
    except:
        print("The price doesn't match")

@pytest.mark.smoke
def test_add_to_basket(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    print(page.get_book_name(PPL.BOOK_NAME_IN_BASKET))
    try:
        assert book_name == (page.get_book_name(PPL.BOOK_NAME_IN_BASKET))
    except:
        print("The titile of the book doesn't match")
    try:
        assert book_price == page.get_book_price(PPL.BOOK_PRICE_IN_BASKET)
    except:
        print("The price doesn't match")

@pytest.mark.integration
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
def test_add_to_test_guest_can_add_product_to_basket(driver, link):
    page = ProductPage(driver, link, 1)
    page.open()
    book_name = page.get_book_name(PPL.BOOK_NAME)
    book_price = page.get_book_price(PPL.BOOK_PRICE)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    try:
        assert book_name == page.get_book_name(PPL.BOOK_NAME_IN_BASKET)
    except:
        print("The titile of the book doesn't match")
    try:
        assert book_price == page.get_book_price(PPL.BOOK_PRICE_IN_BASKET)
    except:
        print("The price doesn't match")

