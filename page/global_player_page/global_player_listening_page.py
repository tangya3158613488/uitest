import time

from common.driver.appium_driver import AppiumDriver
from page.global_player_page.global_player_xiaochang_fm_page import GlobalPlayerXiaoChangFMPage
from page.objects_controller import ObjectsController


class GlobalPlayerListeningPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def empty_page(self):
        """
        是否是空页面
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("xiaochang_btn"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_clear_btn(self):
        """
        点击清空按钮，ios自动点弹窗的确认
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clear_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_clear_sure_btn(self):
        """
        点击清空按钮
        :return:
        """
        self.appium_driver.accept_alert()
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_xiaochang_btn(self):
        """
        无数据时点击进入小唱FM按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("xiaochang_btn")))
        return GlobalPlayerXiaoChangFMPage(self.appium_driver)
