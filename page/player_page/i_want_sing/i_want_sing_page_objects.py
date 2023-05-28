#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

class Android:
    #录制页主题icon
    skin_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("主题")'
    #导入作品，伴奏列表title
    original_list_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("创作原声")'
    #清唱录制页title
    cantata_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清唱")'
    # 我要唱btn
    i_want_sing = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我要演唱")'
