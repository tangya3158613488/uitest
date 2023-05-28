#!/usr/bin/python
# coding=utf-8
# author:lzy

from appium.webdriver.common.mobileby import MobileBy


class Android:
    title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本地录音")'
    back_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'

class IOS:
    # 页面title
    title = MobileBy.IOS_PREDICATE, "name = '本地录音' AND type = 'XCUIElementTypeNavigationBar'"
    # 返回
    back_btn = MobileBy.IOS_PREDICATE, "name = '返回' AND type = 'XCUIElementTypeButton'"
    # 删除按钮
    delete_btn = MobileBy.IOS_PREDICATE, "label = '批量操作' AND type = 'XCUIElementTypeButton'"

    # 伴奏名字
    song_name = MobileBy.IOS_PREDICATE, "name = 'songName' AND type = 'XCUIElementTypeStaticText'"
    # 音频录音二次编辑icon
    edit_icon = MobileBy.IOS_PREDICATE, "name = '可编辑' AND type = 'XCUIElementTypeStaticText'"
    # MV icon
    MV_icon = MobileBy.IOS_PREDICATE, "name = 'mvIcon' AND type = 'XCUIElementTypeImage'"
    # 总分
    score = MobileBy.IOS_PREDICATE, "name BEGINSWITH '总分' AND type = 'XCUIElementTypeStaticText'"
    # 录制时间：label:12-09 10:45
    record_time = MobileBy.IOS_PREDICATE, "index = 3 AND type = 'XCUIElementTypeStaticText'"
    # 录制时长：label:04:46
    record_total_time = MobileBy.IOS_PREDICATE, "name = 'duration' AND type = 'XCUIElementTypeStaticText'"
    # 上传
    upload_btn = MobileBy.IOS_PREDICATE, "name = '上传' AND type = 'XCUIElementTypeButton'"

    # 删除本地录音页面——————————————————————————————————————————————————————
    # 删除本地录音页面title
    delete_record_title = MobileBy.IOS_PREDICATE, "label = '删除本地录音' AND type = 'XCUIElementTypeStaticText'"
    # 全选
    check_all_btn = MobileBy.IOS_PREDICATE, "label = '全选' AND type = 'XCUIElementTypeButton'"
    # 完成
    complete_btn = MobileBy.IOS_PREDICATE, "label = '完成' AND type = 'XCUIElementTypeButton'"

    # 上传
    upload_glay_btn = MobileBy.IOS_PREDICATE, "name = '上传' AND type = 'XCUIElementTypeButton' AND enable = 'false'"
    # 未选中
    location_unselect_btn = MobileBy.IOS_PREDICATE, "name = 'location_unselect' AND type = 'XCUIElementTypeImage'"
    # 选中
    location_select_btn = MobileBy.IOS_PREDICATE, "name = 'location_select' AND type = 'XCUIElementTypeImage'"

