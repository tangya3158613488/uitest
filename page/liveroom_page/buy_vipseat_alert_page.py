from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
import time


class BuyVipSeatAlertPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def get_vipseatpage_title(self):
        return self.appium_driver.find_element(self.get_object("buy_title")).text

    def confirm_btn_click(self):
        time.sleep(3)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("buy_confirm_btn")))
        return self.appium_driver.find_element(self.get_object("buy_success_toast")).text

    def cancel_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("buy_cancel_btn")))
        return BuyVipSeatAlertPage(self.appium_driver)


    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def confirm_btn_displayed(self):
        return self.appium_driver.element_displayed(self.get_object("buy_confirm_btn"))
