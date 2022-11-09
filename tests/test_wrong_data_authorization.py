import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.electronics_page import Electronics_page
from pages.mobile_page import Mobile_page
from pages.cart_page import Cart_page


@allure.description("Test input wrong data authorization")
def test_wrong_data_authorization():
    """ Authorization test with invalid characters"""

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    print("Start test")

    """ User Authorization with invalid data"""
    Login_page(driver).wrong_data_authorization()

    print("Finish test")

    driver.quit()
