from appium.webdriver.common.mobileby import MobileBy


class Android:
    # '房间信息'按钮元素
    room_detail_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("房间信息")'
    # '反馈'按钮元素
    feedback_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("反馈")'
    # '举报'按钮元素
    report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("举报")'
    # '退出房间'按钮元素
    quit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("退出房间")'
    # '房间信息'id元素
    room_info_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("房间信息")'


class IOS:
    # '房间信息'按钮元素（iOS添加这块的元素改动较大，暂时没用上）
    room_detail_btn = MobileBy.IOS_PREDICATE, 'label = "房间信息"'
    # '反馈'按钮元素（iOS添加这块的元素改动较大，暂时没用上）
    feedback_btn = MobileBy.IOS_PREDICATE, 'label = "反馈"'
    # '举报'按钮元素（iOS添加这块的元素改动较大，暂时没用上）
    report_btn = MobileBy.IOS_PREDICATE, 'label = "举报"'
    # '退出房间'按钮元素（iOS添加这块的元素改动较大，暂时没用上）
    quit_btn = MobileBy.IOS_PREDICATE, 'label = "退出房间"'
