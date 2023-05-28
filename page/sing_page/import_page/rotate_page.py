from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.sing_page.import_page.edit_page import EditPage


class RotatePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def rotate_btn_click(self):
        """
        旋转按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rotate_video")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def next_step_btn_click(self):
        """
        下一步按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("next_step_btn")))
        return EditPage(self.appium_driver)