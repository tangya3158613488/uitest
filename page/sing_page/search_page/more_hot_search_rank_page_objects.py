from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 热搜榜页面title
    hot_rank_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热搜榜")'


class IOS:
    # 热搜榜页面title
    hot_rank_page_title = MobileBy.IOS_PREDICATE, 'label = "热搜榜"'
