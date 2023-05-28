from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 房间有人，点击创建房间直接进入房间
    creat_room_virify=MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/root_layout")', 0
    # creat_room_virify = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/foreground_img")', 1


class IOS:
    # 我的tab中的收藏房间文案
    collect_room_text = MobileBy.IOS_PREDICATE, 'label = "收藏房间"'
    # 我的tab中的守护房间文案
    guard_room_text = MobileBy.IOS_PREDICATE, 'label = "守护房间"'
    # 我的tab中的历史访问文案
    history_room_text = MobileBy.IOS_PREDICATE, 'label = "历史访问"'
    # 各房间模块右侧的“收起”按钮
    stow_btn = MobileBy.IOS_PREDICATE, 'label = "收起"'
    # 各房间模块右侧的“展开”按钮
    expend_btn = MobileBy.IOS_PREDICATE, 'label = "展开"'
    # 收藏房间-“展开更多”按钮
    expend_more_collect_room = MobileBy.IOS_PREDICATE, 'label = "展开更多"'

    # 收藏模块内无房间的默认文案
    no_collect_room_text = MobileBy.IOS_PREDICATE, 'label = "暂时还没有收藏的房间，点击房间左上角的收藏按钮即可收藏成功哦~"'
    # 守护模块内无房间的默认文案
    no_guard_room_text = MobileBy.IOS_PREDICATE, 'label = "暂时还没有守护房间哦~快去守护你喜欢的房间吧~"'
    # 历史模块内无房间的默认文案
    no_history_room_text = MobileBy.IOS_PREDICATE, 'label = "暂时还没有留下你的脚印哦~快去找个房间看看吧！"'

    # 创建房间
    create_room = MobileBy.IOS_PREDICATE, 'label = "创建房间"'
    create_room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 1

    # 我的房间
    my_room_tag = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeImage" AND name = "ktv_lr_mychannel_myroom_tag"'
    my_room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 1
    # 房主：**/XCUIElementTypeStaticText[`label == "XXXX"`][1]
    # 公告：**/XCUIElementTypeStaticText[`label == "欢迎XXX"`][1]

    # 收藏房间cell
    collect_room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 2
    # 删除收藏房间按钮
    delete_collect_room = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeButton"', 1

    # 仅展开守护房间
    # 取第一个守护房间cell
    guard_room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 2
    # 删除收藏房间按钮
    delete_guard_room = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeButton"', 1

    # 仅展开历史访问
    # 取第一个历史房间cell
    history_room_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 2
    # 删除收藏房间按钮
    delete_history_room = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeButton"', 1
