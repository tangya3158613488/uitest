#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的tab -- 最近来访页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 最近来访title
    lately_visit_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最近来访")'


class IOS:
    #最近来访title
    lately_visit_title = MobileBy.IOS_PREDICATE, "label = '最近来访' AND type = 'XCUIElementTypeStaticText'"
