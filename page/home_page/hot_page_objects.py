from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 投稿
    submit_work_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("投稿音视频，让更多的人发现你")'
    # 热门tab下的小火车
    train_card = user_nick_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/state_tv")'
    # 作品card
    # work_card = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/contentTv")', 0
    work_card = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/fl_works_card")'

    # 首页搜索
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchCl")'
class IOS:
    # 投稿
    submit_work_btn = MobileBy.IOS_PREDICATE, "label = '投稿' AND type = 'XCUIElementTypeButton'"
    # 热门tab下的小火车
    train_card = MobileBy.IOS_PREDICATE, 'name="小火车" AND label="小火车" '
