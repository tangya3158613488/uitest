from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 保存按钮
    save_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("保存")'
    # 上传按钮
    upload_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("上传")'
    # 视频生成完成 tips
    video_generation_complete = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("视频生成完成")'
