#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
找人页面
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 搜索用户输入框
    search_people_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/placeholder_btn")'
    # 搜索输入框
    search_people_input = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_input_box")'
    # 搜索按钮
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_search_submit")'
    # 搜索出来的用户
    search_user = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我你他她它祂")'
    # 找人title
    find_people_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("找人")'

class IOS:
    # 找人title
    find_people_title = MobileBy.IOS_PREDICATE, "label = '找人'"
    # 搜索用户输入框
    search_people_btn = MobileBy.IOS_PREDICATE, "label = '搜索用户'"
    #搜索输入框
    search_people_input = MobileBy.IOS_PREDICATE, "label BEGINSWITH '唱吧账号' AND type = 'XCUIElementTypeSearchField'"
    #搜索按钮
    search_btn = MobileBy.IOS_PREDICATE, "label in {'搜索', 'Search'} AND type = 'XCUIElementTypeButton'"
    #搜索出来的用户
    search_user = MobileBy.IOS_PREDICATE, "label BEGINSWITH '我你' AND type='XCUIElementTypeCell'"
