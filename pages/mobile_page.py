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


class Mobile_page(Base):

    ########## Locators ############

    FIELD_PRICE_FROM_SELECTOR = "//input[@name='filter[price][from]']"
    FIELD_PRICE_TO_SELECTOR = "//input[@name='filter[price][to]']"
    MANUFACTURER_FILTER_CHECKBOX_SELECTOR = "//label[@title='Apple']"
    TYPE_FILTER_CHECKBOX_SELECTOR = "//span[text()='Тип']"
    TYPE_VALUE_CHECKBOX_SELECTOR = "//a[text()='смартфон']"
    RAM_FILTER_CHECKBOX_SELECTOR = "//*[@id='j-filter__form']/div[4]/dl[9]/dt/span[1]"
    VALUE_RAM_CHECKBOX_SELECTOR = "//label[@title='4 Гб']"
    VERSION_FILTER_CHECKBOX_SELECTOR = "//span[text()='Версия операционной системы']"
    VALUE_VERSION_CHECKBOX_SELECTOR = "//label[text()='iOS 14']"
    COLOR_FILTER_CHECKBOX_SELECTOR = "//span[text()='Цвет']"
    ALL_COLORS_BUTTON_SELECTOR = "//*[@id='j-filter__form']/div[4]/dl[20]/dd/span"
    VALUE_COLOR_CHECKBOX_SELECTOR = "//label[@title='черный']"
    SHOW_PRODUCT_BUTTON_SELECTOR = "//button[@id='j-filter__btn']"
    ADD_TO_CART_BUTTON_SELECTOR = "//form[@data-code='6270080_0']"
    CART_BUTTON_SELECTOR = "//span[text()='Корзина']"

    ########## Action ##############

    def fill_field_price_from(self, price):
        self.get_element(self.FIELD_PRICE_FROM_SELECTOR).send_keys(price)
        print("Fill price phone from field")

    def fill_field_price_to(self, price):
        self.get_element(self.FIELD_PRICE_TO_SELECTOR).send_keys(price)
        print("Fill price phone to field")

    def press_manufacturer_filter_checkbox(self):
        self.get_element(self.MANUFACTURER_FILTER_CHECKBOX_SELECTOR).click()
        print("Press manufacturer filter checkbox")

    def press_type_filter_checkbox(self):
        self.get_element(self.TYPE_FILTER_CHECKBOX_SELECTOR).click()
        print("Press type filter checkbox")

    def press_value_type_checkbox(self):
        self.get_element(self.TYPE_VALUE_CHECKBOX_SELECTOR).click()
        print("Press value type checkbox")

    def press_ram_filter_checkbox(self):
        self.driver.execute_script("arguments[0].click();", self.get_element(self.RAM_FILTER_CHECKBOX_SELECTOR))
        print("Press ram filter checkbox")

    def press_value_ram_checkbox(self):
        self.go_to_element(self.get_element(self.VALUE_RAM_CHECKBOX_SELECTOR))
        self.get_element(self.VALUE_RAM_CHECKBOX_SELECTOR).click()
        print("Press value ram checkbox")

    def press_version_filter_checkbox(self):
        self.get_element(self.VERSION_FILTER_CHECKBOX_SELECTOR).click()
        print("Press version filter checkbox")

    def press_value_version_checkbox(self):
        self.get_element(self.VALUE_VERSION_CHECKBOX_SELECTOR).click()
        print("Press value version checkbox")

    def press_color_filter_checkbox(self):
        self.get_element(self.COLOR_FILTER_CHECKBOX_SELECTOR).click()
        print("Press color filter checkbox")

    def press_all_color_checkbox(self):
        self.go_to_element(self.get_element(self.ALL_COLORS_BUTTON_SELECTOR))
        self.driver.execute_script("arguments[0].click();", self.get_element(self.ALL_COLORS_BUTTON_SELECTOR))
        print("Press all color button")

    def press_value_color(self):
        self.element_is_clickable(self.VALUE_COLOR_CHECKBOX_SELECTOR).click()
        print("Press value color checkbox")

    def press_show_product_button(self):
        self.get_element(self.SHOW_PRODUCT_BUTTON_SELECTOR).click()
        print("Press show product button")

    def press_add_to_cart_button(self):
        self.get_element(self.ADD_TO_CART_BUTTON_SELECTOR).click()
        self.driver.refresh()
        print("Press add product to cart button")

    def press_cart_button(self):
        try:
            self.get_element(self.CART_BUTTON_SELECTOR).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.get_element(self.CART_BUTTON_SELECTOR).click()
        print("Press cart button")

    # Methods

    def search_smart_phone(self):
        """ Search for a product(smartphone), apply filters (price, manufacturer,
        RAM, operating system version and color), apply filters and select a product,
        add it to the cart."""

        with allure.step("Search smart phone"):
            Logger.add_start_step(method="search_smart_phone")
            self.fill_field_price_from(500)
            self.fill_field_price_to(2000)
            self.press_manufacturer_filter_checkbox()
            self.press_type_filter_checkbox()
            self.press_value_type_checkbox()
            self.press_ram_filter_checkbox()
            self.press_value_ram_checkbox()
            self.press_version_filter_checkbox()
            self.press_value_version_checkbox()
            self.press_color_filter_checkbox()
            self.press_all_color_checkbox()
            self.press_value_color()
            self.press_show_product_button()
            self.press_add_to_cart_button()
            self.press_cart_button()
            self.get_screenshot('product_in_cart')
            Logger.add_end_step(url=self.driver.current_url, method="search_smart_phone")
