"""
我的 个人主页-主态
"""
from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 左上角菜单栏按钮
    menu_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/left_view")'
    # 金币/钻石 btn
    coins_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_money")'
    # 任务中心btn
    daily_task_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_view")'
    # 背景图
    back_ground_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imgBg")'
    # 编辑资料btn
    edit_data_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layoutEdit")'
    # 情侣头像标识 关闭状态 点击弹起开启弹窗
    lover_img_btn_close = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imgLoverSetting")'
    # 情侣头像标识 开启状态 点击进入情侣客态个人主页
    lover_img_btn_open = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imgLoverAvatarFl")'
    # 来访按钮
    come_to_visit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("来访")'
    # 性别icon
    gender_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imgGender")'
    # 年龄icon
    age_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/ageTv")'
    # 星座icon
    constellation_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/constellationTv")'
    # 性别年龄星座icon
    GenderAgeArea_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layoutGenderAgeArea")'
    # 现居地icon
    local_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/locateTv")'
    # 个人介绍 主态点击可调起半屏弹窗 客态点击无反应
    singature_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/textSignature")'
    # 会员中心
    vip_center_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("会员中心")'
    # 本地录音tab
    local_record_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("本地录音")'
    # 我的歌单tab
    my_song_list_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("我的歌单")'
    # 我的投稿tab
    submit_work_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("我要投稿")'
    # 作品tab
    work_list = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("作品")'
    # 收藏tab
    collect_tab_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().text("收藏")'
    # 活动tab
    activity_tab_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().text("活动")'
    # 作品tab-录制作品按钮
    record_works_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("快去录一首吧")'
    # 动态tab-发动态按钮
    pulish_dynamic_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("快去录一首吧")'
    # 我的信息
    my_information_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("的信息")'
    # 菜单栏-扫一扫按钮
    menu_scan_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("扫一扫")'
    # 菜单栏-我的直播
    menu_my_live_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的直播")'
    # 菜单栏-我的钱包
    menu_my_wallet_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的钱包")'
    # 菜单栏-我的背包
    menu_my_bag_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的背包")'
    # 菜单栏-播放历史
    menu_play_history_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("播放历史")'
    # 菜单栏-人工修音
    menu_artificial_tuning_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("人工修音")'
    # 菜单栏--K歌商城
    menu_sing_mall_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("K歌商城")'
    # 菜单栏-原创购买
    menu_original_buy_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("原创购买")'
    # 菜单栏-音乐人入驻
    menu_musican_settled_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("音乐人入驻")'
    # 菜单栏-情侣空间
    menu_lover_space_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("情侣空间")'
    # 菜单栏-帮助与反馈
    menu_help_and_feedback_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帮助与反馈")'
    # 菜单栏-小黑屋
    menu_small_black_home_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("小黑屋")'
    # 菜单栏-设置
    menu_setting_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设置")'
    # 点击用户头像-弹窗-头像装扮
    headphoto_dress_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("头像装扮")'
    # 点击用户头像-弹窗-我的相册
    headphoto_my_album_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的相册")'
    # 点击用户头像-弹窗-取消
    headphoto_cancel_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'

class IOS:
    # 编辑资料
    edit_data_btn = MobileBy.IOS_PREDICATE, "label = '编辑资料' AND type = 'XCUIElementTypeButton'"
    # 来访按钮
    come_to_visit_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '来访' AND type = 'XCUIElementTypeStaticText' "
    # 任务中心
    daily_task_btn = MobileBy.IOS_PREDICATE, "label = '任务中心' AND type = 'XCUIElementTypeButton'"
    # 添加好友
    add_friend_btn = MobileBy.IOS_PREDICATE, "label = '添加好友' AND type = 'XCUIElementTypeButton'"
    # 本地录音
    local_record_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '本地录音' AND type = 'XCUIElementTypeButton'"
    # 活动
    activity_tab_btn = MobileBy.IOS_PREDICATE, "label = '活动' AND type = 'XCUIElementTypeButton'"
    # 足迹
    footprint_tab_btn = MobileBy.IOS_PREDICATE, "label = '足迹' AND type = 'XCUIElementTypeButton'"
    # 会员中心
    vip_center_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '会员中心' AND type = 'XCUIElementTypeButton'"
    # 我的歌单
    my_song_list_btn = MobileBy.IOS_PREDICATE, "label BEGINSWITH '我的歌单' AND type = 'XCUIElementTypeButton'"
    # 我的信息
    my_information_btn = MobileBy.IOS_PREDICATE, "label = '编辑信息' AND type = 'XCUIElementTypeButton' "
    #足迹-话题
    topic_btn = MobileBy.IOS_PREDICATE, "label = '话题' AND type = 'XCUIElementTypeButton'"