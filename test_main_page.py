import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators as LPL

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.negative
def test_guest_can_see_login_link(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    #link = "http://selenium1py.pythonanywhere.com/"
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
    page.should_be_login_form

@pytest.mark.login
def test_register_form_present(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
   # link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = LoginPage(driver, link, 1)
    page.open()
    page.should_be_register_form()


