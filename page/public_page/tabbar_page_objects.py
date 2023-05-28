from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 首页ktv tab
    ktv_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/discovery")'
    # 首页唱歌 tab
    sing_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/singing")'
    # 首页 tab
    home_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_changba")'
    # 首页消息 tab
    message_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/message")'
    # 首页我的_tab
    me_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/me")'

class IOS:
    # 首页 tab
    home_tab = MobileBy.IOS_PREDICATE, "label = '首页' AND name = '首页' AND type = 'XCUIElementTypeButton'"
    # 首页ktv tab
    ktv_tab = MobileBy.IOS_PREDICATE, 'label = "KTV"  AND type = "XCUIElementTypeButton"'
    # 唱歌tab
    sing_tab = MobileBy.IOS_PREDICATE, "label = '点歌台' AND type = 'XCUIElementTypeButton'"
    # 消息tab
    message_tab = MobileBy.IOS_PREDICATE, "label BEGINSWITH '消息' AND type = 'XCUIElementTypeButton'"
    # 我的tab
    me_tab = MobileBy.IOS_PREDICATE, "label = '我的' AND name = '我的' AND type = 'XCUIElementTypeButton'"
