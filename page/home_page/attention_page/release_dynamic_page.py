#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wuqiongxue
from page.objects_controller import ObjectsController
from common.driver.appium_driver import AppiumDriver
from page.public_page.navigationbar_page import NavigationBarPage
import time


class PublishDynamicPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.assert_title = "发动态"

    def getPageTitle(self):
        return self.title()

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def cancel_publish_dynamic(self):
        self.back_btn_click()
        time.sleep(2)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def in_public_dynamic_page(self):
        """
        是否在发动态页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("public_btn"))
