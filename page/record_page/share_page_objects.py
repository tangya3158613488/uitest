from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 分享页标题"分享"
    share_title = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba:id/txt_share')"
    # 关闭按钮
    close_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba:id/share_close_btn')"


class IOS:
    pass
