from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 你唱我听title元素
    sing_for_me_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("你唱我听")'
    # 实时合唱title元素
    real_time_chorus_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("实时合唱")'
    # 房间cell元素
    room_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/root_layout")', 0


class IOS:
    # 你唱我听title元素
    sing_for_me_id = MobileBy.IOS_PREDICATE, 'label = "你唱我听"'
    # 实时合唱title元素
    real_time_chorus_id = MobileBy.IOS_PREDICATE, 'label = "实时合唱"'
    # 劲爆抢唱title元素
    popup_sing_id = MobileBy.IOS_PREDICATE, 'label = "劲爆抢唱"'

    # 快速加入房间
    quickenter_room_btn = MobileBy.IOS_PREDICATE, 'label = "liveroom_quickenter_bg"'

    # 房间cell元素
    room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 5
    # 房间名称：**/XCUIElementTypeOther[`label == "唱聊房间XXXX"`]
    # 页面滑动

    # 好友歌友模块
    friends_view = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCollectionView"'
    first_friend_playmode = MobileBy.IOS_PREDICATE, 'name BEGINSWITH "liveroom_friends_header_tag"'
    first_friend_label = MobileBy.IOS_PREDICATE, 'label CONTAINS "正在包房排麦"'

    # 北京tab、家族、聊天室、游戏
    # 房间cell元素
    beijing_room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 1
    beijing_room_audience_amount = MobileBy.IOS_PREDICATE, 'label CONTAINS "观众数"'
    # 校验观众数大于0      label == "游戏房间,晴儿788888♥️游戏房,排麦数1, 观众数2693,"

    # 打boss
    # label == "KTV房间,【官方】打BOSS房间5,排麦数0, 观众数0,"
    # ** / XCUIElementTypeOther[`label == "垂直滚动条, 4页"`]（竖向可滑动几屏？）
    # ** / XCUIElementTypeOther[`label == "水平滚动条, 1页"`]
