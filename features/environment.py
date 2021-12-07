import hashlib
import os
import shutil
import uuid
from datetime import datetime

from behave.model import Scenario
from behave.model_core import Status
from behave.runner import Context
from pyvirtualdisplay import Display

from features.steps.src.browser.driver import BrowserType


_DATE_FORMAT = '%H.%M.%S_%m.%d.%Y'


def before_all(context: Context) -> None:
    browser_kind = context.config.userdata.get('browser')

    context.screenshots_dir = context.config.userdata.get('screenshots', 'screenshots')
    if os.path.isdir(context.screenshots_dir):
        shutil.rmtree(context.screenshots_dir)

    context.headless_mode = context.config.userdata.get('headless').lower() == 'true'

    context.browser_params = dict(
        kind=next((kind for kind in BrowserType if kind.value == browser_kind), browser_kind),
    )

    if context.headless_mode:
        context.display = Display(visible=0, size=(800, 600))
        context.display.start()


def after_scenario(context: Context, scenario: Scenario) -> None:
    if scenario.status == Status.failed:
        hash_gen = hashlib.sha256()
        hash_gen.update(f'{scenario.feature.filename}_{scenario.line}'.encode())

        feature_prefix = scenario.feature.filename.replace(os.sep, '.')
        scenario_id = f'{feature_prefix}_line{scenario.line}_{hash_gen.hexdigest()}'

        screenshot_scenario_dir = os.path.join(context.screenshots_dir, scenario_id)
        os.makedirs(screenshot_scenario_dir, exist_ok=True)

        date_str = datetime.now().strftime(_DATE_FORMAT)
        screenshot_file = os.path.join(
            screenshot_scenario_dir,
            f'{date_str}_{uuid.uuid4().hex}.png',
        )
        context.browser.driver.save_screenshot(screenshot_file)

    context.browser.driver.close()


def after_all(context: Context) -> None:
    if context.headless_mode:
        context.display.stop()
