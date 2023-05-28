from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 最火作品榜title
    hottest_rank_title = MobileBy.IOS_PREDICATE, 'name = "北京最火作品榜" AND type = "XCUIElementTypeNavigationBar"'

    # 全局播放器
    player_btn = MobileBy.IOS_PREDICATE, 'label = "全局播放器" AND type = "XCUIElementTypeButton"'

    # 作品第一cell
    work_card = MobileBy.IOS_PREDICATE, "name = 'workcell' AND type = 'XCUIElementTypeOther'", 1

    # 作品前三名icon
    rank_icon_first = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.1' AND type = 'XCUIElementTypeOther'"

    # 作品前三名icon
    rank_icon_sec = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.2' AND type = 'XCUIElementTypeOther'"

    # 作品前三名icon
    rank_icon_thr = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.3' AND type = 'XCUIElementTypeOther'"

    # 获取最火作品榜 "规则"
    rule_btn = MobileBy.IOS_PREDICATE, 'label = "规则" AND type = "XCUIElementTypeButton"'

    # 规则说明框
    rule_title = MobileBy.ACCESSIBILITY_ID, "规则"

    # 上榜奖励
    rank_reward = MobileBy.IOS_PREDICATE, 'name ="上榜奖励" AND type ="XCUIElementTypeStaticText"'

    # 上榜规则
    rank_rule = MobileBy.IOS_PREDICATE, 'name ="上榜奖励" AND type ="XCUIElementTypeStaticText"'

    # 我知道了
    i_know_btn = MobileBy.IOS_PREDICATE, 'label ="知道了" AND type ="XCUIElementTypeButton"'

    # 月榜
    month_btn = MobileBy.IOS_PREDICATE, 'label="月榜" AND type ="XCUIElementTypeButton"'

    # total榜
    total_btn = MobileBy.IOS_PREDICATE, 'label="总榜" AND type ="XCUIElementTypeButton"'

    # 当前tab榜
    current_btn = MobileBy.IOS_PREDICATE, 'name ="tabBtn已选中" AND type ="XCUIElementTypeButton"'

