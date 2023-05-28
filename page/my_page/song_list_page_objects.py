"""
歌单
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌单页面title
    song_list_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的歌单")'
    # 新建歌单弹窗title
    create_song_list_pop_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新建歌单")'


class IOS:
    # 歌单页面title
    song_list_title = MobileBy.IOS_PREDICATE, "label CONTAINS '的歌单' AND type = 'XCUIElementTypeOther'"
