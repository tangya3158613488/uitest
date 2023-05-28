#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的群组页
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController

class MyGroupPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_my_group_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是我的群组页
        """
        return self.appium_driver.element_displayed(self.get_object("my_group_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_other_group_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是客态的群组页
        """
        return self.appium_driver.element_displayed(self.get_object("other_group_title"))
