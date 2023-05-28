from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 导入页面title元素
    import_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("选择本地文件")'
    # 视频具体cell
    video_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cover")', 7
    # 音频具体cell
    audio_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/fileNameTV")'


class IOS:
    # 导入页面title元素
    import_page_title = MobileBy.IOS_PREDICATE, 'label = "选择本地视频" AND type = "XCUIElementTypeStaticText"'
