from selenium.webdriver.common.by import By

from Utilities import configReader


class CarBase:
    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, configReader.readConfig("locators", "carTitle_XPATH")).text
        #return self.driver.find_element(By.XPATH, configReader.readConfig("locators", "carTitle_XPATH")).text

    def getCarNamesandPrices(self):
        carNames = self.driver.find_elements(By.XPATH, configReader.readConfig("locators", "carNames_XPATH"))
        carPrices = self.driver.find_elements(By.XPATH, configReader.readConfig("locators", "carPrices_XPATH"))

        for i in range(1, len(carPrices)):
            print("------ " + carNames[i].text + "car price is" + carPrices[i].text + " -----")
