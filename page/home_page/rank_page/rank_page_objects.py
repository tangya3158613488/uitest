from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 榜单右侧总榜
    total_rank_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'


class IOS:
    # 榜单右侧总榜
    total_rank_btn = MobileBy.IOS_PREDICATE, 'label = "总榜" AND type = "XCUIElementTypeButton"'
