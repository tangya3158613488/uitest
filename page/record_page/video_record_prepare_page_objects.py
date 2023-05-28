from appium.webdriver.common.mobileby import MobileBy
from page.record_page import audio_record_prepare_page_objects


class IOS(audio_record_prepare_page_objects.IOS):
    # 切换到音频模式按钮
    change_video_btn = MobileBy.IOS_PREDICATE, 'label = "切换到音频"'
    # 翻转按钮
    flip_camera_btn = MobileBy.IOS_PREDICATE, 'label = "翻转到后置摄像头"'
    # 美化按钮
    beauty_btn = MobileBy.IOS_PREDICATE, 'label = "美颜"'
    # 道具按钮
    prop_btn = MobileBy.IOS_PREDICATE, 'label = "道具"'
    # 佩戴耳机tips
    tips = MobileBy.IOS_PREDICATE, 'label = "佩戴耳机演唱音效会更好哦"'
    # 歌名
    sing_name = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 0'
    # 歌手名
    singer_name = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeStaticText" AND index = 1'


class Android(audio_record_prepare_page_objects.Android):
    # 歌名
    song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_titleview")'
    # 歌手名
    singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_sub_titleview")'
    # 音视频模式btn
    change_video_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/audio_selector")'
    # 佩戴耳机tips
    tips = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/layout_headset")'
    # 美化按钮
    beauty_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_beauty_mode")'
    # 道具按钮
    prop_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn_effect")'
    # 翻转按钮
    flip_camera_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/icon_reverse")'
    # 关闭tip按钮
    close_img = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_close")'
