#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

class Android:
    # 导出歌曲按钮
    export_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("导出歌曲")'
    # vip_icon
    vip_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/more_action_vip_label")'
    # 导出MP3
    export_mp3_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("导出为MP3并保存至手机里")'
    # 导出MP4
    export_mp4_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("导出为MV并保存至手机里")'
    # 我的导出记录
    my_export_record_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的导出记录")'
    # 立即续费 按钮
    renewal_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("立即续费")'
    # 开通会员 按钮
    opening_member = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("开通会员")'
    # 我的导出记录 title
    my_export_record_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的导出记录")'
    # 立即开通
    Open_immediately = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认协议并现在开通")'


    # 查看歌曲主页
    view_song_home = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查看歌曲主页")'
    # 我要演唱
    singing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我要演唱")'


    # 弹幕
    barrage_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("弹幕")'

    # 收录至歌单
    includ_playlist_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("收录至歌单")'
    my_song_list = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_list_songnum")'

    # toast
    toast = MobileBy.XPATH, "//*[@class='android.widget.Toast']"

    # 设置振铃
    set_ringing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设置振铃")'
    # 确定导出
    confirm_export_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定导出")'
    # 设置本地铃声
    set_local_ringing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设置本地铃声")'


    # 自动跳过前奏
    skip_prelude_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自动跳过前奏")'
    # 取消跳过前奏
    cancel_skip_prelude_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消跳过前奏")'
    # 一键投瓶
    throw_bottle_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("一键投瓶")'
    # 定时关闭
    timing_close_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("定时关闭")'
    # 举报
    report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("举报")'
    # 弹幕
    barrage_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("弹幕")'





