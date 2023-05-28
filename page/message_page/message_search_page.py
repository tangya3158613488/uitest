#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab-左上角查询
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class MessageSearchPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_message_search_page(self):
        """
        判断是否在查询页
        """
        return self.appium_driver.element_displayed(self.get_object("search_box"))


