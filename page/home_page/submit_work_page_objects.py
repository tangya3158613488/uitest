from appium.webdriver.common.mobileby import MobileBy


class Android:
    pass


class IOS:
    # 投稿
    help_btn = MobileBy.IOS_PREDICATE, "label = '我要上推荐攻略' AND type = 'XCUIElementTypeButton'"
