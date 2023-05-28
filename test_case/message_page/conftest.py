#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
import pytest

from page.public_page.client_utils_page import ClientUtilsPage


@pytest.fixture()
def message_page(client_utils_page: ClientUtilsPage):
    """
    message tab页
    :param client_utils_page:
    :return:
    """
    return  client_utils_page.go_to_tab_bar_master().message_tab_click()


@pytest.fixture()
def message_private_chat_page(client_utils_page: ClientUtilsPage):
    """
    私聊页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().message_tab_click().start_chat_btn_click().click_search_chat_object_btn()

@pytest.fixture()
def select_chat_object_page(client_utils_page: ClientUtilsPage):
    """
    选择对象聊天页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().message_tab_click().start_chat_btn_click()

@pytest.fixture()
def find_people_page(client_utils_page: ClientUtilsPage):
    """
    查询用户页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().message_tab_click().add_friend_btn_click()

@pytest.fixture()
def message_group_chat_page(client_utils_page: ClientUtilsPage):
    """
    群聊页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().message_tab_click().start_chat_btn_click().click_number_one_group()


@pytest.fixture(autouse=True)
def tear_down_message_page(client_utils_page: ClientUtilsPage):
    """
    自动返回消息tab
    :param client_utils_page:
    :return:
    """
    yield





