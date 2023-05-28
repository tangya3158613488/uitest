from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 全部分类页面title元素
    all_classfiy_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部分类")'
    # 国语分类按钮
    mandarin_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("国语")'

class IOS:
    # 全部分类页面title元素
    all_classfiy_page_title = MobileBy.IOS_PREDICATE, 'name="全部分类"'
    # 国语分类按钮
    mandarin_btn = MobileBy.IOS_PREDICATE, 'type="XCUIElementTypeButton" AND name="categoryContent" AND label="国语"'
