#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
找人页
"""
from page.message_page.find_people_page import FindPeoplePage


class TestFindPeoplePage:
    def test_input_search_btn(self,find_people_page:FindPeoplePage):
        """
        点击查询按钮
        :param message_page:
        :return:
        """
        find_people_page.click_search_people_btn()
        assert find_people_page.input_search_btn("15600625102")

    def test_personal_page_btn(self,find_people_page:FindPeoplePage):
        customer_my_page = find_people_page.personal_page_btn("15600625102")
        assert customer_my_page.in_customer_my_page()






