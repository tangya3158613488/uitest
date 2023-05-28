#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 好友合唱title
    friends_chrous_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("好友合唱")'
    # 历史最佳合唱title
    history_best_chrous_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("历史最佳合唱")'
    # 今日最佳合唱title
    today_best_chrous_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("今日最佳合唱")'
    # 加入合唱btn
    join_chrous_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/semi_join_tv")'
    # 转发btn
    forwarding_work_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/forwarding_work")'

class IOS:
    pass
