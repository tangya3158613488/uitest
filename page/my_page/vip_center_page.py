#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
会员中心页
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController

class VipCenterPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_vip_center_page(self):
        print(self.appium_driver.get_page_source())
        """
        判断是会员中心页
        """
        return self.appium_driver.element_displayed(self.get_object("vip_center_title"))

