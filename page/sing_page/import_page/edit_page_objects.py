from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 旋转视频
    rotate_video = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rotate_btn")'
    # 下一步按钮
    next_step_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/next_btn")'
    # 音量按钮
    # volume_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/volume_btn")'
    volume_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("音量")'
    # 特效按钮
    # effect_edit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/effect_edit_btn")'
    effect_edit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("特效")'
    # 封面按钮
    # cover_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cover_edit_btn")'
    cover_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("封面")'
    # 滤镜按钮
    # filter_edit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/filter_edit_btn")'
    filter_edit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("滤镜")'
    # 音量进度条
    audio_volume_seek_bar = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/audio_volume_seek_bar")'
    # 具体特效
    effect_image = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/effect_image")',8
    # 保存按钮
    save_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/save_effect_btn")'
    # 具体滤镜
    filter_image = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/iv_beauty_standard_state_image")',3
    # 封面进度条
    cover_seek_bar = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/music_seek_bar")'