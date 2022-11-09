import time
import datetime
import allure
import selenium

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Smart_watch_page(Base):

    ########## Locators ############

    FIELD_PRICE_FROM_SELECTOR = "//input[@name='filter[price][from]']"
    FIELD_PRICE_TO_SELECTOR = "//input[@name='filter[price][to]']"
    SHOW_PRODUCT_BUTTON_SELECTOR = "//button[@id='j-filter__btn']"
    ADD_PRODUCT_1_TO_CART_BUTTON = "//form[@data-code='65598584_0']"
    ADD_PRODUCT_2_TO_CART_BUTTON = "//form[@data-code='7512219_0']"
    ADD_PRODUCT_3_TO_CART_BUTTON = "//form[@data-code='7293900_0']"
    CART_BUTTON_SELECTOR = "//span[text()='Корзина']"

    ########## Action ##############

    def fill_field_price_product_from(self, price):
        self.get_element(self.FIELD_PRICE_FROM_SELECTOR).send_keys(price)
        print("Fill price product from field")

    def fill_field_price_product_to(self, price):
        self.get_element(self.FIELD_PRICE_TO_SELECTOR).send_keys(price)
        print("Fill price product to field")

    def press_show_product_button(self):
        self.get_element(self.SHOW_PRODUCT_BUTTON_SELECTOR).click()
        print("Press show product button")

    def press_add_product_1_to_cart_button(self):
        try:
            self.element_is_clickable(self.ADD_PRODUCT_1_TO_CART_BUTTON).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.element_is_clickable(self.ADD_PRODUCT_1_TO_CART_BUTTON).click()
        self.driver.refresh()
        print("Press add product 1 to cart button")

    def press_add_product_2_to_cart_button(self):
        try:
            self.element_is_clickable(self.ADD_PRODUCT_2_TO_CART_BUTTON).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.element_is_clickable(self.ADD_PRODUCT_2_TO_CART_BUTTON).click()
        self.driver.refresh()
        print("Press add product 2 to cart button")

    def press_add_product_3_to_cart_button(self):
        try:
            self.element_is_clickable(self.ADD_PRODUCT_3_TO_CART_BUTTON).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.element_is_clickable(self.ADD_PRODUCT_3_TO_CART_BUTTON).click()
        self.driver.refresh()
        print("Press add product 3 to cart button")

    def press_cart_button(self):
        try:
            self.element_is_clickable(self.CART_BUTTON_SELECTOR).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.element_is_clickable(self.CART_BUTTON_SELECTOR).click()
        print("Press cart button")

        ########## Methods ##############

    def search_and_add_product_to_cart(self):
        with allure.step("Search smart watch and add to cart"):
            Logger.add_start_step(method="search_and_add_product_to_cart")
            self.fill_field_price_product_from(80)
            self.fill_field_price_product_to(200)
            self.press_show_product_button()
            self.press_add_product_1_to_cart_button()
            self.press_add_product_2_to_cart_button()
            self.press_add_product_3_to_cart_button()
            self.press_cart_button()
            Logger.add_end_step(url=self.driver.current_url, method="search_and_add_product_to_cart")
