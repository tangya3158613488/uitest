from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 更新时间段
    good_voice_update_time = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/title_tv")'
    # 更新时间段和规则
    time_role = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/banner_rule_tv")'





class IOS:
    pass