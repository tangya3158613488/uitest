"""
全局播放器-正在收听
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 正在收听tab
    listening_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("正在收听")'

    # 无数据时，进入小唱FM btn
    xiaochang_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("小唱FM")'

    # 清空按钮
    clear_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清空")'


class IOS:
    # 无数据时，进入小唱FM btn
    xiaochang_btn = MobileBy.IOS_PREDICATE, 'name == "进入小唱FM"'

    # 清空按钮
    clear_btn = MobileBy.IOS_PREDICATE, "name = '清空'"
