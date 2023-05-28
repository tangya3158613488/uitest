"""
我的tab -- 我的钱包
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 我的钱包title
    my_wallet_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的钱包")'


class IOS:
    pass