from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 绑定手机号title元素
    bind_tel_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("绑定手机号")'
    # 下一步按钮元素
    next_step_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("下一步")'
    # 输入手机号输入框元素
    input_tel_frame = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("请填写手机号码")'


class IOS:
    # 绑定手机号title元素
    bind_tel_title = MobileBy.IOS_PREDICATE, 'name = "绑定手机号"'
    # 下一步按钮元素
    next_step_btn = MobileBy.IOS_PREDICATE, 'label = "下一步" AND visible ="true"'
    # 输入手机号输入框元素
    input_tel_frame = MobileBy.IOS_PREDICATE, 'label = "请填写手机号码" AND visible = "true"'
