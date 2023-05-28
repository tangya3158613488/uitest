#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息-礼物通知页
"""

from appium.webdriver.common.mobileby import MobileBy



class Android:
    pass


class IOS:
    gift_title = MobileBy.IOS_PREDICATE, "label = '礼物' AND type = 'XCUIElementTypeOther'"