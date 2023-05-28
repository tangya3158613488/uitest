from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 更新时间段
    time_role = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_fend_rules_time")'
    # 规则icon
    rule_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_fend_rules_details")'
    # 关注icon
    attention_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/bt_feed_head_focus")'
    # 播放icon
    feed_icon_play = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/iv_works_state")'
    # 排名icon
    feed_head_rank = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/tv_feed_head_rank")'
    # 用户头像
    feed_head_portrait = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/iv_feed_head_portrait")'
    # 用户头像V标识
    feed_head_vip_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/iv_feed_head_vip_icon")'
    # 用户昵称
    user_name_text_tv = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 用户 vip icon
    user_vip_imageview = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview0")'
    # 用户 歌手等级 icon
    user_singer_imageview = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview1")'
    # 用户 财富等级 icon
    user_wealth_imageview = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview2")'
    # 作品card
    national_rank_work_card = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/fl_works_card")'


class IOS:
    total_rank_btn = MobileBy.IOS_PREDICATE, 'label = "总榜" AND type = "XCUIElementTypeButton"'

    gold_rank_icon = MobileBy.IOS_PREDICATE, "label = '全国金榜' AND type = 'XCUIElementTypeButton'"

    # 更新时间段
    time_role = MobileBy.IOS_PREDICATE, "label CONTAINS '剩余刷新时间' AND type = 'XCUIElementTypeStaticText'"

    # 规则icon
    rule_btn = MobileBy.IOS_PREDICATE, "label = '规则' AND type = 'XCUIElementTypeButton'"
    # 关注icon
    attention_icon = MobileBy.IOS_PREDICATE, "label = '关注' ", 0

    # 播放icon
    feed_icon_play = MobileBy.IOS_PREDICATE, "name = 'feed icon play' AND type = 'XCUIElementTypeButton'", 0
