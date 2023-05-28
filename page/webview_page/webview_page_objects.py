from appium.webdriver.common.mobileby import MobileBy


class Android:
    web_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'


class IOS:
    web_view = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeWebView" AND visible = true'
