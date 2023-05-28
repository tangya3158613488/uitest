#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
私聊-相机
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class CameraRollPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_camera_roll_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是否在相册胶卷页
        """
        return self.appium_driver.element_displayed(self.get_object("camera_roll_title"))
