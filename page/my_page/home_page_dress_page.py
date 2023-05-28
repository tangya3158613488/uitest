"""
主页装扮页面
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController

class HomePageDressPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_home_page_dress_page(self):
        """
        判断是主页装扮页
        """
        return self.appium_driver.element_displayed(self.get_object("home_page_dress_title"))

