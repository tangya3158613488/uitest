#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 直播页面作者名称
    room_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/live_room_anchor_name")'
    #直播关闭页面
    close = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/el_empty_close_iv")'
    # 我知道了
    i_know_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/live_double_click_follow_btn")'


class IOS:
    pass
