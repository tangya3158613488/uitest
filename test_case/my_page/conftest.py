#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
import pytest

from page.public_page.client_utils_page import ClientUtilsPage


@pytest.fixture()
def main_my_page(client_utils_page: ClientUtilsPage):
    """
    my tab页 主态
    :param client_utils_page:
    :return:
    """
    # return client_utils_page.go_to_tab_bar_master().my_tab_click().swipe_down_page()
    # return client_utils_page.go_to_tab_bar_master().my_tab_click()
    return client_utils_page.go_to_tab_bar_master().home_tab_click().my_tab_click()
@pytest.fixture()
def customer_my_page(client_utils_page: ClientUtilsPage):
    """
    my 个人主页客态
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().message_tab_click().add_friend_btn_click().personal_page_btn()
