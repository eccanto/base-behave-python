from assertpy import assert_that
from behave import step
from behave.runner import Context

from features.steps.src.pages.duckduckgo import DuckDuckGoPage
from features.steps.src.pages.ecosia import EcosiaPage


@step('I go to the Ecosia page')
def step_impl(context: Context) -> None:
    context.browser = EcosiaPage(**context.browser_params)
    context.browser.load()


@step('I go to the Duckduckgo page')
def step_impl(context: Context) -> None:
    context.browser = DuckDuckGoPage(**context.browser_params)
    context.browser.load()


@step('I fill the search input with the "{text}" term on the Search Engine page')
def step_impl(context: Context, text: str) -> None:
    context.browser.fill_search(text)


@step('I click on the search button on the Search Engine page')
def step_impl(context: Context) -> None:
    context.browser.search()


@step('the text "{text}" should be visible on the result page on the Search Engine page')
def step_impl(context: Context, text: str) -> None:
    assert_that(context.browser.result_text()).contains(text)
