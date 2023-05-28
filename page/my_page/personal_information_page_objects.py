#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的tab-编辑资料 --》个人信息页
"""

from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 编辑个人资料 title
    personal_information_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑个人资料")'


class IOS:
    #个人信息title
    personal_information_title = MobileBy.IOS_PREDICATE, "label = '个人信息' AND type in {'XCUIElementTypeStaticText','XCUIElementTypeOther'}"
