from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass

class IOS:
    # 评论tab
    player_comment_tab = MobileBy.IOS_PREDICATE, 'label CONTAINS "评论" AND type = "XCUIElementTypeButton"'

    # 更多
    more_icon = MobileBy.IOS_PREDICATE, 'name = "moreAction" AND type = "XCUIElementTypeButton" AND label = "更多操作"'
    # 播放模式
    play_mode = MobileBy.IOS_PREDICATE, "name = 'playMode' AND type = 'XCUIElementTypeButton'"
    # 上一首
    last_icon = MobileBy.IOS_PREDICATE, 'name = "上一首" AND type = "XCUIElementTypeButton" AND label = "上一首"'
    # 下一首
    next_icon = MobileBy.IOS_PREDICATE, 'name = "下一首" AND type = "XCUIElementTypeButton" AND label = "下一首"'
    # 暂停/播放
    play_icon = MobileBy.IOS_PREDICATE, 'name = "playBtn" AND type = "XCUIElementTypeButton" AND label = "播放"'
    # 收藏
    collect_icon = MobileBy.IOS_PREDICATE, 'name = "likeBtn" AND type = "XCUIElementTypeButton" AND label = "收藏"'
    # 详情tab
    player_detail_tab = MobileBy.IOS_PREDICATE, 'name = "详情" AND type = "XCUIElementTypeStaticText"'


    # 用户头像
    user_head = MobileBy.IOS_PREDICATE, "label = '全国金榜' AND type = 'XCUIElementTypeButton'"
    # 作者信息
    author_info = MobileBy.IOS_PREDICATE, 'name CONTAINS "作者" AND type = "XCUIElementTypeButton"'
    # 关注按钮
    attention_button = MobileBy.IOS_PREDICATE, 'name = "关注" AND type ="XCUIElementTypeButton"'
    # 聊天按钮
    chat_button = MobileBy.IOS_PREDICATE, 'name = "聊天" AND type ="XCUIElementTypeButton"'
    # 作品名字
    song_name = MobileBy.IOS_PREDICATE, 'name = "songName" AND type ="XCUIElementTypeOther"'
    # 最近听众
    latest_listeners = MobileBy.IOS_PREDICATE, 'name CONTAINS "最近听众" AND type ="XCUIElementTypeOther"'












