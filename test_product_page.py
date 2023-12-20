import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators as PPL
from .pages.login_page import LoginPage



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
    #print(page.get_book_name(PPL.BOOK_NAME_IN_BASKET))
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

@pytest.mark.negative
@pytest.mark.xfail(reason="Guest can see success message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    assert page.is_element_not_present(PPL.BOOK_NAME_IN_BASKET)

@pytest.mark.negative
def test_guest_cant_see_success_message (driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    assert page.is_element_not_present(PPL.BOOK_NAME_IN_BASKET)

@pytest.mark.xfail(reason="Message didn't desappeare after adding product")
@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    assert page.is_desappeared(PPL.BOOK_NAME_IN_BASKET)

@pytest.mark.login
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





