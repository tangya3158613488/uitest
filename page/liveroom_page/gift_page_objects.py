from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 免费鲜花
    free_flowers_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("免费鲜花")'
    # 财富等级查看按钮id
    wealth_level_page_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_wealth_right")'
    #在线成员列表元素
    room_users_info_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/room_users_info")'
    #在线成员列表标题
    room_users_info_title_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("在线成员列表")'



class IOS:
    pass