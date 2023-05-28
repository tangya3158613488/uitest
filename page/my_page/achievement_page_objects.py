"""
成就
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 成就title
    achievement_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("成就")'

class IOS:
    pass
