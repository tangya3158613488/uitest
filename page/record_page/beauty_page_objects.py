from appium.webdriver.common.mobileby import MobileBy


class IOS:
    # 美颜tab元素
    beauty_tab = MobileBy.IOS_PREDICATE, 'label = "美颜"'
    # 风格妆tab元素
    dressing_tab = MobileBy.IOS_PREDICATE, 'label = "风格妆"'
    # 滤镜tab元素
    filter_tab = MobileBy.IOS_PREDICATE, 'label = "滤镜"'
    # 美妆tab元素
    beauty_makeup_tab = MobileBy.IOS_PREDICATE, 'label = "美妆"'


class Android:
    # 美颜tab元素
    beauty_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("美颜")'
    # 风格妆tab元素
    dressing_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("风格妆")'
    # 滤镜tab元素
    filter_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("滤镜")'
    # 美妆tab元素
    beauty_makeup_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("美妆")'




