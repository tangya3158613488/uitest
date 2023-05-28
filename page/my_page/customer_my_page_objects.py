"""
我的tab-客态
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 右上角--更多
    more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/more_view")'
    # 更多--分享个人主页
    share_home_page_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分享主页")'
    # 更多--设置备注名
    more_set_note = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设置备注名")'
    # 更多--赠送会员
    more_give_vip_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("赠送会员")'
    # 更多--举报此人
    more_report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("举报此人")'
    # 更多--加入黑名单
    more_add_black_list_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("加入黑名单")'
    # 更多--取消
    more_cancle_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    # 歌单
    song_list_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌单")'
    # 取消关注btn
    cancel_follow_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/fellowImg")'
    # 关注btn
    follow_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/fellowBtn")'
    # 聊天btn
    chat_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/chatBtn")'
    # 编辑资料btn
    edit_data_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layoutEdit")'

class IOS:
    # 足迹
    footprint_tab_btn = MobileBy.IOS_PREDICATE, "label = '足迹' AND type = 'XCUIElementTypeButton'"
    #back 返回按钮
    back_btn = MobileBy.IOS_PREDICATE, "label = '返回'"
    # 歌单
    song_list_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '歌单' AND type = 'XCUIElementTypeOther'"
    #右上角--更多
    more_btn = MobileBy.IOS_PREDICATE, "label = '更多' AND type = 'XCUIElementTypeButton'"
    #更多--分享个人主页
    share_home_page_btn = MobileBy.IOS_PREDICATE, "label = '分享主页' AND type = 'XCUIElementTypeButton'"