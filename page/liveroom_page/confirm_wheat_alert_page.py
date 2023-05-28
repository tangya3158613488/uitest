
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class ConfirmWheatAlertPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def confirm(self):
        """
        点击确定
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm")))


    def cancel(self):
        """
        点击取消
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel")))

    def confirm_alert_diaplay(self):
        """
        弹框title可见
        :return:
        """
        return self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("title")))