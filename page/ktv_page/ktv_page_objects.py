from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 推荐tab
    recommend_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("推荐")'
    my_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("我的")'
    # 实时合唱title元素
    real_time_chorus_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("实时合唱")'
    # 房间cell元素
    room_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/root_layout")', 0
    #ktv首页我tab元素
    my_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")'
    #我的页面我的房间
    my_room = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("哄哄你木木木哦")'


class IOS:
    # 推荐tab
    recommend_tab = MobileBy.IOS_PREDICATE, 'label == "推荐"'
    # 我的tab
    my_tab = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND value = "我的" AND visible = True'

    # 北京tab
    location_beijing_tab = MobileBy.IOS_PREDICATE, 'label == "北京"'
    # 家族tab
    family_tab = MobileBy.IOS_PREDICATE, 'label == "家族"'
    # 聊天室tab
    chatroom_tab = MobileBy.IOS_PREDICATE, 'label == "聊天室"'
    # 游戏tab
    gameroom_tab = MobileBy.IOS_PREDICATE, 'label == "游戏"'
    # 打boss tab
    bossroom_tab = MobileBy.IOS_PREDICATE, 'label == "打boss"'

    # 右上角搜索按钮 -> 包房首页搜索
    nav_search_tab = MobileBy.IOS_PREDICATE, 'label == "搜索"'
    # 右上角榜单按钮 -> 包房首页榜单
    nav_rank_tab = MobileBy.IOS_PREDICATE, 'label == "排行榜"'
