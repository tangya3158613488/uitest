from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 全部版本 页面title
    all_version_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部版本")'


class IOS:
    all_version_page_title = MobileBy.IOS_PREDICATE, 'label = "全部版本"'
