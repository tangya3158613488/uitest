from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 热门歌手页面title元素
    hot_singer_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热门歌手")'
    # 单个歌手
    single_singer_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/hot_singer_name")'


class IOS:
    # 热门歌手页面title元素
    hot_singer_page_title = MobileBy.IOS_PREDICATE, 'name="热门歌手"'
    # 单个歌手
    single_singer_cell = MobileBy.IOS_PREDICATE, 'label="周杰伦"'
