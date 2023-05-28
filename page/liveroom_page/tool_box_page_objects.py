from appium.webdriver.common.mobileby import MobileBy


class Android:
    # '歌友召唤'按钮元素
    songfriend_call = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("歌友召唤")'
    # '寻人广播'按钮元素
    find_broadcast = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("寻人广播")'
    # '关闭特效'元素
    close_special_effects = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关闭特效")'
    # 群聊
    group_talk= MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("群聊")'
    # 权益中心
    center = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("权益中心")'
    # 打开演唱区按钮
    open_singing_area_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("打开演唱区")'
    # 关闭演唱区
    close_singing_area_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关闭演唱区")'
    #判断演唱区是否展示
    singing_area_displayed_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("戴上耳机演唱效果更好哦~")'
    #弹窗确认按钮
    confirm_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/confirm_btn")'
    #弹窗取消按钮
    cancel_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    #惩罚按钮cell
    punishment_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("惩罚")'
    #惩罚工具cell
    punishment_tool_displayed = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("按下滑杆，选择惩罚项目")'
    #寻人广播按钮可见
    people_search_btn_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("寻人广播")'


class IOS:
    pass