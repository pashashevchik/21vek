import time
import datetime
import allure
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.mobile_page import Mobile_page

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    ########## Locators ############

    CONFIRM_ORDER_BUTTON_SELECTOR = "//button[@id='j-basket__ok']"
    DELIVERY_ADDRESS_CHECKBOX_SELECTOR = "//*[@id='j-addr-widget']/div[1]/div[2]/label[2]"
    FIELD_STREET_FILL_SELECTOR = "//input[@name='data[addr]']"
    FIELD_ENTRANCE_FILL_SELECTOR = "//input[@name='data[entrance]']"
    FIELD_FLOOR_FILL_SELECTOR = "//input[@name='data[floor]']"
    FIELD_FLAT_FILL_SELECTOR = "//input[@name='data[flat]']"
    PHONE_CHECKBOX_SELECTOR = "//*[@id='j-delivery-info']/div[4]/div/div[2]/label[2]"
    FIELD_PHONE_NUMBER_FILL_SELECTOR = "//input[@name='data[phone]']"
    FIELD_COMMENT_FILL_SELECTOR = "//textarea[@name='data[comment]']"
    DELETE_PRODUCT_BUTTON_SELECTOR = "//a[text()='удалить']"
    SMART_WATCH_1_SELECTOR = "//a[text()='Умные часы Xiaomi Mi Watch 2 Lite BHR5436GL (черный)']"
    SMART_WATCH_2_SELECTOR = "//a[text()='Умные часы Realme Watch 2 / RMW2008 (черный)']"
    SMART_WATCH_3_SELECTOR = "//a[text()='Умные часы BQ Watch 1.1 (черный)']"

    ########## Action ##############

    def press_order_button(self):
        self.driver.execute_script("window.scrollTo(0, 350)")
        self.get_element(self.CONFIRM_ORDER_BUTTON_SELECTOR).click()
        print("Press order button")

    def press_delivery_address_checkbox(self):
        self.get_element(self.DELIVERY_ADDRESS_CHECKBOX_SELECTOR).click()
        print("Press delivery address checkbox")

    def fill_field_street(self, street):
        self.get_element(self.FIELD_STREET_FILL_SELECTOR).clear()
        self.get_element(self.FIELD_STREET_FILL_SELECTOR).send_keys(street)
        print("Fill street field")

    def fill_field_entrance(self, entrance):
        self.get_element(self.FIELD_ENTRANCE_FILL_SELECTOR).clear()
        self.get_element(self.FIELD_ENTRANCE_FILL_SELECTOR).send_keys(entrance)
        print("Fill entrance field")

    def fill_field_floor(self, floor):
        self.get_element(self.FIELD_FLOOR_FILL_SELECTOR).clear()
        self.get_element(self.FIELD_FLOOR_FILL_SELECTOR).send_keys(floor)
        print("Fill floor field")

    def fill_field_flat(self, flat):
        self.get_element(self.FIELD_FLAT_FILL_SELECTOR).clear()
        self.get_element(self.FIELD_FLAT_FILL_SELECTOR).send_keys(flat)
        print("Fill flat field")

    def press_phone_checkbox(self):
        self.get_element(self.PHONE_CHECKBOX_SELECTOR).click()
        print("Press phone checkbox")

    def fill_field_phone_number(self, phone_number):
        self.get_element(self.FIELD_PHONE_NUMBER_FILL_SELECTOR).clear()
        self.get_element(self.FIELD_PHONE_NUMBER_FILL_SELECTOR).send_keys(phone_number)
        print("Fill phone number field")

    def fill_field_comment(self, comment):
        self.get_element(self.FIELD_COMMENT_FILL_SELECTOR).clear()
        self.get_element(self.FIELD_COMMENT_FILL_SELECTOR).send_keys(comment)
        print("Fill comment field")

    def fill_field_info(self):
        self.press_delivery_address_checkbox()
        self.fill_field_street("Партизанский проспект")
        self.fill_field_entrance(22)
        self.fill_field_floor(22)
        self.fill_field_flat(222)
        self.press_phone_checkbox()
        self.fill_field_phone_number("+375 (29) 2223456")
        self.fill_field_comment("Удачного дня!")

    def press_button_delete_product_phone(self):
        self.get_element(self.DELETE_PRODUCT_BUTTON_SELECTOR).click()
        print("Press delete product(smart phone) button")

    def press_button_delete_smart_watch(self):
        try:
            self.get_element(self.DELETE_PRODUCT_BUTTON_SELECTOR).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.get_element(self.DELETE_PRODUCT_BUTTON_SELECTOR).click()
        print("Press delete product (smart watch) button")

    ########## Methods #############

    def product_confirmation(self):
        """ Placing an order, entering information
        (street, entrance, floor, flat, phone number) """

        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.press_order_button()
            self.fill_field_info()
            self.get_screenshot("Confirmation")
            self.press_button_delete_product_phone()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")

    def assert_smart_watch_in_cart(self):
        """ Сhecking and Assert the product (by name) in the cart """

        with allure.step("assert smart watch in cart"):
            Logger.add_start_step(method="assert_smart_watch_in_cart")
            self.get_screenshot("Smart_watch_in_cart")
            self.assert_word(self.get_element(self.SMART_WATCH_1_SELECTOR),
                             "Умные часы Xiaomi Mi Watch 2 Lite BHR5436GL (черный)",
                             print_name="Value name smart watch 1 right")
            self.assert_word(self.get_element(self.SMART_WATCH_2_SELECTOR),
                             "Умные часы Realme Watch 2 / RMW2008 (черный)",
                             print_name="Value name smart watch 2 right")
            self.assert_word(self.get_element(self.SMART_WATCH_3_SELECTOR), "Умные часы BQ Watch 1.1 (черный)",
                             print_name="Value name smart watch 3 right")
            self.press_button_delete_smart_watch()
            self.press_button_delete_smart_watch()
            self.press_button_delete_smart_watch()
            Logger.add_end_step(url=self.driver.current_url, method="assert_smart_watch_in_cart")
