#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 首页关注小火车头像
    train_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/live_user_name_tv")'
    # 首页关注小火车卡片
    train_card = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/state_tv")'
    # 首页关注用户头像
    head_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/iv_feed_head_portrait")'
    # 首页关注用户名称
    head_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 发动态
    send_dynamic_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_focus_send")'
    # 首页关注点赞
    zan_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_focus_zan")'
    # 关注_动态zan
    dynamic_zan_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_comment_zan")'
    # 关注_动态评论
    dynamic_comment_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_comment_comment")'
    # 关注_动态说点什么
    dynamic_user_content = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_comment_user_content")'
    # 时间
    moment_time = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_head_time")'
    # 动态文字内容
    moment_content = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_head_collapse_content")'
    # 动态图片
    moment_image = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cl_moment_image_layout")'
    # 动态图片高清
    publish_preview = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/publish_preview_tv")'
    # 动态语音条
    audiobg = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/audiobg")'
    # 动态语音条播放按钮
    moment_audio_play = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/iv_moment_audio_play")'

    # 首页关注送礼
    gift_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_focus_gift")'
    # 首页关注评论
    comment_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_focus_comment")'
    # 首页关注分享
    share_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_footer_focus_share")'
    # 首页关注装扮
    dress_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_head_dress_click")'
    # 立即续费
    open_member = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/open_member_button")'
    # 话题
    topic_id = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/tv_feed_footer_label")'
    # 播放按钮
    play_btn = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/iv_works_state")'
    # 歌曲song name
    song_name = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/tv_works_song_name")'
    # 歌曲播放量
    song_num = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/tv_works_view_num")'
    # 作品id
    work_id = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/fl_works_card")'
    # 会员等级
    member_grade = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/imageview0")'
    # 头像展示ktv
    head_ktv = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/live_ktv_view")'


class IOS:
    # 首页关注小火车头像
    send_dynamic_id = MobileBy.IOS_PREDICATE, "label = '发动态' AND type = 'XCUIElementTypeStaticText'"

    # 首页关注点赞
    zan_id = MobileBy.IOS_PREDICATE, "label = '点赞' ", 0
    # 首页关注送礼
    gift_id = MobileBy.IOS_PREDICATE, "label = '送礼' AND type = 'XCUIElementTypeStaticText' AND visible = true", 0
    # 首页关注评论
    comment_id = MobileBy.IOS_PREDICATE, "label = '评论' ", 0
    # 首页关注分享
    share_id = MobileBy.IOS_PREDICATE, "label = '分享' AND type = 'XCUIElementTypeStaticText' AND visible = true", 0

