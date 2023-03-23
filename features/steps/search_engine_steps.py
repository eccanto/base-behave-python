"""Steps implementation in charge of interacting with the search engine page."""

from assertpy import assert_that
from behave import step
from behave.runner import Context

from features.steps.src.pages.duckduckgo import DuckDuckGoPage
from features.steps.src.pages.ecosia import EcosiaPage


@step('I go to the Ecosia page')
def step_impl(context: Context) -> None:
    """Loads the main Ecosia page."""
    context.browser = EcosiaPage(**context.browser_params)
    context.browser.load()


@step('I go to the Duckduckgo page')
def step_impl(context: Context) -> None:
    """Loads the main Duckduckgo page."""
    context.browser = DuckDuckGoPage(**context.browser_params)
    context.browser.load()


@step('I fill the search input with the "{text}" term on the Search Engine page')
def step_impl(context: Context, text: str) -> None:
    """Enters text for the search."""
    context.browser.fill_search(text)


@step('I click on the search button on the Search Engine page')
def step_impl(context: Context) -> None:
    """Runs the search."""
    context.browser.search()


@step('the text "{text}" should be visible on the result page on the Search Engine page')
def step_impl(context: Context, text: str) -> None:
    """Checks that the text is shown on the page."""
    assert_that(context.browser.result_text()).contains(text)
