from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 任务中心title元素
    task_center_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("任务中心")'
    # 房间cell元素
    room_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/root_layout")', 0
    # '更多'按钮元素
    more_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_more_iv")'
    # '榜单'按钮元素
    rank_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_board_iv")'
    # '房间'id元素
    room_id_text = \
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ktv_room_owner_room_name")'


class IOS:
    # 任务中心title元素
    task_center_title = MobileBy.IOS_PREDICATE, 'label = "任务中心"'
