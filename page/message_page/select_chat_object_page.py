#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
选择聊天对象页
消息tab-更多-发起聊天-选择聊天对象页
"""
import platform

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.message_page.find_people_page import FindPeoplePage
from page.message_page.message_group_chat_page import MessageGroupChatPage
from page.message_page.message_private_chat_page import MessagePrivateChatPage
from page.objects_controller import ObjectsController
import time


class SelectChatObjectPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_select_chat_object_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是否在选择聊天对象页
        """
        return self.appium_driver.element_displayed(self.get_object("select_chat_object_title"))

    def click_search_chat_object_btn(self,nickname="玛卡"):
        """
        进入私聊页
        :param nickname:
        :return:
        """
        # 点击输入框
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_chat_object_btn")))
        # 将内容输入
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("input_chat_object_btn")),nickname)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))
        time.sleep(1)
        # 查看是否展示
        assert self.appium_driver.element_displayed(self.get_object("private_chat_user_btn"))
        # 点击进入私聊页
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("private_chat_user_btn")))
        return MessagePrivateChatPage(self.appium_driver)

    def click_search_people_btn(self):
        # print(self.appium_driver.get_page_source())
        """
        点击找人按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_people_btn")))
        return FindPeoplePage(self.appium_driver)

    def click_number_one_friend(self):
        """
        点击发起聊天下我关注人的第一个对象
        :return:
        """
        # print(self.appium_driver.get_page_source())
        if AppiumDriver.global_var["platform"] == PlatformSelector.ANDROID:
            top_one = self.appium_driver.find_element(self.get_object("top_one"))
            self.appium_driver.press_element(top_one)
            return MessagePrivateChatPage(self.appium_driver)
        else:
            while True:
                me_attention_people_txt = self.appium_driver.element_displayed(self.get_object("me_attention_people_txt"))
                if me_attention_people_txt:
                    user_list = self.appium_driver.find_elements(self.get_object("user_list"))
                    if user_list:
                        self.appium_driver.press_element(user_list[0])
                        return MessagePrivateChatPage(self.appium_driver)
                    else:
                        return None
                else:
                    # 判断是否能拿到数据，若拿不到则滑动一屏
                    self.appium_driver.swipe_up(500)
                    time.sleep(1)

    def click_number_one_group(self):
        """
        点击发起聊天下我的群组下的第一个群组
        :return:
        """
        group_list = self.appium_driver.find_elements(self.get_object("group_list"))
        print(group_list)
        # 第一个是创建群组，从第二开始是群组
        if len(group_list)>1:
            self.appium_driver.press_element(group_list[4])
            return MessageGroupChatPage(self.appium_driver)






