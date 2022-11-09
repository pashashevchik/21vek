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


class Electronics_page(Base):

    ########## Locators ############

    SMART_PHONE_BUTTON_SELECTOR = "//a[@class='cloud-sub__header']"
    SMART_WATCH_BUTTON_SELECTOR = "//a[text()='Умные часы']"

    ########## Action ##############

    def press_smart_phone_catalog(self):
        self.get_element(self.SMART_PHONE_BUTTON_SELECTOR).click()
        print("Press smart phone catalog button")

    def press_smart_watch_catalog(self):
        self.get_element(self.SMART_WATCH_BUTTON_SELECTOR).click()
        print("Press smart watch catalog button")

    ########## Method ##############

    def select_smart_phone(self):
        """ Product selection in the catalog (smartphone)"""

        with allure.step("Select smart phone"):
            Logger.add_start_step(method="select_smart_phone")
            self.press_smart_phone_catalog()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_smart_phone")

    def select_smart_watch(self):
        """ Product selection in the catalog(smartwatch) """

        with allure.step("Select smart watch"):
            Logger.add_start_step(method="select_smart_watch")
            self.press_smart_watch_catalog()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_smart_watch")
