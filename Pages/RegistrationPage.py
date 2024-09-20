from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class Registration(BasePage):
    # contructor
    def __init__(self, driver):
        super().__init__(driver)

    def fillform(self, name, phoneNum, email, country, city, username, password):
        # self.driver.find_element_by_xpath(configReader.readConfig("locators", "name_CSS")).send_key(name)
        # self.driver.find_element_by_xpath(configReader.readConfig("locators", "phone_CSS")).send_key(phoneNum)
        # self.driver.find_element_by_xpath(configReader.readConfig("locators", "email_XPATH")).send_key(email)
        #
        # dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", "country_XPATH"))
        # select = Select(dropdown)
        # select.select_by_visible_text(country)
        #
        # self.driver.find_element_by_xpath(configReader.readConfig("", ""))
        # self.driver.find_element_by_xpath(configReader.readConfig("", ""))
        # self.driver.find_element_by_xpath(configReader.readConfig("", ""))

#keyword driven approach
        self.type("name_XPATH", name)
        self.type("phone_XPATH", phoneNum)
        self.type("email_XPATH", email)
        # dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", "country_XPATH"))
        # select = Select(dropdown)
        # select.select_by_visible_text(country)
        self.select("country_XPATH", country)
        self.type("city_XPATH", city)
        self.type("username_XPATH", username)
        self.type("password_XPATH", password)
        self.click("submit_XPATH")
