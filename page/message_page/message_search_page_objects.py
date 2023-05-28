#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab-左上角查询
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 搜索页元素
    search_box = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索")'


class IOS:
    # 更多btn
    cancel_btn = MobileBy.IOS_PREDICATE, "label = '取消' AND type = 'XCUIElementTypeButton'"
    search_box = MobileBy.IOS_PREDICATE, "label = '搜索' AND type = 'XCUIElementTypeSearchField'"
