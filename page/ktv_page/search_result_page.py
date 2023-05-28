from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class NavSearchTabPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def search_result_title_displayed(self):
        """
        搜索结果页面标题可见
        :return:
        """
        pass
