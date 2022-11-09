import time
import datetime
import allure
import selenium

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger

from base.base_class import Base


class Main_page(Base):

    ########## Locators ############

    CATALOG_BUTTON_SELECTOR = "//span[text()='Каталог товаров']"
    ELECTRONICS_CATALOG_BUTTON_SELECTOR = "//span[text()='Смартфоны, ТВ и электроника']"

    ########## Action ##############

    def press_catalog_button(self):
        try:
            self.get_element(self.CATALOG_BUTTON_SELECTOR).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.get_element(self.CATALOG_BUTTON_SELECTOR).click()
        print("Press catalog button")

    def press_electronics_catalog_button(self):
        try:
            self.get_element(self.ELECTRONICS_CATALOG_BUTTON_SELECTOR).click()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.get_element(self.ELECTRONICS_CATALOG_BUTTON_SELECTOR).click()
        print("Press electronics catalog button")

    ########## Methods ##############

    def select_catalog(self):
        """ Select the desired directory """

        with allure.step("Select catalog"):
            Logger.add_start_step(method="select_product")
            self.press_catalog_button()
            self.press_electronics_catalog_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_product")
