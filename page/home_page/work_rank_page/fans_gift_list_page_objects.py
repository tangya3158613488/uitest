from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 贡献榜title
    fans_contribute_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("粉丝贡献榜")'
    # 礼物箱btn
    gift_box_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("礼物箱")'
    # 用户头像
    head_photo = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/headphoto")'
    # 用户昵称
    user_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/username")'
    # 财富等级
    leverl_wealth = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/level_text_tip")'
    # 送出礼物额度
    contribute_coin_count = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/contribute_coin_count")'
    # 礼物icon
    gift_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/gift")'
    # 踢榜btn
    board_attacker = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("踢榜")'

    # 作品收到礼物列表
    work_receive_gift_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品收到的礼物")'
    # 礼物icon
    gift_image = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/image_tip")'
    # 返回按钮
    back_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/my_lefttview")'


class IOS:
    # 贡献榜title
    fans_contribute_title = MobileBy.IOS_PREDICATE, 'label = "礼物贡献" AND type = "XCUIElementTypeNavigationBar"'
    # 礼物箱btn
    gift_box_btn = MobileBy.IOS_PREDICATE, 'label = "礼物箱" AND type = "XCUIElementTypeButton"'
    # 用户头像
    # head_photo = MobileBy.IOS_PREDICATE, 'label = "头像" AND type = "XCUIElementTypeOther"'
    # 用户昵称
    user_name = MobileBy.IOS_PREDICATE, 'name = "nickName" AND type = "XCUIElementTypeStaticText"'
    # 财富等级
    leverl_wealth = MobileBy.IOS_PREDICATE, 'name = "gold_diamond_gray" AND type = "XCUIElementTypeImage"', 1
    # 送出礼物额度
    contribute_coin_count = MobileBy.IOS_PREDICATE, 'name CONTAINS "送出" AND type = "XCUIElementTypeStaticText"', 1
    # 礼物icon
    gift_icon = MobileBy.IOS_PREDICATE, 'label = "礼物贡献" AND type = "XCUIElementTypeNavigationBar"'
    # 踢榜btn
    board_attacker = MobileBy.IOS_PREDICATE, 'label = "踢榜" AND type = "XCUIElementTypeButton"', 1

    # 作品收到礼物列表
    work_receive_gift_title = MobileBy.IOS_PREDICATE, 'name = "作品收到的礼物" AND type = "XCUIElementTypeNavigationBar"'
    # 礼物icon
    gift_image = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeImage"', 1
    # 返回按钮
    back_btn = MobileBy.IOS_PREDICATE, 'label = "礼物贡献" AND type = "XCUIElementTypeButton"'

