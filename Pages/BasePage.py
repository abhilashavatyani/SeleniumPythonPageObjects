# contains everything common will used by all the classes
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from Utilities import configReader
import logging
from Utilities.LogUtil import Logger

# "__name__" to get the current file name
log = Logger(__name__, logging.INFO)


class BasePage:
    # define a driver which is common in all the classes
    def __init__(self, driver):
        self.driver = driver
        # Set implicit wait time globally
        self.driver.implicitly_wait(10)

    # @pytest.mark.skip                       # as included this as fixture under conftest.py
    # def handleConsentPopup(self):
    #     try:
    #         consent_button_locator = configReader.readConfig("locators", "consent_XPATH")
    #         consent_button = self.driver.find_element(By.XPATH, consent_button_locator)
    #         consent_button.click()
    #         log.logger.info("Consent popup handled by clicking on the consent button.")
    #     except NoSuchElementException:
    #         log.logger.info("Consent popup not found. Moving ahead without handling.")

    # Keyword driven approach
    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
        log.logger.info("clicking on an element:" + str(locator))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing on an element:" + str(locator) + "the text is: " + str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))
        log.logger.info("selecting an element:" + str(locator) + "the value selected is " + str(value))

        select = Select(dropdown)
        select.select_by_visible_text(value)

    # carwale.com
    def moveTo(self, locator):
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("moving the element:" + str(locator))
