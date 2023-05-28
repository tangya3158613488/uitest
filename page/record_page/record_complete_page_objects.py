from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 背景播放区
    background_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                    '"com.changba:id/fl_preview_show_scale_frame")'
    # 生成作品按钮
    # generate_work = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
    #                                              "'com.changba:id/tl_operation_tab_generate') "
    generate_work = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生成作品")'
    # 保存按钮
    save_work = MobileBy.ANDROID_UIAUTOMATOR,  'new UiSelector().text("保存")'
    # 重唱按钮
    re_record = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tl_operation_tab_retry")'
    # 歌名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_title")'
    # hq标签
    is_hq = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_hq")'
    # 打分标签
    score_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_score")'
    # 单句得分页面
    score_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("单句得分")'
    # 单句得分页面_返回
    score_page_close = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'
    # 晒成绩
    show_off_score_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_score_share_score")'
    # 晒成绩页面
    show_off_score_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                              '"com.changba:id/score_title_icon") '
    # 晒成绩页面_返回
    show_off_score_page_back = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/close_btn")'
    # 更多按钮
    more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 换背景按钮
    change_background_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                          '"com.changba:id/tv_preview_show_background") '
    # GIF动图
    choose_gif_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("GIF动图")'
    # 本地相册
    local_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本地相册")'
    # 头像相册
    headphoto_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("头像相册")'
    # 清空
    clear_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清空")'
    # 取消
    cancel_choose_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    # 歌词特效
    lyrics_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_preview_show_lyrics")'
    # 歌词特效面板
    lyrics_board_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_lyrics_title")'
    # 歌词特效-无
    lyrics_board_none_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("无")'
    # 关闭歌词特效按钮
    lyrics_board_close_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                           '"com.changba:id/tv_lyrics_confirm") '
    # 合成进度条
    generate_process_view = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                          '"com.changba:id/upload_progressbar") '
    # 关闭按钮
    close_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'
    # 放弃保存
    forgive_save_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("放弃保存")'
    # 弹窗_确认
    dialog_confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'
    # 放弃弹窗_取消
    dialog_cancel = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cancel_btn")'
    # 播放按钮
    play_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/iv_preview_player_state")'
    # 时间轴左侧时间
    left_time = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(com.changba:id/tv_preview_player_start_time")'
    # 时间轴右侧时间
    right_time = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_preview_player_end_time")'

    # 完成页底部tab——————————————————————————————————————————————————————————————————————————————————————————————————
    # 修音tab
    fix_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("修音")'
    # 混响tab
    effect_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("混响")'
    # 音色tab
    timbre_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("音色")'
    # 降噪tab
    denoise_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("降噪")'
    # 音量tab
    volume_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("音量")'
    # 修音tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 一键修音按钮
    auto_repair_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('一键修音')"
    # 智能混音按钮
    mix_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('智能混音')"
    # 智能混音\自动对齐的选中图标
    clicked_mix_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                     "'com.changba:id/iv_fine_repair_select_fore_icon') "
    # 智能混音半屏-声波图
    mix_curve_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba:id/sv_mixing_curve')"
    # 智能混音半屏-人声比例
    mix_volume_level_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                          "'com.changba:id/tv_mixing_level_text') "
    # 智能混音半屏-混音效果
    mix_effect_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                    "'com.changba:id/tv_mixing_mixing_text') "

    # 人工修音按钮
    manual_repair_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('人工修音')"
    # 自动对齐按钮
    auto_align_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('自动对齐')"
    # 手动对齐按钮
    manual_align_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('手动对齐')"
    # 一键修音按钮选中图标
    clicked_repair_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                        "'com.changba:id/iv_operation_standard_state_mark') "
    # 一键修音半屏
    repair_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba:id/vp_operation_tab_pager')"
    # 修音半屏_确认
    repair_confirm_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba.id/tv_repair_confirm')"
    # 修音半屏_取消修音
    repair_cancel_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba:id/tv_mixing_cancel')"
    # 修音半屏_精细修音
    repair_fine_mix_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.changba:id/tv_mixing_fine')"
    # 修音半屏_对比原声
    repair_compare_original_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                                "'com.changba:id/tv_mixing_comparing_original') "
    # 混响tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    pop = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('流行')"

    # 音色tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    fast_adjust_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('快速调节')"

    # 降噪tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 轻度降噪btn
    lite_denoise_btn = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('轻度降噪')"

    # 音量tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 人声
    volume_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                "'com.changba:id/tv_operation_volume_audio') "
    # 伴奏
    accompany_view = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(" \
                                                   "'com.changba:id/tv_operation_volume_accompany') "

    # 更多按钮——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 片段截取
    clips_cut = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("片段截取")'
    # 功能帮助
    help_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("功能帮助")'
    # 问题反馈
    report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("问题反馈")'
    # 取消按钮
    cancel_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'

    # 全屏按钮
    full_screen_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                    '"com.changba:id/tv_preview_show_full_screen") '
    # 全屏页面——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 播放状态
    play_btn_in_full_screen_page = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                                 '"com.changba:id/iv_preview_player_state") '
    # 当前播放进度
    time_in_full_screen_page = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                             '"com.changba:id/tv_preview_player_start_time") '
    # 伴奏总时长
    duration_in_full_screen_page = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                                 '"com.changba:id/tv_preview_player_end_time") '
    # 关闭全屏按钮
    close_full_screen_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                          '"com.changba:id/iv_preview_player_close_half_screen") '

    # 截取片段半屏——————————————————————————————————————————————————————————————————————————————————————————————————————
    # title
    clips_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("截取片段")'
    # 还原整段
    reset_clip_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_record_trim_lrc_reset")'
    # 歌词区
    clip_lrc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rl_record_trim_lrc")'
    # 截取片段半屏-确认
    clip_confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 截取片段半屏-取消
    clip_cancel = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_leftview")'

    # 清唱————————————————————————————————————————————————
    # input_text
    input_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/input_text")'


class IOS:
    # 背景播放区
    background_view = MobileBy.IOS_PREDICATE, 'name = "recordSongName" AND type = "XCUIElementTypeStaticText"'
    # 歌名
    song_name = MobileBy.IOS_PREDICATE, 'name = "recordSongName" AND type = "XCUIElementTypeStaticText"'
    # 打分标签
    score_icon = MobileBy.IOS_PREDICATE, 'name BEGINSWITH "等级" AND type = "XCUIElementTypeButton"'
    # 更多按钮
    more_btn = MobileBy.IOS_PREDICATE, 'name = "更多" AND type = "XCUIElementTypeButton"'
    # 换背景按钮
    change_background_btn = MobileBy.IOS_PREDICATE, 'label = "换背景" AND type = "XCUIElementTypeButton"'
    # 歌词特效
    lyrics_btn = MobileBy.IOS_PREDICATE, 'label = "歌词特效" AND type = "XCUIElementTypeButton"'
    # 全屏按钮
    full_screen_btn = MobileBy.IOS_PREDICATE, 'label = "全屏" AND type = "XCUIElementTypeButton"'
    # 合成进度条
    generate_process_view = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'

    # GIF动图
    choose_gif_img = MobileBy.IOS_PREDICATE, 'label = "GIF动图" AND type = "XCUIElementTypeButton"'
    # 本地相册
    local_img = MobileBy.IOS_PREDICATE, 'label = "本地相册" AND type = "XCUIElementTypeButton"'
    # 头像相册
    headphoto_img = MobileBy.IOS_PREDICATE, 'label = "头像相册" AND type = "XCUIElementTypeButton"'
    # 取消
    cancel_choose_img = MobileBy.IOS_PREDICATE, 'label = "取消" AND type = "XCUIElementTypeButton"'
    # 歌词特效面板
    lyrics_board_text = MobileBy.IOS_PREDICATE, 'label = "歌词效果" AND type = "XCUIElementTypeStaticText"'
    # 歌词特效面板_无
    lyrics_board_none_btn = MobileBy.IOS_PREDICATE, 'label = "无" AND type = "XCUIElementTypeCell"'
    # 歌词特效面板_关闭
    lyrics_board_close_btn = MobileBy.IOS_PREDICATE, 'label = "关闭" AND type = "XCUIElementTypeButton"'

    # 单句得分页面
    score_page_title = MobileBy.IOS_PREDICATE, 'label = "单句得分" AND type = "XCUIElementTypeStaticText"'
    # 单句得分页面_返回
    score_page_close = MobileBy.IOS_PREDICATE, 'label = "返回" AND type = "XCUIElementTypeButton"'
    # 晒成绩
    show_off_score_btn = MobileBy.IOS_PREDICATE, 'label = "晒成绩" AND type = "XCUIElementTypeButton"'
    # 晒成绩页面
    show_off_score_page_title = MobileBy.IOS_PREDICATE, 'label = "晒成绩" AND type = "XCUIElementTypeStaticText"'
    # 晒成绩页面_返回
    show_off_score_page_back = MobileBy.IOS_PREDICATE, 'label = "button back white" AND type = "XCUIElementTypeButton"'

    # 关闭按钮
    close_btn = MobileBy.IOS_PREDICATE, 'label = "关闭" AND type = "XCUIElementTypeButton"'
    # 放弃保存
    forgive_save_btn = MobileBy.IOS_PREDICATE, 'label = "放弃保存" AND type = "XCUIElementTypeStaticText"'
    # 放弃弹窗_确认
    dialog_confirm = MobileBy.IOS_PREDICATE, 'label = "确认"'
    # 放弃弹窗_取消
    dialog_cancel = MobileBy.IOS_PREDICATE, 'label = "取消" AND type = "XCUIElementTypeButton"'
    # 播放按钮
    play_btn = MobileBy.IOS_PREDICATE, 'label = "播放" AND type = "XCUIElementTypeButton"'
    # 播放按钮
    stop_btn = MobileBy.IOS_PREDICATE, 'label = "暂停" AND type = "XCUIElementTypeButton"'

    # 完成页底部tab——————————————————————————————————————————————————————————————————————————————————————————————————
    # 修音tab
    fix_tab = MobileBy.IOS_PREDICATE, 'label = "修音" AND type = "XCUIElementTypeButton"'
    # 修音tab选中
    fix_tab_selected = MobileBy.IOS_PREDICATE, 'label = "修音" AND name = "tabBtn已选中"'
    # 混响tab
    effect_tab = MobileBy.IOS_PREDICATE, 'label = "混响" AND type = "XCUIElementTypeButton"'
    # 混响tab选中
    effect_tab_selected = MobileBy.IOS_PREDICATE, 'label = "混响" AND name = "tabBtn已选中"'
    # 音色tab
    timbre_tab = MobileBy.IOS_PREDICATE, 'label = "音色" AND type = "XCUIElementTypeButton"'
    # 音色tab选中
    timbre_tab_selected = MobileBy.IOS_PREDICATE, 'label = "音色" AND name = "tabBtn已选中"'
    # 降噪tab
    denoise_tab = MobileBy.IOS_PREDICATE, 'label = "降噪" AND type = "XCUIElementTypeButton"'
    # 降噪tab选中
    denoise_tab_selected = MobileBy.IOS_PREDICATE, 'label = "降噪" AND name = "tabBtn已选中"'
    # 音量tab
    volume_tab = MobileBy.IOS_PREDICATE, 'label = "音量" AND type = "XCUIElementTypeButton"'
    # 音量tab选中
    volume_tab_selected = MobileBy.IOS_PREDICATE, 'label = "音量" AND name = "tabBtn已选中"'

    # 修音tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 一键修音按钮
    auto_repair_btn = MobileBy.IOS_PREDICATE, 'label = "一键修音" AND type = "XCUIElementTypeButton"'
    # 智能混音按钮
    mix_btn = MobileBy.IOS_PREDICATE, 'label = "智能混音" AND type = "XCUIElementTypeButton"'
    # 智能混音\自动对齐的选中图标
    clicked_mix_view = MobileBy.IOS_PREDICATE, 'label = "智能混音" AND type = "XCUIElementTypeButton" AND value = 1'
    # 智能混音半屏-声波图
    mix_curve_view = MobileBy.IOS_PREDICATE, 'label = "一键修音" AND type = "XCUIElementTypeButton"'
    # 智能混音半屏-人声比例
    mix_volume_level_view = MobileBy.IOS_PREDICATE, 'label = "人声比例" AND type = "XCUIElementTypeStaticText"'
    # 智能混音半屏-混音效果
    mix_effect_view = MobileBy.IOS_PREDICATE, 'label = "混响效果" AND type = "XCUIElementTypeStaticText"'
    # 智能混音半屏-混音效果
    cancel_mix_curve = MobileBy.IOS_PREDICATE, 'label = "取消混响" AND type = "XCUIElementTypeButton"'

    # 人工修音按钮
    manual_repair_btn = MobileBy.IOS_PREDICATE, 'label = "人工修音" AND type = "XCUIElementTypeButton"'
    # 自动对齐按钮
    auto_align_btn = MobileBy.IOS_PREDICATE, 'label = "自动对齐" AND type = "XCUIElementTypeButton"'
    # 手动对齐按钮
    manual_align_btn = MobileBy.IOS_PREDICATE, 'label = "手动对齐" AND type = "XCUIElementTypeButton"'
    # 一键修音按钮选中图标
    clicked_repair_view = MobileBy.IOS_PREDICATE, 'label = "一键修音" AND type = "XCUIElementTypeButton" AND value = 1'
    # # 一键修音半屏
    # repair_view = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'
    # # 修音半屏_确认
    # repair_confirm_btn = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'
    # # 修音半屏_取消修音
    # repair_cancel_btn = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'
    # # 修音半屏_精细修音
    # repair_fine_mix_btn = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'
    # # 修音半屏_对比原声
    # repair_compare_original_btn = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'

    # 混响tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    pop = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'

    # 音色tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    fast_adjust_btn = MobileBy.IOS_PREDICATE, 'label = 快速调节'' AND type = "XCUIElementTypeCell"'

    # 降噪tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 轻度降噪btn
    lite_denoise_btn = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'

    # 音量tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 人声
    volume_view = MobileBy.IOS_PREDICATE, 'label = "人声" AND type = "XCUIElementTypeStaticText"'
    # 伴奏
    accompany_view = MobileBy.IOS_PREDICATE, 'label = "伴奏" AND type = "XCUIElementTypeStaticText"'

    # toolbar——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 重唱
    re_record = MobileBy.IOS_PREDICATE, 'label = "重唱" AND type = "XCUIElementTypeButton"'
    # 生成作品
    generate_work = MobileBy.IOS_PREDICATE, 'label = "生成作品" AND type = "XCUIElementTypeButton"'
    # 保存
    save_work = MobileBy.IOS_PREDICATE, 'label = "保存" AND type = "XCUIElementTypeButton"'

    # 更多按钮——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 片段补录
    clips_blue = MobileBy.IOS_PREDICATE, 'label = "片段补录" AND type = "XCUIElementTypeButton"'
    # 片段截取
    clips_cut = MobileBy.IOS_PREDICATE, 'label = "片段截取" AND type = "XCUIElementTypeButton"'
    # 功能帮助
    help_btn = MobileBy.IOS_PREDICATE, 'label = "功能帮助" AND type = "XCUIElementTypeButton"'
    # 问题反馈
    report_btn = MobileBy.IOS_PREDICATE, 'label = "问题反馈" AND type = "XCUIElementTypeButton"'
    # 取消按钮
    cancel_btn = MobileBy.IOS_PREDICATE, 'label = "取消" AND type = "XCUIElementTypeButton"'

    # 全屏页面——————————————————————————————————————————————————————————————————————————————————————————————————————
    # 播放状态
    stop_btn_in_full_screen_page = MobileBy.IOS_PREDICATE, 'name = "暂停" AND type = "XCUIElementTypeButton"'
    # 暂停状态
    play_btn_in_full_screen_page = MobileBy.IOS_PREDICATE, 'name = "播放" AND type = "XCUIElementTypeButton"'
    # 进度条上的播放进度:当前是0分1秒，总时长0分16秒
    progress_in_full_screen_page = MobileBy.IOS_PREDICATE, 'label BEGINSWITH "当前是" AND type = "XCUIElementTypeSlider"'
    # 当前播放进度
    time_in_full_screen_page = MobileBy.IOS_PREDICATE, 'name = "time" AND type = "XCUIElementTypeStaticText"'
    # 伴奏总时长
    duration_in_full_screen_page = MobileBy.IOS_PREDICATE, 'name = "duration" AND type = "XCUIElementTypeStaticText"'
