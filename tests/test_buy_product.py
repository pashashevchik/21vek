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


@allure.description("Test buy product(smartphone)")
def test_buy_product():
    """ Smoke test, authorization and choice to the desired catalog,
    application of filters, selection and purchase of product """

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    print("Start test")

    """ User authorization with valid data"""
    Login_page(driver).authorization()

    """ Select the desired directory """
    Main_page(driver).select_catalog()

    """ Select product(smartphone) """
    Electronics_page(driver).select_smart_phone()

    """ Search product(smartphone), apply filters and add it to the cart """
    Mobile_page(driver).search_smart_phone()

    """ Ordering product """
    Cart_page(driver).product_confirmation()

    print("Finish Test")

    driver.quit()
