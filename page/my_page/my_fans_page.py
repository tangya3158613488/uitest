#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的粉丝页
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController

class MyFansPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_my_fans_page(self):
        """
        判断是粉丝页面
        """
        return self.appium_driver.element_displayed(self.get_object("my_fans_title"))

