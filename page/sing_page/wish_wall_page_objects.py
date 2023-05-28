from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 漂流瓶页面title元素
    wish_wall_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("K歌心愿墙")'


class IOS:
    wish_wall_page_title = MobileBy.IOS_PREDICATE, 'label = "K歌心愿墙" AND type = "XCUIElementTypeStaticText"'
