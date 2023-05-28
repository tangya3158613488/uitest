from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 话题详情页-作品tab
    work_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品")'
    # 话题详情页-动态tab
    moment_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("动态")'
    # 发作品按钮
    public_work = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/publish_btn")'
    # 发作品按钮
    public_moment = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/publish_btn")'
    # 搜索结果页-综合tab
    hot_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("综合")'
    # 话题详情页话题名字
    trend_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/trend_title")'



class IOS:
    # 话题详情页-作品tab
    work_tab = MobileBy.IOS_PREDICATE, 'label = "作品" AND type = "XCUIElementTypeStaticText"'

    # 话题详情页-动态tab
    moment_tab = MobileBy.IOS_PREDICATE, 'label = "动态" AND type = "XCUIElementTypeStaticText"'

    # 发作品按钮
    public_work = MobileBy.IOS_PREDICATE, 'label = "topic square public work" AND type = "XCUIElementTypeButton"'

    # 发动态按钮
    public_moment = MobileBy.IOS_PREDICATE, 'label="topic square public moment" AND type = "XCUIElementTypeButton"'

    # 搜索结果页-综合tab
    hot_btn = MobileBy.IOS_PREDICATE, 'label = "最热" AND type = "XCUIElementTypeStaticText"'
