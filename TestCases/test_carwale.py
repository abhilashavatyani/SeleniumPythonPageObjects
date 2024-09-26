import time

import logging

import pytest
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Pages.NewCarPage import NewCarPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.LogUtil import Logger

log = Logger("__name__", logging.INFO)


class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCars(self):
        log.logger.info("************** Inside New Car Test *****************")
        home = HomePage(self.driver)
        # Handle consent popup before performing other actions
        home.handleConsentPopup()
        home.gotoNewCars()
        time.sleep(5)

        # log.logger.info("************** Inside MarutiSuzuki Test *****************")
        # newCar = NewCarPage(self.driver)
        # newCar.selectMarutiSuzuki()

    # testcase2
    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle",
                             dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("************** Inside Select Car Test *****************")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        #home.handleConsentPopup()  # Handle the consent popup before proceeding

        if carBrand == "MarutiSuzuki":
            home.gotoNewCars().selectMarutiSuzuki()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
        elif carBrand == "Tata":
            home.gotoNewCars().selectTata()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
        elif carBrand == "Mahindra":
            home.gotoNewCars().selectMahindra()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
        else:
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."

    # test case 3
    @pytest.mark.parametrize("carBrand, carTitle",
                             dataProvider.get_data("NewCarsTest"))
    def test_printCarNamesandPrices(self,carBrand,carTitle):  # using consent fixture with "get_browser"
        log.logger.info("************** Inside Car Names and Prices Test *****************")

        # self.driver = get_browser
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        if carBrand == "MarutiSuzuki":
            time.sleep(5)
            # click NewCar > Find New car > select MarutiSuzuki

            home.gotoNewCars().selectMarutiSuzuki()
            time.sleep(5)
            # print the title of Maruti Suzuki
            title = car.getCarTitle()
            print(f"The car title is, {title}")
            # validate the title of the car
            assert title == carTitle, "Not on the correct page as the title is not matching."
            time.sleep(5)

            try:
                # get cars name and price
                car.getCarNamesandPrices()
            except UnexpectedAlertPresentException as e:
                # If an unexpected alert appears, handle it by accepting it
                alert = self.driver.switch_to.alert
                print(f"Unexpected alert present: {alert.text}")
                alert.dismiss()
            except NoAlertPresentException:
                # If no alert is present, just continue
                pass

        elif carBrand == "Tata":
            home.gotoNewCars().selectTata()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
            car.getCarNamesandPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
            car.getCarNamesandPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
            car.getCarNamesandPrices()
        elif carBrand == "Mahindra":
            home.gotoNewCars().selectMahindra()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
            car.getCarNamesandPrices()
        else:
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("The car title is " + title)
            assert title == carTitle, "Not on the correct page as the title is not matching."
            car.getCarNamesandPrices()
