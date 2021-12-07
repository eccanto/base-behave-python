from abc import ABCMeta
from typing import Any, Dict, List, Tuple

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from features.steps.src.browser.driver import BrowserDriverFactory


ElementSelector = Tuple[str, str]


class BaseSearchEngine(metaclass=ABCMeta):
    URL: str

    _INPUT_SEARCH: ElementSelector
    _BTN_SEARCH: ElementSelector
    _RESULT_SEARCH: ElementSelector

    def __init__(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        self.driver = BrowserDriverFactory.create_driver(*args, **kwargs)

    def load(self) -> None:
        self.driver.get(self.URL)

    def find_element(self, selector: ElementSelector, timeout: float = 10.0) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(selector)
        )

    def fill_search(self, text: str) -> None:
        input_web = self.find_element(self._INPUT_SEARCH)
        input_web.send_keys(text)

    def search(self) -> None:
        self.find_element(self._BTN_SEARCH).click()

    def result_text(self) -> str:
        return self.find_element(self._RESULT_SEARCH).text
