from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 作品榜
    works_list_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品榜")'
    # 歌手榜
    singer_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌手榜")'
    # 财富榜
    wealth_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("财富榜")'
    # 总榜全局播放器
    global_player_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/mini_player")'


class IOS:
    # 作品榜
    works_list_tab = MobileBy.IOS_PREDICATE, 'label ="作品榜" AND type ="XCUIElementTypeButton"'
    # 歌手榜
    singer_tab = MobileBy.IOS_PREDICATE, 'label = "歌手榜" AND type = "XCUIElementTypeButton"'
    # 财富榜
    wealth_tab = MobileBy.IOS_PREDICATE, 'label ="财富榜" AND type ="XCUIElementTypeButton"'
    # 总榜全局播放器
    global_player_btn = MobileBy.IOS_PREDICATE, "label = '全局播放器' AND type = 'XCUIElementTypeButton'"
    # 获取作品榜 "规则"
    rule_btn = MobileBy.IOS_PREDICATE, 'label = "规则" AND type = "XCUIElementTypeButton"'
    # 规则说明框
    rule_title = MobileBy.ACCESSIBILITY_ID, "规则"
    # 上榜奖励
    rank_reward = MobileBy.IOS_PREDICATE, 'name ="上榜规则" AND type ="XCUIElementTypeStaticText"'
    # 上榜规则
    rank_rule = MobileBy.IOS_PREDICATE, 'name ="上榜奖励" AND type ="XCUIElementTypeStaticText"'
    # 我知道了
    i_know_btn = MobileBy.IOS_PREDICATE, 'label ="知道了" AND type ="XCUIElementTypeButton"'
    # 细节榜作品榜cell
    details_rank_work_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 1
    # 细节榜榜歌曲名称
    work_song_name = MobileBy.IOS_PREDICATE, 'name = "nickName"', 1
    # 作品榜用户昵称
    user_nickname = MobileBy.IOS_PREDICATE, 'name = "workSongName"', 1
    # 实力作品榜cell title
    capable_work_rank_title = MobileBy.IOS_PREDICATE, 'name CONTAINS "实力作品榜" AND type = "XCUIElementTypeCell"', 0
    # 实力作品榜btn
    capable_work_rank_btn = MobileBy.XPATH, '//XCUIElementTypeCell[@name="北京实力作品榜"]/XCUIElementTypeButton'
    # 最火实力作品榜cell title
    hottest_work_rank_title = MobileBy.IOS_PREDICATE, 'name CONTAINS "最火作品榜" AND type = "XCUIElementTypeCell"', 0
    # 最火实力作品榜btn
    hottest_work_rank_btn = MobileBy.XPATH, '//XCUIElementTypeCell[@name="北京最火作品榜"]/XCUIElementTypeButton'
    # 全国实力作品榜cell title
    nation_capable_work_rank_title = MobileBy.IOS_PREDICATE, 'name = "全国实力作品榜" AND type = "XCUIElementTypeCell"'

    # 全国最火作品榜cell title
    nation_hottest_work_rank_title = MobileBy.IOS_PREDICATE, 'name= "全国最火作品榜" AND type = "XCUIElementTypeCell"'

    # 新人实力作品榜cell title
    newer_capable_work_rank_title = MobileBy.IOS_PREDICATE, 'name = "新人实力作品" AND type = "XCUIElementTypeCell"'

    # 新人最火作品榜cell title
    newer_hottest_work_rank_title = MobileBy.IOS_PREDICATE, 'name = "新人最火作品" AND type = "XCUIElementTypeCell"'

    # 最火mv榜cell title
    hottest_mv_work_rank_title = MobileBy.IOS_PREDICATE, 'name= "最火MV榜" AND type = "XCUIElementTypeCell"'

    # 人气榜cell title
    popular_work_rank_title = MobileBy.IOS_PREDICATE, 'name = "人气榜" AND type = "XCUIElementTypeCell"'

    # 兴趣榜 cell title
    interest_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "兴趣榜" AND type = "XCUIElementTypeCell"'

    # 鲜肉榜
    young_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "鲜肉榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 民谣榜
    folk_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "民谣榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 摇滚榜
    rock_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "摇滚榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 古风榜
    old_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "古风榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 粤语榜
    cantonese_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "粤语榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 动漫榜
    comic_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "动漫榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # R&B榜
    r_b_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "R&B榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 外语榜
    language_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "外语榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 红歌
    red_song_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "红歌榜" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    minik_work_rank_title = MobileBy.IOS_PREDICATE, 'label = "咪哒唱吧minik" AND type = "XCUIElementTypeStaticText" AND name = "workSongName"'

    # 完整榜单
    compete_rank_icon = MobileBy.IOS_PREDICATE, 'label = "完整榜单" AND type = "XCUIElementTypeStaticText"', 1

