#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
找人页面
"""
import time

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.my_page.customer_my_page import CustomerMyPage
from page.objects_controller import ObjectsController


class FindPeoplePage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_find_people_page(self):
        """
        判断是找人页
        """
        # if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
        #     return True
        # else:
        #     return self.appium_driver.element_displayed(self.get_object("find_people_title"))
        return self.appium_driver.element_displayed(self.get_object("find_people_title"))

    def click_search_people_btn(self):
        """
        点击搜索用户btn
        :return:
        """
        # 点击搜索框
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_people_btn")))

    def input_search_btn(self, search_txt):
        # print(self.appium_driver.get_page_source())
        """
        跳转到搜索页面，输入搜索的内容
        查看搜索的内容是否有展示
        :param search_txt: 要搜索的用户
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_people_input")),
                                      search_txt)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))
        time.sleep(1)
        return self.appium_driver.element_displayed(self.get_object("search_user"))

    def personal_page_btn(self, search_txt="15600625102"):
        """
        选择用户进入个人主页
        :return:
        """
        self.click_search_people_btn()
        assert self.input_search_btn(search_txt)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_user")))
        return CustomerMyPage(self.appium_driver)
