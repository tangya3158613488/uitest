"""
相册（我的/Ta的相册）
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 相册页面title
    photo_album_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("头像相册")'


class IOS:
    # 歌单页面title
    photo_album_title = MobileBy.IOS_PREDICATE, "label CONTAINS '的相册' AND type = 'XCUIElementTypeOther'"
