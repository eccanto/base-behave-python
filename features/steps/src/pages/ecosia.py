"""Module in charge of interacting with the Ecosia Search Engine page."""

from selenium.webdriver.common.by import By

from features.steps.src.pages.base_search_engine import BaseSearchEngine


class EcosiaPage(BaseSearchEngine):
    """Class in charge of interacting with the Ecosia Search Engine page."""

    URL = 'https://www.ecosia.org/'

    _INPUT_SEARCH = (By.CSS_SELECTOR, 'input[type=search]')
    _BTN_SEARCH = (By.CSS_SELECTOR, 'button[type=submit]')
    _RESULT_SEARCH = (By.CLASS_NAME, 'mainline')
