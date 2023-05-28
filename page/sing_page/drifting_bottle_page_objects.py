from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 漂流瓶页面title元素
    drifting_bottle_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("漂流瓶")'


class IOS:
    # 漂流瓶页面title元素
    drifting_bottle_page_title = MobileBy.IOS_PREDICATE, 'name = "漂流瓶" AND visible = true'
