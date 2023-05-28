from appium.webdriver.common.mobileby import MobileBy


class Android:
    total_rank_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 全国btn
    national_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全国")'
    # 地区榜btn
    region_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("地区榜")'
    # 好声音
    voice_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("好声音")'
    # 全国金榜
    national_gold_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全国金榜")'
    # 总榜
    total_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_rightview")'
    # 跑马灯
    banner_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/board_marquee")'
    # 返回按钮
    back_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'

    # 规则
    rule_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("规则")'
    # 规则说明框
    rule_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("规则说明")'
    # 我知道了
    i_know_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我知道了")'

    # 作品card，守护者头像
    protect_head = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/board_contribution_user_iv")'

    # 作品card
    work_card = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/headphoto_work")'
    # 作品card,排名icon
    ranking = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_ranking")'
    # 作品card,点赞
    like = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/board_like_iv")'
    # 歌曲名称
    work_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/work_name_ll")'
    # 用户昵称
    user_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 会员等级
    member_level = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview0")'
    # 歌手等级
    singer_level = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview1")'
    # 财富等级
    wealth_level = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview2")'
    # 认证标识（大V）
    v_logo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/imageview3")'
    # 排名提升标识
    up_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/board_rank_change_tv")'
    # MV标识
    mv_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/mv_tag")'


class IOS:
    total_rank_btn = MobileBy.IOS_PREDICATE, 'label = "总榜" AND type = "XCUIElementTypeButton"'

    # 全国btn
    national_tab = MobileBy.IOS_PREDICATE, 'label = "全国榜" AND type = "XCUIElementTypeButton"'
    # 地区榜btn
    region_tab = MobileBy.IOS_PREDICATE, 'label ="北京榜" AND type ="XCUIElementTypeButton"'
    # 好声音
    voice_tab = MobileBy.IOS_PREDICATE, 'label ="好声音" AND type ="XCUIElementTypeButton"'
    # 全国金榜
    national_gold_tab = MobileBy.IOS_PREDICATE, 'label ="全国金榜" AND type ="XCUIElementTypeButton"'
    # 总榜
    total_tab = MobileBy.IOS_PREDICATE, 'label ="总榜" AND type ="XCUIElementTypeButton"'
    # 更新时间
    update_time_text = MobileBy.IOS_PREDICATE, 'label CONTAINS "更新于" AND type ="XCUIElementTypeStaticText"'
    # 跑马灯
    banner_tab = MobileBy.IOS_PREDICATE, 'label CONTAINS "恭喜" AND type ="XCUIElementTypeStaticText"'
    # 返回按钮
    back_btn = MobileBy.IOS_PREDICATE, 'label ="返回" AND type ="XCUIElementTypeButton"'
    # 规则s
    rule_btn = MobileBy.IOS_PREDICATE, 'label ="规则" AND type ="XCUIElementTypeButton"'
    # 规则说明框
    rule_title = MobileBy.IOS_PREDICATE, 'name ="规则说明" AND type ="XCUIElementTypeStaticText"'
    # 我知道了
    i_know_btn = MobileBy.IOS_PREDICATE, 'label ="我知道了" AND type ="XCUIElementTypeButton"'
    # 作品card，守护者头像
    # protect_head = MobileBy.IOS_PREDICATE,
    # 作品card
    work_card = MobileBy.IOS_PREDICATE, "name = 'workcell' AND type = 'XCUIElementTypeOther'", 1

    # 作品card,排名icon
    # ranking = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.1' AND  enabled='true' AND type = 'XCUIElementTypeImage'"
    # // XCUIElementTypeImage[ @ name = "hottest_work_NO.1"]

    ranking = MobileBy.XPATH, '// XCUIElementTypeImage[ @ name = "hottest_work_NO.1"]'
