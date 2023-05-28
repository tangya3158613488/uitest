from appium.webdriver.common.mobileby import MobileBy


class Android:
    title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("K歌主题")'


class IOS:
    # 主题页面title
    title = MobileBy.IOS_PREDICATE, 'label = "K歌主题"'