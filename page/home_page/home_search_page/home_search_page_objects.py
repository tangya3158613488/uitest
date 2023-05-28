from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 搜索框
    search_frame = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_input_box")'
    # 搜索按钮
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_search_submit")'
    # 全站热搜tab
    hot_search_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全站热搜")'
    # 哼唱搜索按钮
    hum_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_view")'
    # 哼唱搜索弹窗点击开始哼唱按钮
    start_hum_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_start_humming")'
    # 历史搜索内容（之前搜的歌曲)
    history_search_list = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tag_item_tv")'
    # 删除历史搜索按钮
    del_history_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/operation_icon")'
    # 全站热搜tab-热搜词
    hot_search_word = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/hot_word")'

    # 精彩活动tab
    hot_activity_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("精彩活动")'

    # 精彩活动tab-活动cell
    hot_activity_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content")'

    # 精彩活动tab-查看更多
    hot_activity_more = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rv_with_footer_loading_end")'
    # 话题tab
    hot_topic_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("话题")'
    # 话题tab-话题cell
    hot_topic_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content")'
    # 话题tab-查看更多
    hot_topic_more = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rv_with_footer_loading_end")'

    # 搜索页下方的推荐title
    recommend_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("推荐")'


class IOS:
    # 搜索框
    search_frame = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeSearchField"'
    # 搜索按钮
    search_btn = MobileBy.IOS_PREDICATE, 'label = "搜索" AND visible=true'
    # 哼唱搜索按钮
    hum_song_btn = MobileBy.IOS_PREDICATE, 'label = "哼唱搜索" AND type= "XCUIElementTypeButton" AND visible=true'

    # 哼唱搜索弹窗点击开始哼唱按钮
    start_hum_song_btn = MobileBy.IOS_PREDICATE, 'label = "点击开始哼唱" AND type= "XCUIElementTypeButton" AND visible=true'

    # 历史搜索内容（之前搜的歌曲)
    history_search_list = MobileBy.IOS_PREDICATE, 'name = "history" AND type= "XCUIElementTypeButton" AND visible=true'

    # 删除历史搜索按钮
    del_history_btn = MobileBy.IOS_PREDICATE, 'label = "删除搜索历史" AND type= "XCUIElementTypeButton" AND visible=true'
    # 全站热搜tab
    hot_search_tab = MobileBy.IOS_PREDICATE, 'label = "全站热搜" AND type = "XCUIElementTypeStaticText"'
    # 全站热搜tab-热搜词
    hot_search_word = MobileBy.IOS_PREDICATE, 'name = "hotSearch"'
    # 精彩活动tab
    hot_activity_tab = MobileBy.IOS_PREDICATE, 'label = "精彩活动" AND type = "XCUIElementTypeStaticText"'
    # 精彩活动tab-活动cell
    hot_activity_cell = MobileBy.IOS_PREDICATE, 'name = "activity" AND visible = true'
    # 精彩活动tab-查看更多
    hot_activity_more = MobileBy.IOS_PREDICATE, 'label = "查看更多" AND visible = true'
    # 话题tab
    hot_topic_tab = MobileBy.IOS_PREDICATE, 'label = "话题" AND type = "XCUIElementTypeStaticText"'
    # 话题tab-话题cell
    hot_topic_cell = MobileBy.IOS_PREDICATE, 'name = "activity" AND visible = true'
    # 话题tab-查看更多
    hot_topic_more = MobileBy.IOS_PREDICATE, 'name = "activity" AND label = "查看更多" AND visible = true'

    # 搜索页下方的推荐title
    recommend_title = MobileBy.IOS_PREDICATE, 'label = "推荐" AND type = "XCUIElementTypeStaticText"'
