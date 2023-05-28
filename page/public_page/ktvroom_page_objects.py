from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 首页ktv tab
    my_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")'


class IOS:
    # 首页ktv tab
    ktv_tab = MobileBy.IOS_PREDICATE, 'label = "KTV"'