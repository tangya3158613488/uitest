#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
私聊-相机
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    camera_roll_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("相机胶卷")'


class IOS:
    camera_roll_title = MobileBy.IOS_PREDICATE, "label = '相机胶卷' AND type = 'XCUIElementTypeOther'"