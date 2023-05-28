#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab
"""
from common.driver.appium_driver import AppiumDriver
# from page.message_page.message_private_chat_page import MessagePrivateChatPage
from page.message_page.broadcast_page import BroadcastPage
from page.message_page.fans_page import FansPage
from page.message_page.find_people_page import FindPeoplePage
from page.message_page.gift_inform_page import GiftInformPage
from page.message_page.interact_inform_page import InteractInformPage
from page.message_page.message_private_chat_page import MessagePrivateChatPage
from page.message_page.message_search_page import MessageSearchPage
from page.message_page.my_group_page import MyGroupPage
from page.message_page.nearby_group_page import NearByGroupPage
from page.message_page.official_message_page import OfficialMessagePage
from page.message_page.select_chat_object_page import SelectChatObjectPage
from page.objects_controller import ObjectsController


class MessagePage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        # print(self.appium_driver.get_page_source())

    def in_message_page(self):
        return self.appium_driver.element_displayed(self.get_object("message_tab"))

    def private_chat_user_btn_click(self):
        """
        私聊用户点击
        :return:
        """
        print("是否存在？",self.appium_driver.find_element(self.get_object("private_chat_user_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("private_chat_user_btn")))
        return MessagePrivateChatPage(self.appium_driver)

    def search_btn_click(self):
        """
        查询按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))
        return MessageSearchPage(self.appium_driver)
    def close_btn_click(self):
        """
        查询页的取消按钮点击
        :return:
        :rtype:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_btn")))

    def more_btn_click(self):
        """
        更多按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn")))
        start_chat = self.appium_driver.element_displayed(self.get_object("start_chat_btn"))
        add_friend = self.appium_driver.element_displayed(self.get_object("add_friend_btn"))
        return start_chat,add_friend


    def fans_btn_click(self):
        """
        粉丝cell点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("fans_btn")))
        return FansPage(self.appium_driver)

    def my_group_btn_click(self):
        """
        我的群组点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_group_btn")))
        return MyGroupPage(self.appium_driver)

    def find_group_btn_click(self):
        """
        发现群组点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("find_group_btn")))
        return NearByGroupPage(self.appium_driver)

    def quick_find_group_btn_click(self):
        """
        快速找群
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("quick_find_group_btn")))

    def interact_inform_btn_click(self):
        """
        互动通知
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("interact_inform_btn")))
        return InteractInformPage(self.appium_driver)


    def gift_inform_btn_click(self):
        """
        礼物通知
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("gift_inform_btn")))
        return GiftInformPage(self.appium_driver)


    def official_message_btn_click(self):
        """
        官方消息
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("official_message_btn")))
        return  OfficialMessagePage(self.appium_driver)

    def broadcast_btn_click(self):
        """
        寻人广播
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("broadcast_btn")))
        return BroadcastPage(self.appium_driver)

    def start_chat_btn_click(self):
        """
        点击发起聊天按钮
        :return:
        """
        start_chat, add_friend = self.more_btn_click()
        if start_chat:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("start_chat_btn")))
            return SelectChatObjectPage(self.appium_driver)

    def add_friend_btn_click(self):
        """
        点击发起添加好友按钮
        :return:
        """
        start_chat, add_friend = self.more_btn_click()
        if add_friend:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("add_friend_btn")))
            return FindPeoplePage(self.appium_driver)
