#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wuqiongxue
import pytest

from page.global_player_page.global_player_page import GlobalPlayerPage
from page.home_page.home_page import HomePage
from page.public_page.client_utils_page import ClientUtilsPage


@pytest.fixture()
def home_page(client_utils_page: ClientUtilsPage):
    """
    home tab页
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().home_tab_click()


@pytest.fixture(autouse=True)
def tear_down_home_page(client_utils_page: ClientUtilsPage):
    """
    自动返回页面
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
    return client_utils_page.go_to_tab_bar_master().home_tab_click().attention_all_click()


@pytest.fixture(autouse=True)
def tear_down_attention_all_page(client_utils_page: ClientUtilsPage):
    """
    自动返回首页
    :param client_utils_page:
    :return:
    """
    yield


@pytest.fixture()
def attention_work_page(client_utils_page: ClientUtilsPage):
    """
    首页关注作品
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().home_tab_click().attention_work_click()


@pytest.fixture()
def attention_dynamic_page(client_utils_page: ClientUtilsPage):
    """
    首页关注动态
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().home_tab_click().attention_dynamic_click()


@pytest.fixture()
def city_page(client_utils_page: ClientUtilsPage):
    """
    首页同城动态
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar().home_tab_click().city_click()


@pytest.fixture()
def hot_page(client_utils_page: ClientUtilsPage):
    """
    首页-热门
    :param client_utils_page:
    :return:
    """
    return client_utils_page.go_to_tab_bar_master().home_tab_click().hot_tab_click()


@pytest.fixture()
def home_search_page(home_page: HomePage):
    """
    首页-热门
    :param home_page:
    :return:
    """
    return home_page.hot_tab_click().click_search_btn()


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
def global_player_page(home_page: HomePage):
    """
    首页-全局播放器
    :param home_page:
    :return:
    """
    return home_page.global_player_btn_click()


@pytest.fixture()
def xiaochang_fm_page(global_player_page: GlobalPlayerPage):
    """
    首页-全局播放器-小唱FM
    :param global_player_page:
    :return:
    """
    return global_player_page.switch_to_xiaochang_fm_tab()


@pytest.fixture()
def listening_page(global_player_page: GlobalPlayerPage):
    """
    首页-全局播放器-正在收听
    :param global_player_page:
    :return:
    """
    return global_player_page.switch_to_listening_tab()


@pytest.fixture()
def global_player_my_page(global_player_page: GlobalPlayerPage):
    """
    首页-全局播放器-正在收听
    :param global_player_page:
    :return:
    """
    return global_player_page.switch_to_my_tab()
