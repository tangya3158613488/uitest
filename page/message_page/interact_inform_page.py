#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab-互动通知页
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class InteractInformPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver


    def in_interact_inform_page(self):
        """
        判断是否在互动通知页
        :return:
        """
        self.appium_driver.element_displayed(self.get_object("interact_title"))

