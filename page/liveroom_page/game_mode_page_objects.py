from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 工具箱清空魅力值按钮文案
    clear_charm_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清空全部魅力值")'


class IOS:
    pass