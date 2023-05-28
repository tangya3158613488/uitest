#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class CameraPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_camera_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是否进入了相机页面
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("view_finder"))