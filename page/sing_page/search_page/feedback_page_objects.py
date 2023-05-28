from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 意见反馈 页面title
    feedback_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("意见反馈")'


class IOS:
    feedback_page_title = MobileBy.IOS_PREDICATE, 'label = "意见反馈"'
