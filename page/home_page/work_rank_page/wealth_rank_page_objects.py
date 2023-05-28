from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 作品榜
    works_list_tab = MobileBy.IOS_PREDICATE, 'label ="作品榜" AND type ="XCUIElementTypeButton"'
    # 歌手榜
    singer_tab = MobileBy.IOS_PREDICATE, 'label = "歌手榜" AND type = "XCUIElementTypeButton"'
    # 财富榜
    wealth_tab = MobileBy.IOS_PREDICATE, 'label ="财富榜" AND type ="XCUIElementTypeButton"'
    # 音乐财富排行
    music_wealth_rank_title = MobileBy.IOS_PREDICATE, 'name="北京音乐财富排行" AND type = "XCUIElementTypeButton"'
    # 包房财富排行
    room_wealth_rank_title = MobileBy.IOS_PREDICATE, 'name="北京包房财富排行" AND type = "XCUIElementTypeButton"'
    # 全国音乐财富排行
    nation_music_wealth_rank_title = MobileBy.IOS_PREDICATE, 'name="全国音乐财富排行" AND type = "XCUIElementTypeButton"'
    # #全国包房财富
    nation_room_wealth_rank_title = MobileBy.IOS_PREDICATE, 'name="全国包房财富排行" AND type = "XCUIElementTypeButton"'
    # 全国直播财富
    nation_live_wealth_rank_title = MobileBy.IOS_PREDICATE, 'name="全国直播财富排行" AND type = "XCUIElementTypeButton"'
    # 音乐福布斯
    music_forbes_rank_title = MobileBy.IOS_PREDICATE, 'name="音乐福布斯排行" AND type = "XCUIElementTypeButton"'




