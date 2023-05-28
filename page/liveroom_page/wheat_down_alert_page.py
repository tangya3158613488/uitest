from common.driver.appium_driver import AppiumDriver
from page.liveroom_page.confirm_wheat_alert_page import ConfirmWheatAlertPage
from page.objects_controller import ObjectsController
from page.public_page.navigationbar_page import NavigationBarPage


class WheatDownAlertPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def wheat_down_click(self):
        """
        点击下麦
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("wheat_down")))
        return ConfirmWheatAlertPage(self.appium_driver)

    def wheat_down_mute(self):
        """
        点击静音
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("mute")))
        return self.appium_driver.find_element(self.get_object("toast_mute")).text

    def wheat_down_cancel(self):
        """
        点击取消
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("wheat_down_cancel")))
        return WheatDownAlertPage(self.appium_driver)

    def alert_display(self):
        """下麦不可见"""
        return self.appium_driver.element_displayed(self.get_object("wheat_down"))

        # return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("wheat_down")))

