#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab页
"""
import time

from page.message_page.message_page import MessagePage


class TestMessagePage:

    def test_search_btn_click(self, message_page: MessagePage):
        """
        点击查询按钮
        :param message_page:
        :return:
        """
        time.sleep(2)
        search_page = message_page.search_btn_click()
        assert search_page.in_message_search_page()
        message_page.close_btn_click()

    def test_fans_btn_click(self, message_page: MessagePage):
        """
        点击粉丝
        :param message_page:
        :return:
        """
        fans_page = message_page.fans_btn_click()
        assert fans_page.in_fans_page()

    def test_official_message_btn_click(self, message_page: MessagePage):
        """
        点击官方通知
        :param message_page:
        :return:
        """
        official_message_page = message_page.official_message_btn_click()
        assert official_message_page.in_official_message_page()

    # def test_gift_inform_btn_click(self,message_page:MessagePage):
    #     """
    #     点击礼物
    #     :param message_page:
    #     :return:
    #     """
    #     gift_inform_page = message_page.gift_inform_btn_click()
    #     assert gift_inform_page.in_gift_inform_page()

    def test_broadcast_btn_click(self, message_page: MessagePage):
        """
        点击寻人广播
        :param message_page:
        :return:
        """
        broadcast_page = message_page.broadcast_btn_click()
        assert broadcast_page.in_broadcast_title_page()

    # def test_interact_inform_btn_click(self,message_page:MessagePage):
    #     """
    #     互动通知
    #     :param message_page:
    #     :return:
    #     """
    #     interact_page = message_page.interact_inform_btn_click()
    #     assert interact_page.in_interact_inform_page()

    def test_more_btn_click(self, message_page: MessagePage):
        """
        点击更多按钮
        :param message_page:
        :return:
        """
        start_chat, add_friend = message_page.more_btn_click()
        assert start_chat and add_friend

    def test_start_chat_btn_click(self, message_page: MessagePage):
        """
        点击更多-发起聊天
        :param message_page:
        :return:
        """
        select_chat_object_page = message_page.start_chat_btn_click()
        assert select_chat_object_page.in_select_chat_object_page()

    def test_add_friend_btn_click(self, message_page: MessagePage):
        """
        点击更多-添加好友
        :param message_page:
        :return:
        """
        add_friend_page = message_page.add_friend_btn_click()
        assert add_friend_page.in_find_people_page()

    def test_find_group_btn_click(self, message_page: MessagePage):
        """
        发现群组
        :return:
        """
        nearby_group_page = message_page.find_group_btn_click()
        assert nearby_group_page.in_nearby_group_page()

    def test_my_group_btn_click(self, message_page: MessagePage):
        """
        我的群组
        :param message_page:
        :return:
        """
        my_group_page = message_page.my_group_btn_click()
        assert my_group_page.in_my_group_page()
