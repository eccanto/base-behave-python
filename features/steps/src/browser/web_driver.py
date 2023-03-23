"""Module in charge of generating selenium web drivers."""

from enum import Enum
from typing import Union

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


WebDriver = Union[webdriver.Firefox, webdriver.Chrome]


class BrowserType(Enum):
    """Selenium web driver type."""

    FIREFOX = 'firefox'
    CHROME = 'chrome'


class BrowserDriverFactory:  # pylint: disable=too-few-public-methods
    """Factory in charge of generating selenium web drivers by browser type."""

    @staticmethod
    def create_driver(kind: BrowserType, headless: bool) -> WebDriver:
        """Generates selenium web driver."""
        options: Union[webdriver.FirefoxOptions, webdriver.ChromeOptions]
        driver: WebDriver

        if kind == BrowserType.FIREFOX:
            options = webdriver.FirefoxOptions()
            options.headless = headless
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        elif kind == BrowserType.CHROME:
            options = webdriver.ChromeOptions()
            options.headless = headless
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        else:
            raise IOError(f'Unsupported driver: {kind}')

        driver.maximize_window()
        return driver
