"""
全局播放器-我的-歌单
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # title
    title = MobileBy.IOS_PREDICATE, "name = '我的歌单'"
