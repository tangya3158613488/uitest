from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 搜索输入框
    search_edit = MobileBy.IOS_PREDICATE, 'label = "房间号、房间名、关键词"'
    # 搜索类别-同城
    search_local_room = MobileBy.IOS_PREDICATE, 'label = "同城"'
    # 搜索类别-情感
    search_emotion_room = MobileBy.IOS_PREDICATE, 'label = "情感"'
    # 搜索历史记录
    search_history_record = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText"', 1
    # 删除单条历史记录
    delete_search_history_record = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeButton"', 1
    # ** / XCUIElementTypeStaticText[`label == "26688888"`]
    # 取消搜索
    search_cancel = MobileBy.IOS_PREDICATE, 'label = "取消"'
