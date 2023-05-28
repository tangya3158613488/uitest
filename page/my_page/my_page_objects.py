#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的tab
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 我的
    my_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")'
    # 全局播放器
    global_player_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/mini_player")'
    # 头像
    head_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imgHeadPhoto")'
    # 编辑资料btn
    edit_data_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layoutEdit")'
    # 昵称
    nick_name_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/textUserName")'
    # 会员等级
    vip_class_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imgMember")'
    # 关注
    attention_number_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关注")'
    # 粉丝
    fans_number_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layoutFans")'
    # 上榜
    announcement_number_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("上榜")'
    # todo 认证
    # 歌手等级
    singer_level_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/textSingerLevel")'
    # 财富等级
    rich_level_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/textSingerRick")'
    # 播放次数icon
    play_count_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("播放")'
    # 我的群组
    my_group_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的群组")'
    # 我的包房
    my_room_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的包房")'
    # 无包房时 我的包房展示
    my_room_create_room_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("创建房间")'
    # 资料tab
    data_tab_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("资料")'
    # 作品tab
    work_tab_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("作品")'
    # 动态tab
    dynamic_tab_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("动态")'
    # 收藏tab
    collect_tab_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().text("收藏")'
    # 活动tab
    activity_tab_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().text("活动")'
    # 音乐tab
    music_tab_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().text("音乐")'
    # 本地录音tab
    local_recording_tab_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("本地录音")'
    # 我的歌单tab
    my_songlist_tab_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的歌单")'
    # 播放全部
    play_number_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("播放全部")'
    # 作品tab下搜索btn
    work_tab_search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/search_btn")'
    # 作品tab下筛选btn
    work_tab_filter_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/filter_work_tv")'
    # 作品tab下 切换单双排btn
    work_tab_row_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rowTypeIv")'
    # 资料tab-相册
    photo_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的相册")'
    # 资料tab-信息
    data_data_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的信息")'
    # 资料tab-成就
    achievement_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的成就")'
    # 资料tab-赞过的
    liked_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("赞过的")'
    # 资料tab-转发
    forward_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的转发")'
    # 资料tab-群组
    groups_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的群组")'
    # 资料tab-包房
    room_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的包房")'
    # 资料tab-直播
    live_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的直播")'
    # 资料tab-二维码
    qr_code_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("二维码")'
    # 动态tab-发动态按钮
    send_dynamic_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发心情")'
    # 动态tab-动态评论按钮展示
    dynamic_say_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("送礼")'
    # 点击播放icon的弹窗
    play_icon_pop = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的作品共获得")'

class IOS:
    # 我的tab
    my_tab = MobileBy.IOS_PREDICATE, "label = '我的' AND type = 'XCUIElementTypeNavigationBar'"
    # 分享
    share_btn = MobileBy.IOS_PREDICATE, "label = '分享' AND type = 'XCUIElementTypeButton'"
    # 全局播放器
    global_player_btn = MobileBy.IOS_PREDICATE, "label = '全局播放器' AND type = 'XCUIElementTypeButton'"
    # 昵称
    nick_name_btn = MobileBy.IOS_PREDICATE, "name = 'nickName' AND type = 'XCUIElementTypeStaticText'"
    # 会员等级
    vip_class_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '会员等级' AND type = 'XCUIElementTypeButton'"
    # 播放
    play_number_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '播放' AND type = 'XCUIElementTypeButton'"
    # 关注
    attention_number_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '关注' AND type = 'XCUIElementTypeButton'"
    # 粉丝
    fans_number_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '粉丝' AND type = 'XCUIElementTypeButton'"
    # 上榜
    announcement_number_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '上榜' AND type = 'XCUIElementTypeButton'"
    # 我的群组
    my_group_btn = MobileBy.IOS_PREDICATE, "label CONTAINS '的群组' AND type = 'XCUIElementTypeButton'"
    # 我的包房
    my_room_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '我的包房' AND type = 'XCUIElementTypeButton'"
    # 资料tab
    data_tab_btn = MobileBy.IOS_PREDICATE, "label = '资料' AND type = 'XCUIElementTypeButton'"
    # 作品tab
    work_tab_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '作品' AND type = 'XCUIElementTypeButton'"
    # 动态tab
    dynamic_tab_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '动态' AND type = 'XCUIElementTypeButton'"
    # 音乐
    music_tab_btn = MobileBy.IOS_PREDICATE, "label = '音乐' AND type = 'XCUIElementTypeButton'"
    # 头像
    head_btn = MobileBy.IOS_PREDICATE, "label = '头像' AND type = 'XCUIElementTypeOther'"
    # 资料下的相册
    photo_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '我的相册' AND type = 'XCUIElementTypeOther' OR label BEGINSWITH 'Ta的相册' AND type = 'XCUIElementTypeOther'"
    # 动态评论
    dynamic_say_btn = MobileBy.IOS_PREDICATE, "label = '说点什么...' AND type = 'XCUIElementTypeStaticText'"
    # 音乐播放按钮
    music_play_btn = MobileBy.IOS_PREDICATE, "label = '播放' AND type = 'XCUIElementTypeOther'"
