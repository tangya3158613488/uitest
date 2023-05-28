"""
我的tab -- 我的直播页面
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class MyLivePage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_my_live_page(self):
        """
        判断是我的直播页面
        """
        return self.appium_driver.element_displayed(self.get_object("start_live_btn"))


