from page.objects_controller import ObjectsController
from common.driver.appium_driver import AppiumDriver

class GoodVoicePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def good_voice_time_role_displayed(self):
        """
        好声音 更新时间 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('good_voice_update_time'))

    def good_voice_role_click(self):
        """
        点击 好声音 规则icon
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("time_role")))

