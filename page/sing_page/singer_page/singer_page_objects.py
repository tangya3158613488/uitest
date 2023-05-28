from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌手页面title元素
    singer_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌手")'
    # 热门歌手title元素
    hot_singer_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热门歌手")'
    # 热门歌手-查看全部元素
    hot_singer_see_more = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查看全部")', 0


class IOS:
    # 歌手页面title元素
    singer_page_title = MobileBy.IOS_PREDICATE, 'label = "歌手"'
    # 热门歌手title元素
    hot_singer_title = MobileBy.IOS_PREDICATE, 'label = "热门歌手"'
    # 热门歌手-查看全部元素
    hot_singer_see_more = MobileBy.IOS_PREDICATE, 'label="查看全部" AND visible=true', 0
