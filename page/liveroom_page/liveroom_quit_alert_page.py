from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class LiveRoomQuitAlertPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def get_quit_alert_page_title(self):
        return self.appium_driver.find_element(self.get_object("title")).text

    def quit_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("quit_btn")))

    def small_btn_click(self):
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("small_btn")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def quit_btn_displayed(self):
        return self.appium_driver.element_displayed(self.get_object("quit_btn"))
