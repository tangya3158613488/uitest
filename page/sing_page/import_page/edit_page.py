# from tkinter import RIGHT

from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.sing_page.import_page.upload_page import UploadPage


class EditPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def close_bottom_pop(self):
        """
        点击页面空白处收起弹窗
        :return:
        """
        self.appium_driver.press_location(600, 700)
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def swipe_effect_filter_module(self):
        """
        滑动特效 滤镜模块
        :return:
        """
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.swipe(device_width * 0.85, device_height * 0.9, device_width * 0.35, device_height * 0.9)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def audio_volume_btn_click(self):
        """
        音量按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("volume_btn")))
        return self

    def drag_audio_volume_seek(self):
        """
        拖动音量进度条
        :return:
        """
        self.appium_driver.swipe_el(self.appium_driver.find_element(self.get_object("audio_volume_seek_bar")), RIGHT, 500)
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def effect_edit_btn_click(self):
        """
        特效按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("effect_edit_btn")))
        return self

    def long_click_effect(self):
        """
        长按特效选择特效
        :return:
        """
        self.swipe_effect_filter_module()
        self.appium_driver.long_press_element(self.appium_driver.find_elements(self.get_object("effect_image"))[8])
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def filter_edit_btn_click(self):
        """
        滤镜按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("filter_edit_btn")))
        return self

    def choose_filter(self):
        """
        选择具体滤镜
        :return:
        """
        self.swipe_effect_filter_module()
        self.appium_driver.press_element(self.appium_driver.find_elements("filter_image")[6])
        return self

    def cover_btn_click(self):
        """
        封面按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element("cover_btn"))
        return self

    def drag_choose_cover(self):
        """
        拖动选择封面
        :return:
        """
        self.appium_driver.swipe_el(self.appium_driver.find_element("cover_seek_bar"), RIGHT, 500)
        return self

    def click_save_btn(self):
        """
        点击保存按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("save_btn")))
        return self

    def click_next_step(self):
        """
        点击下一步按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("next_step_btn")))
        return UploadPage(self.appium_driver)





