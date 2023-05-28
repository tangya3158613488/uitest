#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息-群聊页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 底部更多btn
    add_more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_fl")'
    # 相册
    photo_album_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("相册")'
    # 拍照
    take_photo_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("拍照")'
    # 本地录音
    local_record_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本地录音")'
    # 我的作品
    my_production_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的作品")'
    # 真心话
    true_words_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("真心话")'
    # 我的房间
    my_room_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的房间")'
    # emoji btn
    emoji_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/emoji_fl")'
    # 最近使用按钮
    recently_used_btn = MobileBy.XPATH, "//android.widget.HorizontalScrollView/android.widget.LinearLayout[" \
                                        "1]/android.widget.FrameLayout[2] "
    # 语音 btn
    voice_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/left_btn")'
    # 请按住说话btn
    speak_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("请按住说话")'
    # 普通问题
    common_question_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("普通问题")'
    # 自己分享出去的包房
    my_room = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("立即")'
    # 发送语音消息为4秒
    send_voice = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")'
    # 全局播放器
    global_player_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/mini_player")'
class IOS:
    # 顶部title
    title_tab = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeNavigationBar'"
    # 更多btn
    more_btn = MobileBy.IOS_PREDICATE, "label = '更多' AND type = 'XCUIElementTypeButton'"
    # emoje btn
    emoji_btn = MobileBy.IOS_PREDICATE, "label = '切换表情输入' AND type = 'XCUIElementTypeButton'"
    # 语音 btn
    voice_btn = MobileBy.IOS_PREDICATE, "label = '切换语音输入' AND type = 'XCUIElementTypeButton' "
    # 请按住说话btn
    speak_btn = MobileBy.IOS_PREDICATE, "label = '请按住说话' AND type = 'XCUIElementTypeButton' "
    # 发送了语音
    send_voice = MobileBy.IOS_PREDICATE, "label CONTAINS '发送了语音消息'"
    # 底部更多btn
    add_more_btn = MobileBy.IOS_PREDICATE, "label = '更多输入' AND type = 'XCUIElementTypeButton'"
    # 全局播放器
    global_player_btn = MobileBy.IOS_PREDICATE, "label = '全局播放器' AND type = 'XCUIElementTypeButton' "
    # 返回按钮
    back_btn = MobileBy.IOS_PREDICATE, "label = '返回' AND type = 'XCUIElementTypeButton' "
    # 最近使用按钮
    recently_used_btn = MobileBy.IOS_PREDICATE, "label = '最近使用' AND type = 'XCUIElementTypeButton' "
    # 相册
    photo_album_btn = MobileBy.IOS_PREDICATE, "label = '相册' AND type = 'XCUIElementTypeCell' "
    # 拍照
    take_photo_btn = MobileBy.IOS_PREDICATE, "label = '拍照' AND type = 'XCUIElementTypeCell' "
    # 本地录音
    local_record_btn = MobileBy.IOS_PREDICATE, "label = '本地录音' AND type = 'XCUIElementTypeCell' "
    # 我的作品
    my_production_btn = MobileBy.IOS_PREDICATE, "label = '我的作品' AND type = 'XCUIElementTypeCell' "
    # 真心话
    true_words_btn = MobileBy.IOS_PREDICATE, "label = '真心话' AND type = 'XCUIElementTypeCell' "
    # 我的房间
    my_room_btn = MobileBy.IOS_PREDICATE, "label = '我的房间' AND type = 'XCUIElementTypeCell' "
    # 普通问题
    common_question_btn = MobileBy.IOS_PREDICATE, "label = '普通问题' AND  type='XCUIElementTypeButton' "
    # 敏感问题
    sensitive_question_btn = MobileBy.IOS_PREDICATE, "label = '敏感问题' AND  type='XCUIElementTypeButton' "
    # 自定义问题
    custom_question_btn = MobileBy.IOS_PREDICATE, "label = '自定义问题' AND  type='XCUIElementTypeButton' "
    # 自己分享出去的包房
    my_room = MobileBy.IOS_PREDICATE, "label CONTAINS '包房' "
