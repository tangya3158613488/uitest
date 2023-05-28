from appium.webdriver.common.mobileby import MobileBy


class Android:
    grant_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("授权")'

    i_see_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")'

    cannel_btn = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/cancel")'


class IOS:
    pass
