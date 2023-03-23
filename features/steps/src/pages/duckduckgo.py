"""Module in charge of interacting with the DuckDuckGo Search Engine page."""

from selenium.webdriver.common.by import By

from features.steps.src.pages.base_search_engine import BaseSearchEngine


class DuckDuckGoPage(BaseSearchEngine):
    """Class in charge of interacting with the DuckDuckGo Search Engine page."""

    URL = 'https://duckduckgo.com/'

    _INPUT_SEARCH = (By.ID, 'search_form_input_homepage')
    _BTN_SEARCH = (By.ID, 'search_button_homepage')
    _RESULT_SEARCH = (By.ID, 'links')
