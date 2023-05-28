from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.record_page.audio_record_prepare_page import RecordPreparePage
from page.sing_page.ordered_page.local_acc_page import LocalAccPage


class OrderedPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def page_title_displayed(self):
        """
        页面title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("ordered_page_title"))

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=False)
    def click_import_acc_btn(self):
        """
        点击【导入伴奏】按钮
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("import_acc_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=False)
    def click_import_local_acc(self):
        """
        点击【导入本地伴奏】按钮
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("import_local_acc")))
        return LocalAccPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=False)
    def click_acc_cell(self):
        """
        点击伴奏热区
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("acc_cell")))
        return self

    def get_click_acc_cell_song_name(self):
        """
        获取点击的歌曲名
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            song_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("song_name"))[0], "text")
        else:
            song_name = self.appium_driver.get_attribute(
                self.appium_driver.find_elements(self.get_object("song_name"))[0],
                "label")
        print("找到了吗？", song_name)
        return song_name

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=False)
    def click_acc_sing_btn(self):
        """
        点击伴奏演唱按钮
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sing_btn")))
        return RecordPreparePage(self.appium_driver)
