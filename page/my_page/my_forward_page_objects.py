"""
我的tab -- 我转发的 页面
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 页面title
    my_forward_works_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("转发的作品")'


class IOS:
    pass