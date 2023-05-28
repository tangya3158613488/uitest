from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 旋转视频
    rotate_video = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rotate_btn")'
    # 下一步按钮
    next_step_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/next_btn")'