"""
我的tab -- 上榜记录
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class ListRecordPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_list_record_page(self):
        """
        判断是上榜记录页面
        """
        return self.appium_driver.element_displayed(self.get_object("list_record_title"))


