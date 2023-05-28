#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的粉丝页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 粉丝title
    my_fans_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的粉丝")'


class IOS:
    # 粉丝title
    my_fans_title = MobileBy.IOS_PREDICATE, "label = '粉丝' AND type = 'XCUIElementTypeStaticText' OR label CONTAINS '的粉丝' AND type='XCUIElementTypeOther'"
