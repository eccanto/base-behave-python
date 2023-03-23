"""Common steps implementation in charge of interacting with the search engine page."""

from assertpy.assertpy import assert_that
from behave import step
from behave.runner import Context


@step('I see "{title}" in the title')
def step_impl(context: Context, title: int) -> None:
    """Asserts that the title contains `title`."""
    assert_that(context.browser.driver.title).contains(title)
