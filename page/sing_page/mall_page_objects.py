from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 商城页面title元素
    mall_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商城")'


class IOS:
    # 商城页面title元素
    mall_page_title = MobileBy.IOS_PREDICATE, 'label = "商城" AND type = "XCUIElementTypeStaticText"'
