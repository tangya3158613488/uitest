#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.driver.appium_driver import AppiumDriver, SwipeDirection
from page.objects_controller import ObjectsController
from page.public_page.navigationbar_page import NavigationBarPage


class LivePage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def get_live_page_name(self):
        live_name = self.appium_driver.find_element(self.get_object("room_name")).text
        return live_name

    def close_live(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close")))

    def know_displayed(self):
        return self.appium_driver.element_displayed(self.get_object("i_know_btn"))

    def know_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_know_btn")))

