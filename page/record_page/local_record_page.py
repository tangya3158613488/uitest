#!/usr/bin/python
# coding=utf-8
# author:lzy
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class LocalRecordPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_local_record_page(self):
        """
        查看是否在本地录音页面
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("title"))

    def click_back_btn(self):
        """
        点击返回到我页面
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_btn")))

    def get_song_name(self, index):
        """
        获取本地录音的伴奏名
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_elements(self.get_object("song_name"))[index],
                                                'label')

    def is_MV_icon_shown(self, index):
        """
        是否展示MV icon
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("MV_icon"))[index]

    def get_record_time(self, index):
        """
        获取录制时间：label:12-09 10:45
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_elements(self.get_object("record_time"))[index],
                                                'label')

    def get_record_total_time(self, index):
        """
        获取录制时长：label:04:46
        :return:
        """
        return self.appium_driver.get_attribute(
            self.appium_driver.find_elements(self.get_object("record_total_time"))[index],
            'label')
