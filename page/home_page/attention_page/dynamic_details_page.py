#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wuqiongxue
from page.objects_controller import ObjectsController
from common.driver.appium_driver import AppiumDriver
from page.public_page.navigationbar_page import NavigationBarPage
import time


class DynamicDetailsPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.assert_moment_details = "动态详情"

    def getPageTitle(self):
        return self.title()

    def cancel_publish_dynamic(self):
        self.back_btn_click()
        time.sleep(2)
        print(self.get_object("confirm"))
        print("是否存在%s" % str(self.appium_driver.element_displayed(self.get_object("confirm"))))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def dynamic_details_comment(self):
        """
        是否弹出评论列表
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("comment_count"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def dynamic_details_comment_content(self):
        """
        是否弹出评论列表
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("content"))