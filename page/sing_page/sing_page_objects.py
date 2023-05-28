from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 任务中心入口元素
    task_center = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("任务入口")'
    # 搜索框元素
    search_frame_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_switcher")'
    # 识别歌曲元素
    recog_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_view")'
    # 识别歌曲弹窗-开始哼唱btn
    start_hum_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("点击开始哼唱")'
    # 识别歌曲弹窗-放弃识别btn
    give_up_recog_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("点击放弃识别")'
    # 识别歌曲弹窗-点击重新识别btn
    re_recog_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("点击重新识别")'
    # 识别歌曲弹窗-关闭btn
    close_recog_pop_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_close")'
    # 小火车cell
    small_train_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/live_user_fl")',1
    # 开歌房icon
    open_live_room_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("开歌房")'
    # 直播唱icon
    live_sing_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("直播唱")'
    # 实时合唱icon
    real_time_chrous_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("实时合唱")'
    # 劲爆抢唱icon
    grab_sing_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("劲爆抢唱")'
    # 清唱icon
    only_sing_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清唱")'
    # 漂流瓶icon
    drifting_bottle_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("漂流瓶")'
    # 以声相遇icon
    meet_by_sounds_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("以声相遇")'
    # 心愿墙icon
    wish_wall_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("心愿墙")'
    # 导入icon
    import_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("导入")'
    # 已点btn元素
    ordered_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("已点")'
    # 歌手btn元素
    singer_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌手")'
    # 分类btn元素
    classify_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("分类")'
    # 商城btn元素
    mall_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商城")'
    # 点歌区-猜你喜欢tab
    guess_you_like_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("猜你喜欢")'
    # 点歌区-我的伴奏tab
    my_acc_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的伴奏")'
    # 点歌区-飙升榜tab
    soaring_list_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("飙升榜")'
    # 点歌区-年代榜tab
    years_list_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("年代榜")'
    # 点歌区-抖音热歌tab
    dou_yin_hot_songs_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("抖音热歌")'
    # 点歌区-热歌榜tab
    hot_songs_list_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热歌榜")'
    # 点歌区-一键修音tab
    one_click_edit_sounds_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("一键修音")'
    # 点歌区-新歌榜tab
    new_songs_list_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新歌榜")'
    # 点歌区-歌曲cell
    songs_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content_layout")'
    # 点歌区-歌曲cell-歌曲名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_name")'
    # 点歌区-歌曲cell-歌手名
    singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_content")'
    # 点歌区-歌曲cell-演唱btn
    sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_sing")'
    # 点歌区-歌曲封面
    songs_cover = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_cover")'
    # 点歌区-歌曲播放暂停按钮
    songs_play_or_pause = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/play_or_pause")'

class IOS:
    # 任务中心入口元素
    task_center = MobileBy.IOS_PREDICATE, 'label = "任务中心" AND type = "XCUIElementTypeButton"'
    # 搜索框元素
    search_frame_loc = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeSearchField"'
    # 识别歌曲元素
    recog_song_btn = MobileBy.IOS_PREDICATE, 'label = "哼唱搜索" AND type = "XCUIElementTypeButton"'
    # 识别歌曲弹窗-开始哼唱btn
    start_hum_sing_btn = MobileBy.IOS_PREDICATE, 'label = "点击开始哼唱" AND type = "XCUIElementTypeButton"'
    # 识别歌曲弹窗-放弃识别btn
    give_up_recog_btn = MobileBy.IOS_PREDICATE, 'label = "点击放弃识别" AND type = "XCUIElementTypeButton"'
    # 识别歌曲弹窗-点击重新识别btn
    re_recog_song_btn = MobileBy.IOS_PREDICATE, 'label = "点击重新识别" AND type = "XCUIElementTypeButton"'

    close_recog_pop_btn = MobileBy.IOS_PREDICATE, 'label = "关闭" AND type = "XCUIElementTypeButton"'
    # 小火车cell todo 找不到
    small_train_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell" AND visible = true', 0
    # 开歌房icon
    open_live_room_icon = MobileBy.IOS_PREDICATE, 'label = "开歌房" AND type = "XCUIElementTypeCell"'
    # 直播唱icon
    live_sing_icon = MobileBy.IOS_PREDICATE, 'label = "直播唱" AND type = "XCUIElementTypeCell"'
    # 实时合唱icon
    real_time_chrous_icon = MobileBy.IOS_PREDICATE, 'label = "实时合唱" AND type = "XCUIElementTypeCell"'
    # 劲爆抢唱icon
    grab_sing_icon = MobileBy.IOS_PREDICATE, 'label = "劲爆抢唱" AND type = "XCUIElementTypeCell"'
    # 清唱icon
    only_sing_icon = MobileBy.IOS_PREDICATE, 'label = "清唱" AND type = "XCUIElementTypeCell"'
    # 漂流瓶icon
    drifting_bottle_icon = MobileBy.IOS_PREDICATE, 'label = "漂流瓶" AND type = "XCUIElementTypeCell"'
    # 以声相遇icon
    meet_by_sounds_icon = MobileBy.IOS_PREDICATE, 'label = "以声相遇" AND type = "XCUIElementTypeCell"'
    # 心愿墙icon
    wish_wall_icon = MobileBy.IOS_PREDICATE,'label = "心愿墙" AND type = "XCUIElementTypeCell"'
    # 导入icon
    import_icon = MobileBy.IOS_PREDICATE, 'label = "导入" AND type = "XCUIElementTypeCell"'
    # 导入icon
    import_local_video = MobileBy.IOS_PREDICATE, 'label = "导入本地视频"'
    # 已点btn元素
    ordered_btn = MobileBy.IOS_PREDICATE, 'label = "已点" AND type = "XCUIElementTypeButton"'
    # 歌手btn元素
    singer_btn = MobileBy.IOS_PREDICATE, 'label = "歌手" AND type = "XCUIElementTypeButton"'
    # 分类btn元素
    classify_btn = MobileBy.IOS_PREDICATE, 'label = "分类" AND type = "XCUIElementTypeButton"'
    # 商城btn元素
    mall_btn = MobileBy.IOS_PREDICATE, 'label = "商城" AND type = "XCUIElementTypeButton"'

    # 点歌区-歌曲cell-演唱btn
    sing_btn = MobileBy.IOS_PREDICATE, 'label = "演唱" AND type = "XCUIElementTypeButton"'
    # 点歌区-歌曲cell-歌手名
    singer_name = MobileBy.IOS_PREDICATE, 'name = "singer" AND type = "XCUIElementTypeStaticText"'
    # 点歌区-歌曲cell-伴奏名
    song_name = MobileBy.IOS_PREDICATE, 'name = "songName" AND type = "XCUIElementTypeStaticText"'

    # 点歌区-歌曲cell
    songs_cell = MobileBy.IOS_PREDICATE,  'type = "XCUIElementTypeCell"'
