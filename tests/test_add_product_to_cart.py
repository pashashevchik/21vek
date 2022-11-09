import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.electronics_page import Electronics_page
from pages.smart_watch_page import Smart_watch_page
from pages.cart_page import Cart_page


@allure.description("Test add product to cart")
def test_add_product_to_cart():
    """ Critical path test, authorization and choice to the desired catalog
    select product(smartwatch) and add in to the cart """

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    print("Start Test")

    """ User Authorization with valid data """
    Login_page(driver).authorization()

    """ Select the desired directory """
    Main_page(driver).select_catalog()

    """ Select product(smartwatch) """
    Electronics_page(driver).select_smart_watch()

    """ Search product(smartwatch), apply filters and add it to the cart """
    Smart_watch_page(driver).search_and_add_product_to_cart()

    """ Check product(smartwatch) in cart"""
    Cart_page(driver).assert_smart_watch_in_cart()

    print("Finish Test")

    driver.quit()

