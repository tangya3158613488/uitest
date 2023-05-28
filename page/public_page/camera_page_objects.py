#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
from appium.webdriver.common.mobileby import MobileBy


class Android:
    view_finder = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("拍照")'


class IOS:

    view_finder = MobileBy.IOS_PREDICATE, "label = '取景器' AND type = 'XCUIElementTypeImage'"


