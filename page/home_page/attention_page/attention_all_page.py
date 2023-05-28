#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.driver.appium_driver import AppiumDriver
from page.me_page.person_page import PersonPage
from page.objects_controller import ObjectsController
from page.home_page.home_base_element_page import HomeBaseElementPage


class AttentionAllPage(HomeBaseElementPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.chorus = "加入合唱"

    def recommend_user_click(self):
        self.find_els("recommend_user_icon")
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("recommend_user_icon")))
        return PersonPage(self.appium_driver)

    def get_recommend_user_name(self):
        self.find_els("recommend_user_name")
        return self.appium_driver.find_element(self.get_object("recommend_user_name")).text

    def recommend_attention_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("recommend_user_attention")))

    def get_recommend_user_attention_status(self):
        self.find_els("recommend_user_attention")
        return self.appium_driver.find_element(self.get_object("recommend_user_attention")).text
