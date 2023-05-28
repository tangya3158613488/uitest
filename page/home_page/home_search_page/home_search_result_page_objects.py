from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 搜索结果页-综合tab
    comprehensive_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("综合")'
    # 搜索结果页-伴奏tab
    accompaniment_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("伴奏")'
    # 搜索结果页-群组tab
    group_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("群组")'
    # 搜索结果页-用户tab
    user_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("用户")'
    # 搜索结果页-作品tab
    work_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品")'
    # 搜索结果页-合唱tab
    duet_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("合唱")'
    # 演唱按钮
    sing_btn =  MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn")'

    # 伴奏cell
    accompaniment_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content_layout")'

    # 伴奏cell 添加到已点按钮
    accompaniment_cell_add_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_add")'
    # 伴奏tab-更多版本按钮
    more_accompaniment_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/expand_button")'
    # 用户tab-昵称
    user_nick_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/first_line")'
    # 加入群组
    group_join_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_join")'

    # 合唱tab-合唱按钮
    duet_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_item")'


    # 合唱tab-仅显示视频合唱开关
    duet_switch = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/chorus_only")'

    # 合唱tab-昵称
    duet_nick_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/username")'

    # 合唱tab-歌曲名
    duet_song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/songname")'

    # 删除搜索框内容按钮
    clear_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_search_submit")'

    # 搜索框左侧返回按钮
    back_btn = MobileBy.IOS_PREDICATE, 'label="返回" AND type = "XCUIElementTypeButton" AND visible = true'

    # 作品tab作品封面
    search_work_card = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清唱1分钟")'


class IOS:
    # 搜索结果页-综合tab
    comprehensive_search_tab = MobileBy.IOS_PREDICATE, 'label = "综合" AND type = "XCUIElementTypeStaticText"'
    # 搜索结果页-伴奏tab
    accompaniment_search_tab = MobileBy.IOS_PREDICATE, 'label = "伴奏" AND type = "XCUIElementTypeStaticText"'
    # 搜索结果页-群组tab
    group_search_tab = MobileBy.IOS_PREDICATE, 'label = "群组" AND type = "XCUIElementTypeStaticText"'
    # 搜索结果页-用户tab
    user_search_tab = MobileBy.IOS_PREDICATE, 'label = "用户" AND type = "XCUIElementTypeStaticText"'
    # 搜索结果页-作品tab
    work_search_tab = MobileBy.IOS_PREDICATE, 'label = "作品" AND type = "XCUIElementTypeStaticText"'
    # 搜索结果页-合唱tab
    duet_search_tab = MobileBy.IOS_PREDICATE, 'label = "合唱" AND type = "XCUIElementTypeStaticText"'
    # 演唱按钮
    sing_btn = MobileBy.IOS_PREDICATE, 'label = "演唱" AND type = "XCUIElementTypeButton" AND visible = true'

    # 伴奏cell
    accompaniment_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell" AND visible = true'

    # 伴奏cell 添加到已点按钮
    accompaniment_cell_add_song_btn = MobileBy.IOS_PREDICATE, 'label="sing home add to sing" AND type="XCUIElementTypeButton" AND visible=true'

    # 伴奏tab-更多版本按钮
    more_accompaniment_btn = MobileBy.IOS_PREDICATE, 'label="更多版本" AND type="XCUIElementTypeButton" AND visible = true'

    # 用户tab-昵称
    user_nick_name = MobileBy.IOS_PREDICATE, 'name="nickName" AND type = "XCUIElementTypeStaticText" AND visible = true'

    # 加入群组
    group_join_btn = MobileBy.IOS_PREDICATE, 'label="加入" AND type = "XCUIElementTypeButton" AND visible = true'

    # 合唱tab-合唱按钮
    duet_btn = MobileBy.IOS_PREDICATE, 'label="合唱" AND type = "XCUIElementTypeButton" AND visible = true'

    # 合唱tab-仅显示视频合唱开关
    duet_switch = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeSwitch" AND visible = true'

    # 合唱tab-昵称
    duet_nick_name = MobileBy.IOS_PREDICATE, 'name="nickName" AND type = "XCUIElementTypeStaticText" AND visible = true'

    # 合唱tab-歌曲名
    duet_song_name = MobileBy.IOS_PREDICATE, 'name="songName" AND type = "XCUIElementTypeStaticText" AND visible = true'

    # 删除搜索框内容按钮
    clear_text = MobileBy.IOS_PREDICATE, 'label="清除文本" AND type = "XCUIElementTypeButton" AND visible = true'

    # 搜索框左侧返回按钮
    back_btn = MobileBy.IOS_PREDICATE, 'label="返回" AND type = "XCUIElementTypeButton" AND visible = true'
