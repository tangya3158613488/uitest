#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息-寻人广播/歌友召集
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class BroadcastPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_broadcast_title_page(self):
        """
        判断是否在寻人广播页
        """
        return self.appium_driver.element_displayed(self.get_object("broadcast_title"))
