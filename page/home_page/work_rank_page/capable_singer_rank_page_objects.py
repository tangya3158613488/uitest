from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 实力作品榜title
    capable_singer_rank_title = MobileBy.IOS_PREDICATE, 'name = "北京实力歌手榜" AND type = "XCUIElementTypeNavigationBar"'

    # 获取实力作品榜 "规则"
    rule_btn = MobileBy.IOS_PREDICATE, 'label = "规则" AND type = "XCUIElementTypeButton"'

    # 全局播放器
    player_btn = MobileBy.IOS_PREDICATE, 'label = "全局播放器" AND type = "XCUIElementTypeButton"'

    # 规则说明框
    rule_title = MobileBy.ACCESSIBILITY_ID, "规则"

    # 上榜奖励
    rank_reward = MobileBy.IOS_PREDICATE, 'name ="上榜奖励" AND type ="XCUIElementTypeStaticText"'

    # 上榜规则
    rank_rule = MobileBy.IOS_PREDICATE, 'name ="上榜奖励" AND type ="XCUIElementTypeStaticText"'

    # 我知道了
    i_know_btn = MobileBy.IOS_PREDICATE, 'label ="知道了" AND type ="XCUIElementTypeButton"'

    # 排名icon 1
    rank_icon_first = MobileBy.ACCESSIBILITY_ID, "hottest_work_NO.1"
    # 排名icon 2
    rank_icon_sec = MobileBy.ACCESSIBILITY_ID, "hottest_work_NO.2"
    # 排名icon 3
    rank_icon_three = MobileBy.ACCESSIBILITY_ID, "hottest_work_NO.3"
    # 歌手昵称
    nick_name = MobileBy.IOS_PREDICATE, 'name ="nickName" AND type ="XCUIElementTypeStaticText"', 3
    # 播放按钮
    player_icon = MobileBy.IOS_PREDICATE, 'name ="liveroom_search_singing" AND type ="XCUIElementTypeImage"', 3
    # 音符icon
    note_icon = MobileBy.IOS_PREDICATE, 'name ="feed_work_audio_listen_count" AND type ="XCUIElementTypeImage"', 3
    # 关注按钮
    attention_icon = MobileBy.IOS_PREDICATE, 'name = "followBtn" AND type ="XCUIElementTypeButton"',3
    # 取消关注actionsheet
    attention_sheet = MobileBy.ACCESSIBILITY_ID, "确定不再关注Ta"
    # 确定btn
    sure_btn = MobileBy.IOS_PREDICATE, 'label ="确定" AND name ="确定" AND type ="XCUIElementTypeButton"'
    # 取消btn
    cancel_btn = MobileBy.IOS_PREDICATE, 'label ="取消" AND name ="取消" AND type ="XCUIElementTypeButton"'






