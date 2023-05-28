from appium.webdriver.common.mobileby import MobileBy


class Android:
#  下麦确定按钮
    confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")'

    #  下麦取消按钮
    cancel = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")'
    # title
    title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("是否确认下麦？")'




class IOS:
    pass