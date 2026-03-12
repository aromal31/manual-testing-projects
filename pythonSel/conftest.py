import pytest
from selenium import webdriver
from datetime import datetime
import pytest_html


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection"
    )


@pytest.fixture()
def browserInstance(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(4)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        extra = getattr(report, "extras", [])

        if report.failed:

            driver = item.funcargs.get("browserInstance")

            if driver:

                screenshot = driver.get_screenshot_as_base64()

                extra.append(pytest_html.extras.image(screenshot, mime_type="image/png"))

        report.extras = extra