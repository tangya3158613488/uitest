#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.driver.appium_driver import AppiumDriver
from page.home_page.home_base_element_page import HomeBaseElementPage


class AttentionDynamicPage(HomeBaseElementPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

