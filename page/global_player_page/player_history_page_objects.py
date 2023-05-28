"""
全局播放器-我的-播放历史
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # title
    title = MobileBy.IOS_PREDICATE, "name = '播放历史'"

    # 歌名列表
    song_name_list = MobileBy.IOS_PREDICATE, "name = 'songName'"

    # 昵称列表
    nick_name_list = MobileBy.IOS_PREDICATE, "name = 'nickName'"

    # 头像列表
    head_photo_list = MobileBy.IOS_PREDICATE, "name = 'headPhoto'"

    # 作品cell列表
    cell_list = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeCell'"

    # 空页面文案
    empty_text = MobileBy.IOS_PREDICATE, "name = '没有播放历史'"

    # 删除
    delete_btn = MobileBy.IOS_PREDICATE, "name = '清空'"

    # 清空全部
    clean_btn = MobileBy.IOS_PREDICATE, "name = '全部清除'"
