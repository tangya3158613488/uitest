from appium.webdriver.common.mobileby import MobileBy


class Android:
    # '静音'按钮元素
    mute = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("静音")'
    # '下麦'按钮元素
    wheat_down = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("下麦")'
    # 取消按钮
    wheat_down_cancel = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    # 你已被静音
    toast_mute=MobileBy.XPATH,"//*[@class='android.widget.Toast']"

# '关闭特效'元素
# close_special_effects = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关闭特效")'


class IOS:
    pass