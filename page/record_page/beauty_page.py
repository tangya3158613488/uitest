from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class BeautyPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def is_dressing_tab_showed(self):
        return self.appium_driver.element_displayed(self.get_object("dressing_tab"))

    def close_beauty_board(self):
        device_height = self.appium_driver.device_height()
        device_width = self.appium_driver.device_width()
        self.appium_driver.press_location(device_height / 2, device_width / 2)






