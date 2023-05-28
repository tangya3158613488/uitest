#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
选择对象聊天页
"""
import time

from page.message_page.select_chat_object_page import SelectChatObjectPage


class TestSelectChatObjectPage:

    def test_click_search_chat_object_btn(self, select_chat_object_page: SelectChatObjectPage):
        """
        点击查询进入私聊页
        :param select_chat_object_page:
        :return:
        """
        message_private_page = select_chat_object_page.click_search_chat_object_btn("玛卡")
        assert message_private_page.in_message_private_page()

    def test_click_search_people_btn(self, select_chat_object_page: SelectChatObjectPage):
        """
        点击找人按钮
        :param select_chat_object_page:
        :return:
        """
        time.sleep(1)
        find_people_page = select_chat_object_page.click_search_people_btn()
        assert find_people_page.in_find_people_page()

    def test_click_number_one_group(self, select_chat_object_page: SelectChatObjectPage):
        """
        点击我加入的群组选择第一个群组进行点击
        :param select_chat_object_page:
        :return:
        """
        group_message_page = select_chat_object_page.click_number_one_group()
        assert group_message_page.in_message_group_page() is False

    def test_click_number_one_friend(self, select_chat_object_page: SelectChatObjectPage):
        """
        点击我关注的人选择第一个进行点击
        :param select_chat_object_page:
        :return:
        """

        private_message_page = select_chat_object_page.click_number_one_friend()
        assert private_message_page.in_message_private_page()
