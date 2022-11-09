import time
import datetime
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import Base


class Login_page(Base):
    url = 'https://www.21vek.by/'

    ########## Locators ############

    ACCOUNT_SELECTOR_BUTTON_SELECTOR = "//span[text()='Аккаунт']"
    LOGIN_SELECTOR_BUTTON_SELECTOR = "//button[@data-testid='loginButton']"
    LOGIN_FIELD_SELECTOR = "//input[@id='login-email']"
    PASSWORD_FIELD_SELECTOR = "//input[@id='login-password']"
    ENTER_BUTTON_SELECTOR = "//button[@data-testid='loginSubmit']"
    ERROR_MESSAGE_LINE_SELECTOR = "//span[text()='Неправильный формат электронной почты']"

    ########## Action ##############

    def press_account_button(self):
        self.get_element(self.ACCOUNT_SELECTOR_BUTTON_SELECTOR).click()
        print("Press account button")

    def press_login_button(self):
        self.get_element(self.LOGIN_SELECTOR_BUTTON_SELECTOR).click()
        print("Press login button")

    def fill_field_login(self, login):
        self.get_element(self.LOGIN_FIELD_SELECTOR).send_keys(login)
        print("Fill user email field")

    def fill_field_password(self, password):
        self.get_element(self.PASSWORD_FIELD_SELECTOR).send_keys(password)
        print("Fill user password field")

    def press_enter_button(self):
        self.get_element(self.ENTER_BUTTON_SELECTOR).click()
        print("Press enter button")

    ########## Methods ##############

    def authorization(self):
        """ Open web applications, go to the authorization window
            and enter valid user data (login and password), then press the login button
            and go to the main page, check that we are on the right page """

        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.press_account_button()
            self.press_login_button()
            self.fill_field_login("pshevchik44@mail.ru")
            self.fill_field_password("CG6BBBI4")
            self.press_enter_button()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

    def wrong_data_authorization(self):
        """ Open web applications, go to the authorization window
            and enter invalid user data (login and password), then press the login button
            and check the pop-up notification """

        with allure.step("Authorization with invalid data"):
            Logger.add_start_step(method="wrong_data_authorization")
            self.driver.get(self.url)
            self.press_account_button()
            self.press_login_button()
            self.fill_field_login("$$$$$$$$$")
            self.fill_field_password("$$$$$$$$$$$")
            self.press_enter_button()
            self.assert_word(self.get_element(self.ERROR_MESSAGE_LINE_SELECTOR), "Неправильный формат электронной почты")
            Logger.add_end_step(url=self.driver.current_url, method="wrong_data_authorization")
