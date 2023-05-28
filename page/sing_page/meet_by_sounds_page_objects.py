from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 漂流瓶页面title元素
    meet_by_sounds_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("以声相遇")'


class IOS:
    # 漂流瓶页面title元素
    meet_by_sounds_page_title = MobileBy.IOS_PREDICATE, 'label = "以声相遇" AND type = "XCUIElementTypeStaticText"'
