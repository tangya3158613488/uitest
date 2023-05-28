#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的群组页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 我的群组title
    my_group_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的群组")'
    # 客态用户的群组title
    other_group_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我你他她它祂的群组")'

class IOS:
    # 我的群组title
    my_group_title = MobileBy.IOS_PREDICATE, "label CONTAINS '我的的群组' AND type = 'XCUIElementTypeStaticText' OR label CONTAINS '的群组' AND type='XCUIElementTypeOther'"
