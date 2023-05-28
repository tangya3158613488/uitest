from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 本地伴奏页面title
    local_acc_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("本地伴奏")'
    # 具体伴奏
    acc_el = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/local_record_item_view")'
    # 演唱按钮
    sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("演唱")'
    # 歌曲名称
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'


class IOS:
    # 本地伴奏页面title
    local_acc_title = MobileBy.IOS_PREDICATE, 'name = "本地伴奏"'
    # 具体伴奏
    acc_el = MobileBy.IOS_PREDICATE, "name = '蝶恋'"
    # 演唱按钮
    sing_btn = MobileBy.IOS_PREDICATE, 'name = "演唱"'
    # 歌曲名称  todo 定位不到
    song_name = MobileBy.IOS_PREDICATE,  "name = '蝶恋'"
