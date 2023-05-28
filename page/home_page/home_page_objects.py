#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 左上角榜单
    rank_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_ranking_list")'
    # 首页顶部关注点击
    attetion_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关注")'
    # 首页顶部广场点击
    hot_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("广场")'
    # 首页顶部直播点击
    live_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("直播")'
    # 首页顶部同城
    city_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tab_layout_id_0")',3
    # 首页关注全部
    attention_all_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部")'
    # 首页关注作品
    attention_work_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品")'
    # 首页关注动态
    attention_dynamic_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("动态")'
    # 首页搜索
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_search")'
    # 首页搜索
    search_btn2 = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchCl")'
    # 首页全局播放器
    global_player_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/mini_player")'


class IOS:
    # 左上角榜单
    rank_btn = MobileBy.IOS_PREDICATE, "label = '榜单' AND type = 'XCUIElementTypeButton'"
    # 左上角榜单
    rank_tab = MobileBy.IOS_PREDICATE, "label = '榜单' AND type = 'XCUIElementTypeButton'"
    # 首页顶部关注点击
    attetion_btn = MobileBy.IOS_PREDICATE, "label = '关注' AND type = 'XCUIElementTypeButton'"
    # 首页关注全部
    attention_all_btn = MobileBy.IOS_PREDICATE, "label = '全部' AND type = 'XCUIElementTypeButton'"
    # 首页顶部热门点击
    hot_btn = MobileBy.IOS_PREDICATE, "label = '广场' AND type = 'XCUIElementTypeButton'"
    # 首页顶部同城
    city_btn = MobileBy.IOS_PREDICATE, "name BEGINSWITH 'tabBtn' AND type = 'XCUIElementTypeButton' AND index=3 "
    # 首页搜索
    search_btn = MobileBy.IOS_PREDICATE, "label = '搜索' AND type = 'XCUIElementTypeButton'"
    # 首页全局播放器
    global_player_btn = MobileBy.IOS_PREDICATE, "label = '全局播放器' AND type = 'XCUIElementTypeButton'"