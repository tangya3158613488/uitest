from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.record_page.audio_record_prepare_page import RecordPreparePage


class LocalAccPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("local_acc_title"))

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=False)
    def click_acc_el(self):
        """
        点击具体伴奏
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("acc_el")))
        return self

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=False)
    def click_sing_btn(self):
        """
        点击演唱按钮
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sing_btn")))
        return RecordPreparePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def get_song_name(self):
        """
        获取点击的歌曲名
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            song_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("song_name"))[0],
                "text")
        else:
            song_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("song_name"))[0],
                "label")
        return song_name
