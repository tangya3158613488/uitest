from appium.webdriver.common.mobileby import MobileBy


class Android:
    # '歌房群聊'按钮元素
    group_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/group_title")'

class IOS:
    pass