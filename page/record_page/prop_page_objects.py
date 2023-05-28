from appium.webdriver.common.mobileby import MobileBy


class IOS:
    # 道具_无
    prop_no_item = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell" AND label = "无"', 0
    # 所有道具
    prop_items = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"'
    # 道具_惊吓
    prop_scare = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell" AND label = "惊吓"'
    # 道具面板
    prop_broad = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCollectionView"'


class Android:
    # 道具_无
    prop_no_item = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/clear_prop_btn")'
    # 所有道具
    prop_items = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/effect_image")'
    # 道具_惊吓
    prop_scare = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/effect_image")', 2
    # 道具面板
    prop_broad = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/view_pager")'

