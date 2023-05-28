#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息-粉丝页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    fans_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("粉丝")'


class IOS:
    #主态展示我的粉丝，客态展示xx的粉丝
    fans_title = MobileBy.IOS_PREDICATE, "label = '粉丝' AND type = 'XCUIElementTypeOther' OR label CONTAINS '的粉丝' AND type = 'XCUIElementTypeOther'"