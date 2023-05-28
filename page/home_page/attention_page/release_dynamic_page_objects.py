#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wuqiongxue
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 确认按钮
    confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'


class IOS:
    # 确认按钮
    confirm = MobileBy.IOS_PREDICATE, "label = '确定' AND type = 'XCUIElementTypeButton'"
    # 发动态title
    pulbic_dynamic = MobileBy.IOS_PREDICATE, 'name="发动态" AND label="发动态" AND type="XCUIElementTypeStaticText" '
    # 发布按钮
    public_btn = MobileBy.IOS_PREDICATE, 'name="发布" AND label="发布" AND type="XCUIElementTypeButton"'
