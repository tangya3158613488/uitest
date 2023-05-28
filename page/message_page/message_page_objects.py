#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息tab
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 更多按钮
    more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 添加好友
    add_friend_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("添加好友")'
    # 发起聊天
    start_chat_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发起聊天")'
    # 搜索按钮
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'
    # 粉丝
    fans_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("粉丝")'
    # 官方通知
    official_message_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/official_notice_container")'
    # 歌友召集
    broadcast_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/message_item_container")'
    # 发现群组
    find_group_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发现群组")'
    # 我的群组
    my_group_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的群组")'
    # 取消
    close_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
class IOS:
    #我你他
    private_chat_user_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '我你' AND type = 'XCUIElementTypeStaticText'"

    # 消息tab
    message_tab = MobileBy.IOS_PREDICATE, "label = '消息' AND type = 'XCUIElementTypeNavigationBar'"
    # 搜索按钮
    search_btn = MobileBy.IOS_PREDICATE, "label = '搜索' "
    # 更多按钮
    more_btn = MobileBy.IOS_PREDICATE, "label = '更多' "
    # 首页全局播放器
    global_player_btn = MobileBy.IOS_PREDICATE, "label = '全局播放器' AND type = 'XCUIElementTypeButton' "
    # 我的群组
    my_group_btn = MobileBy.IOS_PREDICATE, "label = '我的群组' "
    # 发现群组
    find_group_btn = MobileBy.IOS_PREDICATE, "label = '发现群组' "
    # 快速找群
    quick_find_group_btn = MobileBy.IOS_PREDICATE, "label = '快速找群' "
    # 粉丝
    fans_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '粉丝通知' "
    #AND type = 'XCUIElementTypeCell
    # 互动通知
    interact_inform_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '互动通知'  "
    # 礼物通知
    gift_inform_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '礼物通知'"
    #官方消息
    official_message_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '官方通知'  "
    # 寻人广播
    broadcast_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '寻人广播' OR label BEGINSWITH '歌友召集'  "
    # 发起聊天
    start_chat_btn = MobileBy.IOS_PREDICATE, "label = '发起聊天' "
    # 添加好友
    add_friend_btn = MobileBy.IOS_PREDICATE, "label = '添加好友' "





