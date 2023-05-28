from appium.webdriver.common.mobileby import MobileBy


class Android:
    page_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    # 话题广场
    topic_square = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    # 我的
    me = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")'
    # 热门
    popular_topics = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热门")'
    # 作品数
    works = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/topic_square_detail_item_work_count")'
    # 动态数目
    dynamic = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/topic_square_detail_item_play_count")'
    # 具体的话题cell
    topic_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/topic_square_item_container")'



class IOS:
    page_id = MobileBy.IOS_PREDICATE, "name = '话题广场' AND type = 'XCUIElementTypeNavigationBar' AND visible = true"
    # 话题广场
    topic_square = MobileBy.IOS_PREDICATE, "label = '话题广场' AND name = '话题广场' AND type = 'XCUIElementTypeStaticText' AND visible = true"
    # 我的
    me = MobileBy.IOS_PREDICATE, "label = '我的' AND name = '我的' AND type = 'XCUIElementTypeStaticText' AND visible = true"
    # 热门
    popular_topics = MobileBy.IOS_PREDICATE, "label = '热门' AND name = '热门' AND type = 'XCUIElementTypeStaticText' AND visible = true"
    # 作品数
    works = MobileBy.IOS_PREDICATE, "label BEGINSWITH '作品' AND type = 'XCUIElementTypeStaticText' AND visible = true"
    # 动态数目
    dynamic = MobileBy.IOS_PREDICATE, "label BEGINSWITH '动态' AND type = 'XCUIElementTypeStaticText' AND visible = true"
    # 具体的话题cell
    topic_cell = MobileBy.IOS_PREDICATE, " type = 'XCUIElementTypeCell' AND visible = true"
