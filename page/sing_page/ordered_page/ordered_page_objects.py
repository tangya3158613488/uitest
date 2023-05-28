from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 已点歌曲title元素
    ordered_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("已点歌曲")'
    # 已点tab元素
    ordered_tab_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("已点")'
    # 收藏tab元素
    collect_tab_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("收藏")'
    # 暂无收藏歌曲 txt
    no_collect_songs_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("暂无收藏歌曲")'
    # 待唱tab元素
    wait_sing_tab_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("待唱")'
    # 暂无待唱歌曲 txt
    no_wait_sing_songs_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("暂无待唱歌曲")'
    # 演唱按钮
    sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("演唱")'
    # 导入伴奏 btn
    import_acc_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("导入伴奏")'
    # 导入本地伴奏 btn
    import_local_acc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("导入本地伴奏")'
    # 伴奏cell热区
    acc_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content_layout")'
    # 伴奏cell 歌名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_name")'


class IOS:
    # 已点歌曲title元素
    ordered_page_title = MobileBy.IOS_PREDICATE, 'label = "已点歌曲" AND type = "XCUIElementTypeStaticText"'
    # 已点tab元素
    ordered_tab_txt = MobileBy.IOS_PREDICATE, 'label = "已点" AND type = "XCUIElementTypeStaticText"'
    # 收藏tab元素
    collect_tab_txt = MobileBy.IOS_PREDICATE, 'label = "收藏" AND type = "XCUIElementTypeStaticText"'
    # 暂无收藏歌曲 txt
    no_collect_songs_txt = MobileBy.IOS_PREDICATE, 'label = "暂无收藏歌曲" AND type = "XCUIElementTypeStaticText"'
    # 待唱tab元素
    wait_sing_tab_txt = MobileBy.IOS_PREDICATE, 'label = "待唱" AND type = "XCUIElementTypeStaticText"'
    # 暂无待唱歌曲 txt
    no_wait_sing_songs_txt = MobileBy.IOS_PREDICATE, 'label = "暂无待唱歌曲" AND type = "XCUIElementTypeStaticText"'
    # 演唱按钮
    sing_btn = MobileBy.IOS_PREDICATE, 'label = "演唱" AND type = "XCUIElementTypeButton"'
    # 导入伴奏 btn
    import_acc_btn = MobileBy.IOS_PREDICATE, "name ='导入伴奏' AND visible = true "
    # 导入本地伴奏 btn
    import_local_acc = MobileBy.IOS_PREDICATE, "name = '导入本地伴奏' AND type ='XCUIElementTypeButton'"
    # 伴奏cell 歌名
    song_name = MobileBy.IOS_PREDICATE, "name = '简单爱'"
