"""
全局播放器-我的-我的收藏
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # title
    title = MobileBy.IOS_PREDICATE, "name = '我的收藏'"

    # 作品cell列表
    cell_list = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeCell' AND visible = true"

    # 空页面文案
    empty_text = MobileBy.IOS_PREDICATE, "name = '没有播放历史'"
