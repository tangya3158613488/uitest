#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
关注
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 关注title
    attention_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关注")'

class IOS:
    # 关注title
    attention_title = MobileBy.IOS_PREDICATE, "label = '关注' AND type = 'XCUIElementTypeOther'"
