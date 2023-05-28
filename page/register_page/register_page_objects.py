from appium.webdriver.common.mobileby import MobileBy

class Android:

    # 用户协议与隐私保护-同意tab
    agree_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("同意")'

    # 用户协议与隐私保护-不同意tab
    disagree_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("不同意")'

    # 请输入手机号
    userid_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入手机号")'

    # 获取验证码
    get_verification_code_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("获取验证码")'

    # 验证码框
    # verification_code_tab = MobileBy.XPATH,'//*[@resource-id="com.changba:id/edit_layout"]/android.widget.RelativeLayout[1]'
    verification_code_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("请输入短信验证码")'

    # 登录tab
    login_btn = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")'

    # 同意协议tab
    consent_protocol_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/check")'

    # 密码登录tab
    password_login_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("密码登录")'

    # 唱吧ID
    changba_id_input = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/email")'

    # 密码
    # password_text_input = MobileBy.XPATH,'//*[@resource-id="com.changba:id/edit_layout"]/android.widget.RelativeLayout[1]'
    # password_text_input = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.changba:id/password")'
    password_text_input = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入密码")'


    # 忘记密码或账号
    forget_password_tab = MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains(忘记密码)'

    grant_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("授权")'

    i_see_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")'

    man_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男生")'
    woman_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女生")'
    open_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("开启我的唱吧之旅")'
