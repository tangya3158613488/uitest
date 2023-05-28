#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的tab -- 最近来访页
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class LatelyVisitPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_lately_visit_page(self):
        """
        判断是最近来访页
        """
        return self.appium_driver.element_displayed(self.get_object("lately_visit_title"))


