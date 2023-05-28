from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 主播实名认证页面title元素
    live_real_name_identify_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("主播实名认证")'


class IOS:
    # 主播实名认证页面title元素
    live_real_name_identify_page_title = MobileBy.IOS_PREDICATE, 'label = "主播实名认证"'

