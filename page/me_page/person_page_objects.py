#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 获取用户名称
    username_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_name_tv")'
    # 主页关注按钮
    user_attention = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/luxury_follow_btn")'
    # 取消关注
    cancel_attention = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消关注")'

class IOS:
    pass