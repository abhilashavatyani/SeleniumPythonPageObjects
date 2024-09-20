from Pages.BasePage import BasePage
from Pages.MarutiSuzukiPage import MarutiSuzukiPage


class NewCarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def selectMarutiSuzuki(self):
        self.click("marutiSuzuki_XPATH")

        return MarutiSuzukiPage(self.driver)

    def selectHyundai(self):
        self.click("hyundai_XPATH")



    def selectTata(self):
        self.click("tata_XPATH")

    def selectMahindra(self):
        self.click("mahindra_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectBMW(self):
        self.click("BMW_XPATH")