"""Module in charge of interacting with the Search Engine page."""

from abc import ABCMeta
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from features.steps.src.browser.web_driver import BrowserDriverFactory, BrowserType


ElementSelector = Tuple[str, str]


class DuckduckgoPage(metaclass=ABCMeta):
    """Class in charge of interacting with the Search Engine page."""

    URL = 'https://duckduckgo.com/'

    _INPUT_SEARCH = (By.ID, 'search_form_input_homepage')
    _BTN_SEARCH = (By.ID, 'search_button_homepage')
    _RESULT_SEARCH = (By.ID, 'links')

    def __init__(self, kind: BrowserType, headless: bool) -> None:
        """Constructor method."""
        self.driver = BrowserDriverFactory.create_driver(kind=kind, headless=headless)

    def load(self) -> None:
        """Loads the main page."""
        self.driver.get(self.URL)

    def find_element(self, selector: ElementSelector, timeout: float = 10.0) -> WebElement:
        """Finds an element."""
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(selector))

    def fill_search(self, text: str) -> None:
        """Enters text for the search."""
        input_web = self.find_element(self._INPUT_SEARCH)
        input_web.send_keys(text)

    def search(self) -> None:
        """Runs the search."""
        self.find_element(self._BTN_SEARCH).click()

    def result_text(self) -> str:
        """Gets the text of the search result."""
        return self.find_element(self._RESULT_SEARCH).text
