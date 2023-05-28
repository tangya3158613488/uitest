"""
我的tab -- 主页装扮页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 主页装扮title
    home_page_dress_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("主页装扮")'


class IOS:
    pass