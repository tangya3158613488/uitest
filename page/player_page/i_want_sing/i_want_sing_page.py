from page.objects_controller import ObjectsController
from common.driver.appium_driver import AppiumDriver


class IWantSing(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def i_want_sing_displayed(self):
        """
        我要唱 btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("i_want_sing"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def i_want_sing_btn_click(self):
        """
        我要唱 btn 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_want_sing")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def cantata_title_displayed(self):
        """
        清唱录制页面  title可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("cantata_title"))


