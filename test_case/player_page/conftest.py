#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wuqiongxue
import pytest

from page.home_page.home_page import HomePage
from page.public_page.client_utils_page import ClientUtilsPage


@pytest.fixture()
def attention_hot_page(client_utils_page: ClientUtilsPage):
    """
    home 热门页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().home_tab_click().hot_tab_click()


@pytest.fixture(autouse=True)
def tear_down_hot_page(client_utils_page: ClientUtilsPage):
    """
    自动返回热门页面
    :param client_utils_page:
    :return:
    """
    yield


@pytest.fixture()
def attention_all_page(client_utils_page: ClientUtilsPage):
    """
    首页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar().home_tab_click().attention_all_click()


@pytest.fixture(autouse=True)
def tear_down_attention_all_page(client_utils_page: ClientUtilsPage):
    """
    自动返回首页
    :param client_utils_page:
    :return:
    """
    yield


@pytest.fixture()
def hot_page(client_utils_page: ClientUtilsPage):
    """
    首页-热门
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar().home_tab_click().hot_tab_click()


@pytest.fixture()
def home_search_page(home_page: HomePage):
    """
    首页-热门
    :param home_page:
    :return:
    """
    return home_page.click_search_btn()


@pytest.fixture()
def home_search_result_page(home_page: HomePage, request):
    """

    :param home_page:
    :param request:
    :return:
    """
    param = request.param
    home_search_result_page_obj = home_page.click_search_btn().search_song_by_keyword(param["keyword"])
    return home_search_result_page_obj, param


@pytest.fixture()
def work_rank_page(home_page: HomePage):
    """
    首页-榜单
    :param home_page:
    :return:
    """
    return home_page.work_rank_click()


@pytest.fixture()
def home_page(client_utils_page: ClientUtilsPage):
    """
    home tab页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().home_tab_click()
