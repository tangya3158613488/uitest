from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 联想词语
    search_result_record = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"', 1
    # label == "1120陈连转的房间,排麦1,观众1,正在演唱琼剧伴奏 一场大祸起萧墙"
