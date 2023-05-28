from appium.webdriver.common.mobileby import MobileBy


class Android:
    # '拒绝'按钮元素
    refuse_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("拒绝")'
    # '更多'按钮元素
    more_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_more_iv")'
    # '关闭'按钮元素
    close_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_close_room_button")'
    # '榜单'按钮元素
    rank_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_board_iv")'
    # '房间'id元素
    room_id_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_room_owner_room_name")'
    # '工具箱'id元素
    toolbox_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tool_box_button")'
    # '签到'id元素
    sign_in_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/sign_in_button")'
    # '房间信息'id元素
    room_info_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("房间信息")'
    # '礼物箱' id元素
    gift_box_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/gift_box_button")'
    # '公聊'  id元素
    public_chat_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/public_chat_button")'

class IOS:
    # '更多'按钮元素
    more_btn_id = MobileBy.IOS_PREDICATE, 'label = "更多"'
    # '榜单'按钮元素
    rank_btn_id = MobileBy.IOS_PREDICATE, 'label = "排行榜"'
    # '房间'id元素
    room_id_text = MobileBy.IOS_PREDICATE, 'label CONTAINS "房间:" AND type = "XCUIElementTypeStaticText"'
