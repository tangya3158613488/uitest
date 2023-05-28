from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 电台直播tab元素
    audio_live_tab_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("电台直播")'
    # 选择背景文案
    select_background_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("选择背景")'
    # 上传背景文案
    upload_background_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("上传背景")'


class IOS:
    # 电台直播tab元素
    audio_live_tab_title = MobileBy.IOS_PREDICATE, 'label = "电台直播" AND visible = "true"'
    # 选择背景文案 ios 没选择背景文案
    select_background_txt = MobileBy.IOS_PREDICATE, 'label = "上传背景"'
    # 上传背景文案
    upload_background_txt = MobileBy.IOS_PREDICATE, 'label = "上传背景" AND visible = "true"'
