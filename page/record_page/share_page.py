from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class SharePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def is_share_title_shown(self):
        return self.appium_driver.element_displayed(self.get_object("share_title"))

    def click_close_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_btn")))
