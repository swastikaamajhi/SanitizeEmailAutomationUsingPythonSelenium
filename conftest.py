import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Capture screenshot on test failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to get the report object
    outcome = yield
    rep = outcome.get_result()

    # only for failed calls
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )