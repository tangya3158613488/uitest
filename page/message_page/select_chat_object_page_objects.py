#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab-更多-发起聊天-选择聊天对象页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 群组列表
    group_list = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.RelativeLayout")'
    # 选择聊天对象
    select_chat_object_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("选择聊天对象")'
    # 搜索框
    search_chat_object_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/placeholder_btn")'
    # 输入框
    input_chat_object_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/search_text")'
    # 进入私聊页
    private_chat_user_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("玛卡巴卡")'
    # 搜索按钮
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/search_btn")'
    # 找人按钮
    search_people_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 关注啊下的第一个人
    top_one = MobileBy.XPATH, '//*[@resource-id="android:id/list"]/android.widget.RelativeLayout[6]'
class IOS:
    # 进入私聊页
    private_chat_user_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '我你他她它祂' AND type = 'XCUIElementTypeStaticText'"
    #title 选择聊天对象
    select_chat_object_title = MobileBy.IOS_PREDICATE, "label = '选择聊天对象'"
    #搜索框
    search_chat_object_btn = MobileBy.IOS_PREDICATE, "label = '搜索聊天对象' AND type='XCUIElementTypeSearchField'"
    #输入框
    input_chat_object_btn = MobileBy.IOS_PREDICATE, "label = '搜索聊天对象' AND type='XCUIElementTypeSearchField'"
    #找人按钮
    search_people_btn = MobileBy.IOS_PREDICATE, "label = '找人' AND type='XCUIElementTypeButton'"
    #我关注的人
    me_attention_people_txt = MobileBy.IOS_PREDICATE, "label = '我关注的人' AND type='XCUIElementTypeStaticText'"
    #我加入的群组
    me_add_group_txt = MobileBy.IOS_PREDICATE, "label = '我加入的群组' AND type='XCUIElementTypeStaticText'"
    #user列表
    user_list = MobileBy.IOS_PREDICATE,"name = 'nickName' AND type='XCUIElementTypeStaticText'"
    # group列表
    group_list = MobileBy.IOS_PREDICATE, "type='XCUIElementTypeCell'"



