"""
我的tab -- 上榜记录页面
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 上榜记录 title
    list_record_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("上榜记录")'


class IOS:
    pass