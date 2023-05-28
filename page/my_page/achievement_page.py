"""
成就
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class AchievementPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_achievement_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是成就
        """
        return self.appium_driver.element_displayed(self.get_object("achievement_title"))
