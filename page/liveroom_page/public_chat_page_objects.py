from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 工具箱清空魅力值按钮文案
    clear_charm_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清空全部魅力值")'
    # 房间cell元素
    report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("举报")'
    #在线成员列表元素
    room_users_info_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/room_users_info")'
    #在线成员列表标题
    room_users_info_title_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("在线成员列表")'



class IOS:
    pass