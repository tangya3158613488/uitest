from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.record_page.beauty_page import BeautyPage
from page.record_page.audio_record_prepare_page import RecordPreparePage
from page.record_page.prop_page import PropPage


class VideoRecordPreparePage(RecordPreparePage):
    def __init__(self, appium_driver, song_name='', singer=''):
        super().__init__(appium_driver, song_name, singer)
        self.appium_driver = appium_driver

    def is_flip_camera_btn_showed(self):
        return self.appium_driver.element_displayed(self.get_object("flip_camera_btn"))

    def is_prop_btn_showed(self):
        return self.appium_driver.element_displayed(self.get_object("prop_btn"))

    def is_beauty_btn_showed(self):
        return self.appium_driver.element_displayed(self.get_object("beauty_btn"))

    def click_beauty_btn(self):
        self.appium_driver.wait_for(2, False)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("beauty_btn")))
        beauty_page = BeautyPage(self.appium_driver)
        return beauty_page

    def click_prop_btn(self):
        self.appium_driver.wait_for(2, False)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("prop_btn")))
        prop_page = PropPage(self.appium_driver)
        return prop_page

    def close_tip(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_img")))
            return
        w = self.appium_driver.find_element(self.get_object("earphone_tip")).size["width"]
        h = self.appium_driver.find_element(self.get_object("earphone_tip")).size["height"]
        x = self.appium_driver.find_element(self.get_object("earphone_tip")).location['x'] + w - w * 1 / 10
        y = self.appium_driver.find_element(self.get_object("earphone_tip")).location['y'] + h / 2
        print("width is {},height is {},x is {},y is {}".format(w, h, x, y))
        return self.appium_driver.press_location(x, y)
