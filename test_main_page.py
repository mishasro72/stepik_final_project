import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import LoginPageLocators as LPL
from .pages.locators import MainPageLocators as MPL
from .pages.locators import BasePageLocators as BPL

@pytest.mark.main
def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


@pytest.mark.main
def test_guest_can_see_login_link(driver):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link, 1)
    page.open()
    page.should_be_login_link()

@pytest.mark.login
def test_login_url(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = LoginPage(driver, link, 1)
    page.open()
    page.should_be_login_url()

@pytest.mark.login
def test_login_form_present(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
   # link = "hhttp://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = LoginPage(driver, link, 1)
    page.open()
    print(page.is_element_present(LPL.REGISTER_FORM))
    page.should_be_login_form()

@pytest.mark.login
def test_register_form_present(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
   # link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = LoginPage(driver, link, 1)
    page.open()
    page.should_be_register_form()

@pytest.mark.negative
def test_no_message(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = MainPage(driver, link, 1)
    page.open()
    page.should_not_be_success_message(MPL.NO_SUCH_ELEMENT)

@pytest.mark.basket   
def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(driver, driver.current_url)
    page.check_basket_empty()
    page.check_basket_empty_message()
    




