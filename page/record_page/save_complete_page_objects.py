from appium.webdriver.common.mobileby import MobileBy


class IOS:
    # 再唱一次
    re_record_btn = MobileBy.IOS_PREDICATE, 'label = "再唱一次" AND type = "XCUIElementTypeButton"'
    # 私密发布
    private_publish_btn = MobileBy.IOS_PREDICATE, 'label = "私密上传" AND type = "XCUIElementTypeButton"'
    # 去本地录音查看
    go_local_record_page_check_btn = MobileBy.IOS_PREDICATE, 'label = "保存成功，本地查看" AND type = "XCUIElementTypeButton"'
    # 推荐歌曲
    recommend_song_title = MobileBy.IOS_PREDICATE, 'label = "推荐歌曲" AND type = "XCUIElementTypeStaticText"'
    # 推荐歌曲cells
    recommend_song = MobileBy.IOS_PREDICATE, 'name = "songCell" AND type = "XCUIElementTypeCell"'


    # 关闭
    close_btn = MobileBy.IOS_PREDICATE, 'label = "关闭" AND type = "XCUIElementTypeButton"'
    # 搜索
    search_btn = MobileBy.IOS_PREDICATE, 'label = "搜索" AND type = "XCUIElementTypeButton"'
    # 保存完成页title
    save_complete_page_title = MobileBy.IOS_PREDICATE, 'label = "保存" AND type = "XCUIElementTypeStaticText"'


class Android:
    # 再唱一次
    re_record_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_re_sing")'
    # 私密发布
    private_publish_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_upload")'
    # 去本地录音查看
    go_local_record_page_check_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/publish_txt")'
    # 推荐歌曲
    recommend_song_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("推荐歌曲")'
    # 推荐歌曲cells
    recommend_song = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content_layout")'
    # 关闭
    close_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'
    # 搜索
    search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 保存完成页title
    save_complete_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("保存")'



