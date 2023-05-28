from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 清唱title元素
    only_sing_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清唱")'
    # 演唱按钮元素
    sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("演唱")'


class IOS:
    # 清唱title元素
    only_sing_title = MobileBy.IOS_PREDICATE, 'label = "清唱" AND type = "XCUIElementTypeStaticText"'
    # 演唱按钮元素
    sing_btn = MobileBy.IOS_PREDICATE,  'label = "演唱" AND type = "XCUIElementTypeButton"'

