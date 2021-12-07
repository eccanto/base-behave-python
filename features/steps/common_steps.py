from assertpy.assertpy import assert_that
from behave import step
from behave.runner import Context


@step('I see "{title}" in the title')
def step_impl(context: Context, title: int) -> None:
    assert_that(context.browser.driver.title).contains(title)
