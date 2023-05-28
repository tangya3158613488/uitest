"""
我的tab -- 我的直播页面
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 开始直播按钮
    start_live_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("开始直播")'


class IOS:
    pass