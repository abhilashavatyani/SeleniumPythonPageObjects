# carwale.com
import time

from Pages.BasePage import BasePage
from Pages.NewCarPage import NewCarPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newCar_XPATH")
        #time.sleep(4)
        self.click("findNewCar_XPATH")
        #time.sleep(3)

        return NewCarPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass


