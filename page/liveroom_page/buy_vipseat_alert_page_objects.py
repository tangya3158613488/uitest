from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 弹框标题
    buy_title=MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/dialog_content_text")'
    # '确定按钮'
    buy_confirm_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")'
    # '取消按钮'
    buy_cancel_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    # 抢占成功toast
    # buy_success_toast=MobileBy.XPATH,"//*[contains(@text, “抢占成功”)]"
    buy_success_toast=MobileBy.XPATH,"//*[@class='android.widget.Toast']"



class IOS:
    pass