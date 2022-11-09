import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def group_up():
    print("Enter system")
    yield
    print("Exit system")
