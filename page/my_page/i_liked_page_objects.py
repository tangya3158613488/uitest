"""
我的tab -- 我赞过的
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 页面title
    i_liked_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我赞过的")'


class IOS:
    pass