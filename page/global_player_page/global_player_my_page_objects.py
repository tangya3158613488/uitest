"""
全局播放器-我的
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 播放全部按钮
    play_all_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("播放全部")'
    # 播放历史
    player_history_entrance = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("播放历史")'
    # 歌单
    song_sheet_entrance = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌单")'
    # 收藏
    collect_entrance = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("收藏")'
    # 作品列表
    work_cell_list = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/work_1st_line")'

class IOS:
    # 播放全部按钮
    play_all_btn = MobileBy.IOS_PREDICATE, "name ='播放全部' AND type ='XCUIElementTypeStaticText' AND visible =true"

    # 播放历史
    player_history_entrance = MobileBy.IOS_PREDICATE, "name BEGINSWITH '播放历史'"

    # 歌单
    song_sheet_entrance = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeStaticText' AND name BEGINSWITH '歌单'"

    # 收藏
    collect_entrance = MobileBy.IOS_PREDICATE, "name BEGINSWITH '收藏' AND NOT name IN {'收藏', '已收藏'} AND type = 'XCUIElementTypeStaticText' AND visible = true"

    # 作品列表
    work_cell_list = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeCell' AND visible = true"
