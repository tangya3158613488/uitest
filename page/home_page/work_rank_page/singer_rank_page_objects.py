from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 作品榜
    works_list_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品榜")'
    # 歌手榜
    singer_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌手榜")'
    # 财富榜
    wealth_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("财富榜")'


class IOS:
    # 子榜作品cell
    singer_rank_work_cell = MobileBy.IOS_PREDICATE,'type ="XCUIElementTypeCell"',1
    # 子榜歌手昵称
    work_singer_name = MobileBy.IOS_PREDICATE, 'name ="workSingerName" AND type = "XCUIElementTypeStaticText" AND value CONTAINS "1"'
    # 完整榜单
    wealth_tab = MobileBy.IOS_PREDICATE, 'label ="完整榜单" AND type ="XCUIElementTypeStaticText"'
    # 实力歌手榜
    capable_singer_rank_title = MobileBy.IOS_PREDICATE, 'name ="userChartTitle" AND label = "北京实力歌手榜"'

    # 实力歌手榜 title
    capable_singer_rank_btn = MobileBy.IOS_PREDICATE, 'name="北京实力歌手榜" AND type = "XCUIElementTypeButton"'

    # 最火歌手榜
    hottest_singer_rank_title = MobileBy.IOS_PREDICATE, 'name ="userChartTitle" AND label = "北京最火歌手榜"'

    # 最火歌手榜 title
    hottest_singer_rank_btn = MobileBy.IOS_PREDICATE, 'name="北京最火歌手榜" AND type = "XCUIElementTypeButton"'

    # 全国实力歌手榜
    nation_capable_singer_rank_title = MobileBy.IOS_PREDICATE, 'name= "全国实力歌手榜" AND type = "XCUIElementTypeButton"'

    # 全国最火歌手榜
    nation_hottest_singer_rank_title = MobileBy.IOS_PREDICATE, 'name= "全国最火歌手榜" AND type = "XCUIElementTypeButton"'

    # 新人榜
    newer_singer_rank_title = MobileBy.IOS_PREDICATE, 'name= "新人榜" AND type = "XCUIElementTypeButton"'


