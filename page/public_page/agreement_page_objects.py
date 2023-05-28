from appium.webdriver.common.mobileby import MobileBy

class Android:

    # 用户协议与隐私保护-同意tab
    agree_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("同意")'

    # 用户协议与隐私保护-不同意tab
    disagree_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("不同意")'