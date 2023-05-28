"""
我的tab -- 歌手等级
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌手等级页面title
    singer_grade_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌手等级")'


class IOS:
    pass