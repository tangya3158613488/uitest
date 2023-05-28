#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 推荐用户头像
    recommend_user_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_icon")'
    # 推荐用户名字
    recommend_user_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_name")'
    # 推荐用户关注按钮
    recommend_user_attention = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/follow_btn")'


class IOS:
    pass
