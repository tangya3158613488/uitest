"""
我的tab -- 财富等级
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌手等级页面title
    wealth_grade_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("财富等级")'


class IOS:
    pass