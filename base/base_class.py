import time
import datetime

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """ Get current page address """

        url = self.driver.current_url
        print("Current url " + url)

    ########## Method assert word ############

    def assert_word(self, word, result, print_name="Assert: Value word right"):
        """ Makes a word comparison """

        value_word = word.text
        assert value_word == result
        print(print_name)

    ########## Method screenshot ############

    def get_screenshot(self, name):
        """ Get a screenshot of the current page """

        time.sleep(1)
        now_data = datetime.datetime.utcnow().strftime("%H.%M.%S.%d.%m.%Y")
        name_screenshot = name + now_data + '.png'
        self.driver.save_screenshot('F:\\PycharmProjects\\Vek_project\\screen\\' + name_screenshot)
        print("Get screenshot")

    ########## Method assety url ###########

    def assert_url(self, result):
        """ Makes a url comparison """
        assert self.get_current_url() == result
        print("Good value url")

    ########## Method get element ############

    def get_element(self, selector, locator=By.XPATH, timeout=8, select_method="element_to_be_clickable"):
        """ Gets the element  """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((locator, selector)))

    def element_is_visible(self, selector, locator=By.XPATH, timeout=5):
        self.go_to_element(self.element_is_present(selector))
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator, selector)))

    def elements_are_visible(self, selector, locator=By.XPATH, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator, selector)))

    def element_is_present(self, selector, locator=By.XPATH, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, selector)))

    def elements_are_present(self, selector, locator=By.XPATH, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((locator, selector)))

    def element_is_not_visible(self, selector, locator=By.XPATH, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((locator, selector)))

    def element_is_clickable(self, selector, locator=By.XPATH, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((locator, selector)))

    # Method go to element
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
