import pytest
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = "no", help = 'Choose your language')


@pytest.fixture
def chrome_opt(request):
    language = request.config.getoption('--language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages' : language})
    options.add_argument('--headless')
    return options

@pytest.fixture
def driver(chrome_opt):
    print("\n Start testing")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    print("\n End testing")
    driver.quit()





