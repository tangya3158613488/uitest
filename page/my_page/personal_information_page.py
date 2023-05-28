#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的tab-编辑资料 --》个人信息页
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class PersonalInformationPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_personal_information_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是个人信息页
        """
        return self.appium_driver.element_displayed(self.get_object("personal_information_title"))
