#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息-寻人广播/歌友召集
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    broadcast_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌友召集")'


class IOS:
    broadcast_title = MobileBy.IOS_PREDICATE, "label IN {'寻人广播','歌友召集'}"