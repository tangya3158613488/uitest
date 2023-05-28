from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    # 歌手名
    singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_sub_titleview")'
    # 退出btn
    exit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageViewClose")'
    # 开始录制btn
    recording_state_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                        '"com.changba:id/recording_state_control_btn") '
    # 主题btn
    change_skin_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                    '"com.changba:id/record_change_skin_change_iv")'
    # 唱片段btn
    clip_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_part_sing")'
    # 唱全部btn
    all_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_all_sing")'
    # 独唱btn
    single_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("独唱")'
    # 发起合唱btn
    duet_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发起合唱")'
    # 音视频模式btn
    mode_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/audio_selector")'
    # 佩戴耳机提示
    earphone_tip = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layout_headset")'
    # hq按钮
    hq_tag = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_hq_accompany")'
    # 关闭tip按钮
    close_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_close")'
    # 我先唱按钮
    my_order_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我先唱")'
    # 我后唱歌按钮
    others_order_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我后唱")'
    # 智能识别按钮
    agent_distinguish_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("智能识别")'
    # 左侧头像
    left_photo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/left_photo")'
    # 右侧头像
    right_photo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_photo")'


class IOS:
    # 伴奏名
    song_name = MobileBy.IOS_PREDICATE, 'index = 1 AND type = "XCUIElementTypeStaticText"'
    # 歌手名
    singer_name = MobileBy.IOS_PREDICATE, 'index = 2 AND type = "XCUIElementTypeStaticText"'
    # 关闭按钮
    exit_btn = MobileBy.IOS_PREDICATE, 'label = "关闭"'
    # 练唱按钮
    practice_sing_btn = MobileBy.IOS_PREDICATE, 'label = "练唱"'
    # 录制按钮
    recording_state_btn = MobileBy.IOS_PREDICATE, 'label = "演唱" AND type="XCUIElementTypeButton"'
    # 主题按钮
    change_skin_btn = MobileBy.IOS_PREDICATE, 'label = "主题"'
    # 唱片段按钮
    clip_sing_btn = MobileBy.IOS_PREDICATE, 'label = "唱片段" AND type = "XCUIElementTypeButton"'
    # 唱整首按钮
    all_sing_btn = MobileBy.IOS_PREDICATE, 'label = "唱整首" AND type = "XCUIElementTypeButton"'
    # 发起合唱按钮
    duet_sing_btn = MobileBy.IOS_PREDICATE, 'label = "发起合唱" AND type="XCUIElementTypeButton"'
    # 我先唱按钮
    my_order_btn = MobileBy.IOS_PREDICATE, 'label = "我先唱" AND type="XCUIElementTypeButton"'
    # 我后唱歌按钮
    others_order_btn = MobileBy.IOS_PREDICATE, 'label = "我后唱" AND type="XCUIElementTypeButton"'
    # 智能识别按钮
    agent_distinguish_btn = MobileBy.IOS_PREDICATE, 'label = "智能识别" AND type="XCUIElementTypeButton"'
    # 独唱按钮
    single_sing_btn = MobileBy.IOS_PREDICATE, 'label = "独唱"'
    # 切换到音频按钮
    change_to_audio_mode_btn = MobileBy.IOS_PREDICATE, 'label = "切换到音频"'
    # 切换到视频按钮
    change_to_video_mode_btn = MobileBy.IOS_PREDICATE, 'label = "切换到视频"'
    # 戴耳机tips
    earphone_tip = MobileBy.IOS_PREDICATE, 'label = "佩戴耳机演唱音效会更好哦"'

