from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 国语分类页面title元素
    mandarin_classify_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("国语")'
    # 页面title txt
    page_title_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/collapsedTitleTV")'


class IOS:
    mandarin_classify_page_title = MobileBy.IOS_PREDICATE, 'label = "国语"'
    # 页面title txt
    page_title_txt = MobileBy.IOS_PREDICATE, 'name = "title"'

