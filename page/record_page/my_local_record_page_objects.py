#!/usr/bin/python
# coding=utf-8
# author:zhangjiao

from appium.webdriver.common.mobileby import MobileBy


class Android:
    title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本地录音")'


class IOS:
    # 页面title
    title = MobileBy.IOS_PREDICATE, "label = '我的本地录音' AND type in { 'XCUIElementTypeStaticText','XCUIElementTypeOther'}"
