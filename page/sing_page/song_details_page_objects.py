from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌曲名称元素
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_name")'
    # 歌手名称元素
    singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_artist")'
    # '我要演唱'按钮元素
    sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/sing_btn")'
    # 今日最佳tab
    today_best_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("今日最佳")'
    # 年度最佳tab
    years_best_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("年度最佳")'
    # 历史最佳tab
    history_best_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("历史最佳")'
    # 加入合唱tab
    add_duet_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("加入合唱")'
    # 用户昵称
    user_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_name")'
    # 歌曲分类icon
    song_category_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_category_first")'
    # 上滑页面后 演唱按钮变为 演唱
    swipe_after_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("演唱")'
    # 今日最佳tab-好友最佳独唱
    friend_best_sing = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("好友最佳独唱")'
    # 今日最佳tab-用户头像
    today_best_tab_headphoto = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/headphoto")'
    # 今日最佳tab-用户昵称
    today_best_tab_user_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_name")'
    # 年度最佳tab-用户头像
    years_best_tab_headphoto = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/headphoto")'
    # 年度最佳tab-用户昵称
    years_best_tab_user_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_name")'
    # 加入合唱tab-作品描述
    add_duet_tab_work_content = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/work_content")'
    # 加入合唱tab-合唱按钮
    add_duet_tab_chorus_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_pk_or_chorus")'


class IOS:
    # 歌曲名称元素
    song_name = MobileBy.IOS_PREDICATE, 'name = "songName"'
    # 歌手名称元素
    singer_name = MobileBy.IOS_PREDICATE, 'name = "singerName"'
    # '我要演唱'按钮元素
    sing_btn = MobileBy.IOS_PREDICATE, 'label = "我要演唱"'
    # 今日最佳tab
    today_best_tab = MobileBy.IOS_PREDICATE, 'label = "今日最佳"'
    # 历史最佳tab
    history_best_tab = MobileBy.IOS_PREDICATE, 'label = "历史最佳"'
    # 加入合唱tab
    add_duet_tab = MobileBy.IOS_PREDICATE, 'label = "加入合唱"'
    # 举报按钮
    report_btn = MobileBy.IOS_PREDICATE, 'name="举报" AND label="举报" AND type="XCUIElementTypeButton"'
    # 教唱
    learn_btn = MobileBy.IOS_PREDICATE, 'name="教唱" AND label="教唱" AND type="XCUIElementTypeButton"'
    # 折叠按钮
    fold_btn = MobileBy.IOS_PREDICATE, 'name="折叠" AND label="折叠"'
    # 历史最佳tab下方用户昵称
    nick_name = MobileBy.IOS_PREDICATE, 'name="nickName" AND type="XCUIElementTypeStaticText" '
    # 历史最佳tab下方用户cell
    user_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"'
    # 历史最佳tab下方用户头像
    user_head_photo = MobileBy.IOS_PREDICATE, 'name = "headPhoto"'
    # 加入tab下方合唱
    duet_btn = MobileBy.IOS_PREDICATE, 'name="合唱" AND label="合唱" AND visible = true '
    # 今日最佳去演唱
    goto_sing_btn = MobileBy.IOS_PREDICATE, 'name="去演唱" AND label="去演唱" AND type="XCUIElementTypeButton"'
    # 今日最佳tab下 今日最佳独唱
    today_best_solo = MobileBy.IOS_PREDICATE, 'name="今日最佳独唱" AND type="XCUIElementTypeStaticText"'
    # 年度最佳tab
    years_best_tab = MobileBy.IOS_PREDICATE, 'label = "年度最佳"'
    # 年度最佳tab-用户头像
    years_best_tab_headphoto = MobileBy.IOS_PREDICATE, "label ='headphoto'"
    # 年度最佳tab-用户昵称
    years_best_tab_user_name = MobileBy.IOS_PREDICATE, "label ='username'"
    # 选择的tab
    tab_selected = MobileBy.IOS_PREDICATE, "name ='tabBtn已选中'"
