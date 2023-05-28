from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class AudioLivePreparePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def select_background_txt_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("select_background_txt"))
