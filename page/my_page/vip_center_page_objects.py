#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
会员中心页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 会员中心title
    vip_center_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("会员中心")'


class IOS:
    # 会员中心title
    vip_center_title = MobileBy.IOS_PREDICATE, "label = '会员中心' AND type = 'XCUIElementTypeStaticText'"
