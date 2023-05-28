from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class NavSearchTabPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def search_edit_displayed(self):
        """
        搜索输入框可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("search_edit"))

    def search_edit_click(self):
        """
        点击搜索输入框
        :return:
        """
        pass

    def search_history_click(self):
        """
        搜索历史
        :return:
        """
        pass
