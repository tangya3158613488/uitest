"""
附近群组
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class NearByGroupPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_nearby_group_page(self):
        """
        判断是否在附近群组页
        """
        return self.appium_driver.element_displayed(self.get_object("nearby_group_title"))

