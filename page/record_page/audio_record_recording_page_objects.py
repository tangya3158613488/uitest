from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 总分等级横条
    score_level_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/sing_level_view")'
    # 打分器
    score_container_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                         '"com.changba:id/fl_scoring_container") '
    # 打开极速模式
    open_fast_mode_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/open_fast_text")'
    # 右上角更多btn
    more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_layout")'
    # 歌名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    # 歌手名（此页不应有）
    singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_sub_titleview")'
    # 退出btn
    exit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageViewClose")'
    # 关闭打分器btn
    score_control_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                      '"com.changba:id/scoreControlIv") '
    # 歌词区btn
    lyric_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/recording_lrc")'
    # hq标签
    hq_tag = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_hq")'
    # 放弃录制btn
    forgive_record_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("放弃录制")'
    # 音视频切换模式
    mode_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/audio_selector")'
    # 首句助唱btn
    first_lyric_help = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                     '"com.changba:id/btn_first_guide_layout") '
    # 音量电平
    volume_prompt_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                       '"com.changba:id/volume_prompt_view") '
    # 放大歌词
    enlarge_lyrics_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("放大歌词")'
    # 还原歌词
    restore_lyrics_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("还原歌词")'
    # 功能帮助
    help_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("功能帮助")'
    # 反馈问题
    report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("反馈问题")'

    # 调音台————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    # 耳机监听view
    earphone_monitor_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                         '"com.changba:id/earphoneMonitorTv") '
    # 耳机监听switch
    earphone_monitor_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                         '"com.changba:id/earphone_switch_btn") '
    # 人声view
    voice_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/earTv")'
    # 人声bar
    voice_bar = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/earphone_seekbar")'
    # 伴奏view
    accompany_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/mic")'
    # 伴奏bar
    accompany_bar = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/accompany_seekbar")'
    # 变调view
    tone_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/updowntxt")'
    # 降调btn
    tone_down_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tone_down")'
    # 升调btn
    tone_up_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tone_up")'
    # 变调bar
    tone_bar = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tone_seekbar")'
    # 底部btn——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 领唱btn
    original_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/original_btn")'
    # 调音台btn
    volume_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/volume_btn")'
    # 录制状态btn
    recording_state_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                        '"com.changba:id/recording_state_control_btn")'
    # 重唱btn
    re_record_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/re_record_btn")'
    # 完成btn
    finish_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/complete_btn_text")'
    # 录制计时
    time_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/timeTv")'
    # 重唱弹窗_文案
    dialog_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/dialog_content_text")'
    # 重唱弹窗_确认
    dialog_confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'
    # 重唱弹窗_取消
    dialog_cancel = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cancel_btn")'
    # 合成进度弹窗
    dialog_content = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/dialog_content")'
    # 跳过前奏
    skip_prelude = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("跳过前奏")'
    # 左侧头像
    left_photo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/left_photo")'
    # 右侧头像
    right_photo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_photo")'


class IOS:
    # 总分等级横条
    score_level_view = MobileBy.IOS_PREDICATE, 'label BEGINSWITH "当前等级" '
    # 打分器
    score_container_view = MobileBy.IOS_PREDICATE, 'name="RecordView_Wavy_Line_BG_RRD" AND type = "XCUIElementTypeImage"'
    # 右上角更多btn
    more_btn = MobileBy.IOS_PREDICATE, 'label="更多"'
    # 音视频切换模式
    mode_btn = MobileBy.IOS_PREDICATE, 'label="切换到视频"'
    # 歌名
    song_name = MobileBy.IOS_PREDICATE, 'index = 1 AND type = "XCUIElementTypeStaticText"'
    # 歌手名（此页不应有）
    singer_name = MobileBy.IOS_PREDICATE,
    # 退出btn
    exit_btn = MobileBy.IOS_PREDICATE, 'name="关闭" AND type = "XCUIElementTypeButton"'
    # 收起打分器btn
    score_control_btn = MobileBy.IOS_PREDICATE, 'name="收起打分器" AND type = "XCUIElementTypeButton"'
    # 展开打分器btn
    score_control_unfold_btn = MobileBy.IOS_PREDICATE, 'name="展开打分器" AND type = "XCUIElementTypeButton"'
    # 歌词区btn
    lyric_view = MobileBy.IOS_PREDICATE, 'name="lyrics" AND type = "XCUIElementTypeStaticText"'
    # 跳过前奏tips
    skip_prelude = MobileBy.IOS_PREDICATE, 'label="跳过前奏"'
    # 首句助唱tips
    first_lyric_help = MobileBy.IOS_PREDICATE, 'label="首句助唱"'
    # 合唱头像
    chorus_head = MobileBy.IOS_PREDICATE, 'name="chorusHead_default" AND type = "XCUIElementTypeImage"'
    # 合唱头像 &
    chorus_head_and = MobileBy.IOS_PREDICATE, 'name="record_and" AND type = "XCUIElementTypeImage"'
    # hq标签
    hq_tag = MobileBy.IOS_PREDICATE, 'name="收起打分器" AND type = "XCUIElementTypeButton"'
    # 关闭_重新录制
    exit_re_record = MobileBy.IOS_PREDICATE, 'name="重新录制" AND type = "XCUIElementTypeButton"'
    # 关闭_放弃录制
    forgive_record_btn = MobileBy.IOS_PREDICATE, 'name="放弃录制" AND type = "XCUIElementTypeButton"'
    # 关闭_取消
    exit_cancel = MobileBy.IOS_PREDICATE, 'name="取消" AND type = "XCUIElementTypeButton"'
    # 首句助唱btn
    first_guid_btn = MobileBy.IOS_PREDICATE, 'name="首句助唱"'
    # 音量电平
    volume_prompt_view = MobileBy.IOS_PREDICATE,

    # 打开副歌特效
    open_chorus_effect_btn = MobileBy.IOS_PREDICATE, 'label="打开副歌特效" AND type = "XCUIElementTypeButton"'
    # 放大歌词
    enlarge_lyrics_btn = MobileBy.IOS_PREDICATE, 'label="放大歌词" AND type = "XCUIElementTypeButton"'
    # 还原歌词
    restore_lyrics_btn = MobileBy.IOS_PREDICATE, 'label="还原歌词" AND type = "XCUIElementTypeButton"'
    # 功能帮助
    help_btn = MobileBy.IOS_PREDICATE, 'label="功能帮助" AND type = "XCUIElementTypeButton" AND index = 0'
    # 反馈问题
    report_btn = MobileBy.IOS_PREDICATE, 'label="反馈问题" AND type = "XCUIElementTypeButton"'
    # 取消
    cancle_btn = MobileBy.IOS_PREDICATE, 'label="取消" AND type = "XCUIElementTypeButton"'

    # 调音台————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    # 耳机监听view
    earphone_monitor_txt = MobileBy.IOS_PREDICATE, 'name="耳机监听"'
    # 耳机监听switch
    earphone_monitor_btn = MobileBy.IOS_PREDICATE, 'name="开启耳返" AND type = "XCUIElementTypeButton"'
    # 人声view
    voice_txt = MobileBy.IOS_PREDICATE, 'name="人声" AND type = "XCUIElementTypeStaticText"'
    # 人声bar
    voice_bar = MobileBy.IOS_PREDICATE, 'name="人声音量" AND type = "XCUIElementTypeSlider"'
    # 伴奏view
    accompany_txt = MobileBy.IOS_PREDICATE, 'name="伴奏" AND type = "XCUIElementTypeStaticText"'
    # 伴奏bar
    accompany_bar = MobileBy.IOS_PREDICATE, 'name="伴奏音量" AND type = "XCUIElementTypeSlider"'
    # 变调view
    tone_txt = MobileBy.IOS_PREDICATE, 'name="变调" AND type = "XCUIElementTypeStaticText"'
    # 降调btn
    tone_down_btn = MobileBy.IOS_PREDICATE, 'name="降调" AND type = "XCUIElementTypeButton"'
    # 升调btn
    tone_up_btn = MobileBy.IOS_PREDICATE, 'name="升调" AND type = "XCUIElementTypeButton"'
    # 变调bar
    tone_bar = MobileBy.IOS_PREDICATE, 'index = 2" AND type = "XCUIElementTypeOther"'
    # 底部btn——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 领唱btn
    original_btn = MobileBy.IOS_PREDICATE, 'name="领唱" AND type = "XCUIElementTypeButton"'
    # 调音台btn
    volume_btn = MobileBy.IOS_PREDICATE, 'name="调音台" AND type = "XCUIElementTypeButton"'
    # 录制状态btn
    recording_state_btn = MobileBy.IOS_PREDICATE, 'name="暂停" AND type = "XCUIElementTypeButton"'
    # 暂停状态btn
    stop_state_btn = MobileBy.IOS_PREDICATE, 'name="继续" AND type = "XCUIElementTypeButton"'
    # 重唱btn
    re_record_btn = MobileBy.IOS_PREDICATE, 'name="重唱" AND type = "XCUIElementTypeButton"'
    # 完成btn
    finish_btn = MobileBy.IOS_PREDICATE, 'name="完成" AND type = "XCUIElementTypeButton"'
    # 录制计时
    time_view = MobileBy.IOS_PREDICATE, 'label ENDSWITH "秒" AND type = "XCUIElementTypeStaticText"'
    # 重唱弹窗_文案
    dialog_text = MobileBy.IOS_PREDICATE, 'name="确定要重新录制吗？" AND type = "XCUIElementTypeStaticText"'
    # 重唱弹窗_确认
    dialog_confirm = MobileBy.IOS_PREDICATE, 'label="确定" AND type = "XCUIElementTypeButton"'
    # 重唱弹窗_取消
    dialog_cancel = MobileBy.IOS_PREDICATE, 'label="取消" AND type = "XCUIElementTypeButton"'
