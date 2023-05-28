#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab-官方通知
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    official_message_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("通知")'


class IOS:

    official_message_title = MobileBy.IOS_PREDICATE, "label = '通知' AND type = 'XCUIElementTypeOther'"
