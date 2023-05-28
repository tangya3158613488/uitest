#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class PersonPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def get_username(self):
        username = self.appium_driver.find_element(self.get_object("username_id")).text
        print("person username%s" % username)
        return username

    def get_attention_status(self):
        return self.appium_driver.find_element(self.get_object("user_attention")).text

    def cancel_attention(self):
        if self.get_attention_status() == "":
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("user_attention")))
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_attention")))
            return self.get_attention_status()
        else:
            return self.get_attention_status()
