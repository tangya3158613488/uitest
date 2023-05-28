from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 实力作品榜title
    capable_rank_title = MobileBy.IOS_PREDICATE, 'name = "北京实力作品榜" AND type = "XCUIElementTypeNavigationBar"'

    # 获取实力作品榜 "规则"
    rule_btn = MobileBy.IOS_PREDICATE, 'label = "规则" AND type = "XCUIElementTypeButton"'

    # 全局播放器
    player_btn = MobileBy.IOS_PREDICATE, 'label = "全局播放器" AND type = "XCUIElementTypeButton"'

    # 作品第一cell
    work_card = MobileBy.IOS_PREDICATE, "name = 'workcell' AND type = 'XCUIElementTypeOther'", 1

    # 作品前三名icon
    rank_icon_first = MobileBy.ACCESSIBILITY_ID, "hottest_work_NO.1"

    # 作品前三名icon
    rank_icon_sec = MobileBy.ACCESSIBILITY_ID, "hottest_work_NO.2"

    # 作品前三名icon
    rank_icon_thr = MobileBy.ACCESSIBILITY_ID, "hottest_work_NO.3"

    # 规则说明框
    rule_title = MobileBy.ACCESSIBILITY_ID, "规则"

    # 上榜奖励
    rank_reward = MobileBy.IOS_PREDICATE, 'name ="上榜规则" AND type ="XCUIElementTypeStaticText"'
    # 上榜规则
    rank_rule = MobileBy.IOS_PREDICATE, 'name ="上榜奖励" AND type ="XCUIElementTypeStaticText"'

    # 我知道了
    i_know_btn = MobileBy.IOS_PREDICATE, 'label ="知道了" AND type ="XCUIElementTypeButton"'
