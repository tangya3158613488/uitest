from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 排行icon
    ranking_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("排行")'
    # 任务icon
    task_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("任务")'
    # 劲爆抢唱title
    grab_sing_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("劲爆抢唱")'
    # 停止匹配btn
    stop_match_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId(' \
                                                   '"com.changba:id/ktv_match_dialog_title_cancel_tv") '

class IOS:
    # 排行icon
    ranking_icon = MobileBy.IOS_PREDICATE, 'value = "排行" AND type = "XCUIElementTypeStaticText"'
    # 任务icon
    task_icon = MobileBy.IOS_PREDICATE, 'value = "任务" AND type = "XCUIElementTypeStaticText"'
    # 返回icon
    back_image = MobileBy.IOS_PREDICATE, 'type="XCUIElementTypeImage"', 1
    # 新手引导
    new_user_guide = MobileBy.IOS_PREDICATE, 'value="选择一个曲库进行游戏吧" '
