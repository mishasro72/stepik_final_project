import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
    #time.sleep(3)
