"""
歌手等级页面
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class SingerGradePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_singer_grade_page(self):
        """
        判断是歌手等级页面
        """
        return self.appium_driver.element_displayed(self.get_object("singer_grade_page_title"))
