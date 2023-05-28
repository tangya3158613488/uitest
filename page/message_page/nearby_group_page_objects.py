"""
附近群组页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    nearby_group_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("附近群组")'


class IOS:

    nearby_group_title = MobileBy.IOS_PREDICATE, "label = '附近群组' AND type='XCUIElementTypeOther'"
