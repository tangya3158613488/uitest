#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab-互动通知页
"""

from appium.webdriver.common.mobileby import MobileBy



class Android:
    pass


class IOS:
    interact_title = MobileBy.IOS_PREDICATE, "label IN {'评论','点赞'}"