from enum import Enum

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserType(Enum):
    FIREFOX = 'firefox'
    CHROME = 'chrome'


class BrowserDriverFactory:
    @staticmethod
    def create_driver(kind: BrowserType = BrowserType.FIREFOX) -> WebDriver:
        if kind == BrowserType.FIREFOX:
            firefox_options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(), options=firefox_options
            )
        elif kind == BrowserType.CHROME:
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(), options=chrome_options
            )
        else:
            raise IOError(f'Unsupported driver: {kind}')

        driver.maximize_window()
        return driver
