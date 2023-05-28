from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 实时合唱title元素
    real_time_chrous_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("实时合唱")'
    # 与他合唱btn元素
    chrous_with_him_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("与他合唱")'
    # 开始合唱btn元素
    start_chrous_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("开始合唱")'


class IOS:
    # 实时合唱title元素
    real_time_chrous_title = MobileBy.IOS_PREDICATE, 'label = "实时合唱" AND type = "XCUIElementTypeStaticText"'
    # 与他合唱btn元素
    chrous_with_him_btn = MobileBy.IOS_PREDICATE, 'label = "与TA合唱" AND type = "XCUIElementTypeButton"'
    # 开始合唱btn元素
    start_chrous_btn = MobileBy.IOS_PREDICATE, 'label = "开始合唱" AND type = "XCUIElementTypeButton"'
