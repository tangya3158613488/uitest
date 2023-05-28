"""
我的tab -- 二维码页面
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 二维码title
    qr_code_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("二维码")'
    # 分享主页按钮
    share_home_page_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分享主页")'
    # 分享二维码按钮
    share_qr_code_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分享二维码")'


class IOS:
    pass