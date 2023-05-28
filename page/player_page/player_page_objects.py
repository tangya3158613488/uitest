#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 礼物箱礼物tab
    gift_box = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("礼物")'
    # 评论
    comment = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tab_layout_id_0")', 1
    # 评论tab
    comment_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tab_layout_id_0")'
    # 分享弹窗第一个分享渠道名称
    share = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/share_item_name")'
    # 新版播放页 详情 tab
    details_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("详情")'
    # mp4关闭按钮
    close_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/close_mp4_gift_button")'
    # 关闭动画提示
    clone_mp4_tips = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关闭动画今日不再播放，确认关闭吗？")'
    # 确定btn
    confirm_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")'
    # 首次进到礼物箱长按礼物弹窗"我知道了"
    longpress_sendgift_window = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_i_known")'
    # 播放页作品名称
    work_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_song_name")'
    # 直播导流icon可见
    live_head_photo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/play_page_live_head_photo_iv_b")'
    # 歌词
    lyric = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/lyric_text")'
    # 更多btn
    more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'


class IOS:
    # 礼物箱礼物
    gift_box = MobileBy.IOS_PREDICATE, "label = '礼物' AND type = 'XCUIElementTypeStaticText'"
    # 评论
    comment = MobileBy.IOS_PREDICATE, "label = '评论' "
    # 分享
    share = MobileBy.IOS_PREDICATE, 'label="分享完整作品链接至"'
    # 首次进到礼物箱长按礼物弹窗"我知道了"
    longpress_sendgift_window = MobileBy.IOS_PREDICATE, "label = '我知道了'"

    # 详情tab
    detail_tab = MobileBy.IOS_PREDICATE, "label = '详情' "
