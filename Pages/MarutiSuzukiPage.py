# every page will have the same contructor with super key word and the base class as well (BasePage)
from Pages.BasePage import BasePage


class MarutiSuzukiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)