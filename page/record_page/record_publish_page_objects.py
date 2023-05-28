from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    # 发布按钮
    publish_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/publish_button")'
    # 描述编辑区
    publish_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/publish_text")'
    # 公开按钮
    public_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/public_layout")'
    # 上传进度条
    upload_process_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                        '"com.changba:id/upload_progressbar") '
    # 封面图片
    cover_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/upload_cover_image")'
    # 更换封面按钮
    change_cover_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().reourceId("com.changba:id/change_cover_button")'
    # tip
    tip = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("一张好封面可以帮助你收获更多听众哦！")'
    # 添加话题btn
    add_tread_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/add_tread_btn")'
    # 谁可以看btn
    who_can_see_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/who_can_see_icon")'
    # 选择比赛view
    choose_competition_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/competitionView")'
    # 所在位置btn
    select_area_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_select_area")'
    # 允许他人合唱
    able_join_chorus_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layout_able_chorus")'
    # 保存并退出btn
    save_and_exit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("保存并退出")'



class IOS:
    # 发布按钮
    publish_btn = MobileBy.IOS_PREDICATE, 'label = "发布" AND type = "XCUIElementTypeButton"'
    # 描述编辑区：我刚唱了一首歌，快来听听吧。
    publish_text = MobileBy.IOS_PREDICATE, 'name BEGINSWITH "我刚唱了一首歌" AND type = "XCUIElementTypeTextView"'
    # 添加话题按钮
    add_topic_btn = MobileBy.IOS_PREDICATE, 'label = "添加话题" AND type = "XCUIElementTypeButton"'
    # 谁可以看cell
    who_can_see_text = MobileBy.IOS_PREDICATE, 'label = "谁可以看" AND type = "XCUIElementTypeStaticText"'
    # 公开按钮
    public_btn = MobileBy.IOS_PREDICATE, 'label = "公开" AND type = "XCUIElementTypeButton"'
    # 选择比赛
    select_competition_btn = MobileBy.IOS_PREDICATE, 'label = "选择比赛" AND type = "XCUIElementTypeButton"'
    # 上传进度条
    upload_process_view = MobileBy.IOS_PREDICATE, 'label BEGINSWITH "正在上传..." AND type = "XCUIElementTypeStaticText"'
