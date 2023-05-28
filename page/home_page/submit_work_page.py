from common.driver.appium_driver import AppiumDriver
from page.public_page.navigationbar_page import NavigationBarPage


class SubmitWorkPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.assert_title = "选择作品"
