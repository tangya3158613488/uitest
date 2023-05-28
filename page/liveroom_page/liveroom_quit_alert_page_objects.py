from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 退出房间时弹窗文案
    title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/title")'
    # 退出房间时弹窗中"退出"按钮
    quit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("退出")'
    # 退出房间时弹窗中"最小化"按钮
    small_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("最小化")'


class IOS:
    # 退出房间时弹窗文案
    title = MobileBy.IOS_PREDICATE, 'label = "即将离开房间，是否确认退出？"'
    # 退出房间时弹窗中"退出"按钮
    quit_btn = MobileBy.IOS_PREDICATE, 'label = "退出"'
    # 退出房间时弹窗中"最小化"按钮
    small_btn = MobileBy.IOS_PREDICATE, 'label = "最小化"'
