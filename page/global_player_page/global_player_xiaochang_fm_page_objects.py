"""
全局播放器-小唱FM
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 播放全部按钮
    play_all_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("播放全部")'

    # 换一批按钮
    replace_all_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("换一批")'

    # 作品列表
    work_cell_list = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/work_1st_line")'


class IOS:
    # 播放全部按钮
    play_all_btn = MobileBy.IOS_PREDICATE,  "name ='播放全部' AND type ='XCUIElementTypeButton'"

    # 换一批按钮
    replace_all_btn = MobileBy.IOS_PREDICATE, "name = '换一批'"

    # 作品列表
    work_cell_list = MobileBy.IOS_PREDICATE, "type = 'XCUIElementTypeCell' AND visible = true"


