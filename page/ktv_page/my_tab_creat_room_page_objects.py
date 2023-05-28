from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 包房底部按钮
    ktv = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/operation_button_bg")'
    # 退出包房按钮
    quit = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'
    # 创建房间弹窗
    # collect_room_alert = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/live_discovery_mine_room_top_mineroom")")'
    # 编辑房间标题文案
    edit_room_name_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑房间标题")'
    # 房间玩法文案
    room_playmode_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("房间玩法")'
    # 取消按钮
    cancel_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    # 确认按钮
    queren_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm")'

    # 房间名称输入框
    room_name_text_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSslector().resourceId("com.changba:id/room_name_edit_text")'
    # 房间玩法-KTV
    room_playmode_ktv = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("KTV")'
    # 房间玩法-唱聊
    room_playmode_claw = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("唱聊")'
    # 房间玩法-竞拍
    room_playmode_auction = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("竞拍")'
    # 房间玩法-游戏
    room_playmode_mc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("游戏")'
    # 房间玩法-抢唱
    room_playmode_grab_sing = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("抢唱")'


class IOS:
    # 创建房间弹窗
    collect_room_alert = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeOther"', 2
    # 编辑房间标题文案
    edit_room_name_text = MobileBy.IOS_PREDICATE, 'label = "编辑房间标题"'
    # 房间玩法文案
    room_playmode_text = MobileBy.IOS_PREDICATE, 'label = "房间玩法"'
    # 取消按钮
    cancel_btn = MobileBy.IOS_PREDICATE, 'label = "取消" AND type = "XCUIElementTypeButton"'
    # 确认按钮
    queren_btn = MobileBy.IOS_PREDICATE, 'label = "确认" AND type = "XCUIElementTypeButton"'

    # 房间名称输入框
    room_name_text_view = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeTextView"'
    # 房间玩法-KTV
    room_playmode_ktv = MobileBy.IOS_PREDICATE, 'label = "KTV" AND type = "XCUIElementTypeButton"', 1
    # 房间玩法-唱聊
    room_playmode_claw = MobileBy.IOS_PREDICATE, 'label = "唱聊" AND type = "XCUIElementTypeButton"'
    # 房间玩法-竞拍
    room_playmode_auction = MobileBy.IOS_PREDICATE, 'label = "竞拍" AND type = "XCUIElementTypeButton"'
    # 房间玩法-游戏
    room_playmode_mc = MobileBy.IOS_PREDICATE, 'label = "游戏" AND type = "XCUIElementTypeButton"'
    # 房间玩法-抢唱
    room_playmode_grab_sing = MobileBy.IOS_PREDICATE, 'label = "抢唱" AND type = "XCUIElementTypeButton"'
