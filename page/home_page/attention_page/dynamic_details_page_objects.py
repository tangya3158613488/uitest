#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wuqiongxue
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 确认按钮
    comment_count = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/comment_count")'
    # 评论键盘框
    content = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content")'


class IOS:
    pass
