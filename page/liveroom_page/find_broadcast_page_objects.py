from appium.webdriver.common.mobileby import MobileBy


class Android:
    # '寻人广播'title元素
    find_broadcast_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("寻人广播")'


class IOS:
    pass