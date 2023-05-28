"""
全局播放器页
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    xiaochang_fm_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("小唱FM")'


class IOS:
    # 全局播放页小唱
    xiaochang_fm_tab = MobileBy.IOS_PREDICATE, 'label = "小唱FM"'

    # 正在收听tab
    listening_tab = MobileBy.IOS_PREDICATE, 'label = "正在收听"'

    # 我的tab
    my_tab = MobileBy.IOS_PREDICATE, 'label = "我的"'

    # 正在选择的tab
    selected_tab = MobileBy.IOS_PREDICATE, 'name = "tabBtn已选中"'

    # 全局播放器底部进度条
    player_slider = MobileBy.IOS_PREDICATE, "name = 'playerSlider'"

    # 全局播放器底部播放模式按钮
    play_model = MobileBy.IOS_PREDICATE, "name BEGINSWITH '播放模式'"

    # 上一首
    prev_btn = MobileBy.IOS_PREDICATE, "name = '上一首'"

    # 下一首
    next_btn = MobileBy.IOS_PREDICATE, "name = '下一首'"

    # 播放暂停按钮
    play_btn = MobileBy.IOS_PREDICATE, "name IN {'播放','暂停'}"

    # 收藏按钮
    collect_btn = MobileBy.IOS_PREDICATE, "name CONTAINS '收藏'"

    songCntTxt = MobileBy.IOS_PREDICATE, "name ENDSWITH '首' AND NOT name CONTAINS '一'"

    workCellList = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeCell' AND visible = true"

    workCell = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeCell' AND visible = true"

    moreBtn = MobileBy.IOS_PREDICATE, "name = 'globalplay more btn' AND visible = true"

    forwardBtn = MobileBy.IOS_PREDICATE, "name = '转发'"

    clearBtn = MobileBy.IOS_PREDICATE, "name = '移除'"

    unlikeBtn = MobileBy.IOS_PREDICATE, "name = '不喜欢'"

    moreTitle = MobileBy.IOS_PREDICATE, "name = 'baseTitle'"
