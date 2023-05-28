from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 页面顶部title元素
    navigation_bar_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'
    room_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/live_room_anchor_name")'
    close = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/el_empty_close_iv")'
    # 弹窗_确认
    dialog_confirm = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'


class IOS:
    # 页面左上角返回键
    back_btn = MobileBy.IOS_PREDICATE, "label IN {'button back white','button back red','button close white','返回','close button image','取消', '返回“唱吧”', 'button down', '关闭', '点歌台','消息','选择聊天对象','确认','本地伴奏','已点歌曲','歌手'} AND type = 'XCUIElementTypeButton' AND visible = true"
    # 页面顶部title元素
    navigation_bar_title = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeNavigationBar"'
