# 82. capturing screenshot in case of failure
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configReader

import logging
from Utilities.LogUtil import Logger

# "__name__" to get the current file name
log = Logger(__name__, logging.INFO)


# 83. Pytest - understanding conftest.py file
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()  # 82. capturing screenshot in case of failure
def log_on_failure(request, get_browser):  # 83. use common fixture defined under conftest.py
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


# 84.pytest – Parameterized fixture
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        # Add option to block notifications
        prefs = {
            "profile.default_content_setting_values.notifications": 2  # 2 means block
        }
        options.add_experimental_option("prefs", prefs)

        service = Service(executable_path=ChromeDriverManager().install().replace("THIRD_PARTY_NOTICES.chromedriver",
                                                                                  "chromedriver.exe"))
        driver = webdriver.Chrome(service=service, options=options)
    if request.param == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    request.cls.driver = driver  # added when moved all usefixture call to BaseTest.py

    driver.get(configReader.readConfig("basic info", "testsiteurl"))
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(autouse=True)
# def handleConsentPopup(get_browser):
#     """Fixture that automatically handles the consent popup if it appears during any test step."""
#     try:
#         consent_button_locator = configReader.readConfig("locators", "consent_XPATH")
#         consent_button = get_browser.find_element(By.XPATH, consent_button_locator)
#         if consent_button.is_displayed():
#             consent_button.click()
#             log.logger.info("Consent popup handled by clicking on the consent button.")
#     except NoSuchElementException:
#         log.logger.info("Consent popup not found. Moving ahead without handling.")
