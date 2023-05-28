from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 搜索结果页面的标题
    search_result_title = MobileBy.IOS_PREDICATE, 'name = "搜索房间" AND type = "XCUIElementTypeNavigationBar"'
    # 搜索结果
    search_result_record = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 1
    # 搜索结果的lable
    search_result_lable = MobileBy.IOS_PREDICATE, 'label = "广州同城,排麦0,观众804"'
