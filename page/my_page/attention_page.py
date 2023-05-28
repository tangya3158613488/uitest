#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
关注
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController

class AttentionPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_attention_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是关注页
        """
        return self.appium_driver.element_displayed(self.get_object("attention_title"))
