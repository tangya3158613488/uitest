from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 地区榜text
    region_choose_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("地区")'
    # 已选择的地区
    old_region = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/gps_city_view")'
    # 北京
    beijing = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("北京")', 1
    # 朝阳
    chaoyang = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("朝阳")', 0
    # 东城
    dongcheng = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("东城")', 0
    # 完成
    complete = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("完成")'
    # 定位icon
    region_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/select_city_tv")'
    # 更新时间段和规则
    time_role = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/banner_rule_tv")'


class IOS:
    # 地区榜text
    old_tabBtn = MobileBy.IOS_PREDICATE, "label = '北京榜' AND type = 'XCUIElementTypeButton'"
    # 更新后的地区榜text
    new_tabBtn = MobileBy.IOS_PREDICATE, "name = 'tabBtn已选中' AND type = 'XCUIElementTypeButton'"
    # 已选择地区
    old_region = MobileBy.IOS_PREDICATE, "name = '北京-朝阳' AND type = 'XCUIElementTypeButton'"
    # 更新后的地区
    new_region = MobileBy.IOS_PREDICATE, "name = '北京-东城' AND type = 'XCUIElementTypeButton'"
    # 地区选择一级页title todo
    area_title = MobileBy.IOS_PREDICATE, "name = '地区' AND type = 'XCUIElementTypeNavigationBar' AND enabled ='true'"
    # gps 定位icon
    # gps_icon = MobileBy.ACCESSIBILITY_ID, "location_current"
    gps_icon = MobileBy.IOS_PREDICATE, "name = 'location_current' AND type = 'XCUIElementTypeImage'"
    # gps 定位地区
    gps_area = MobileBy.IOS_PREDICATE, "name = '北京' AND type = 'XCUIElementTypeStaticText'", 0

    gps_area_btn = MobileBy.IOS_PREDICATE, "name = '北京' AND type = 'XCUIElementTypeCell'", 0
    # 北京
    beijing = MobileBy.IOS_PREDICATE, "name = '北京' AND type = 'XCUIElementTypeCell'", 1

    # 朝阳
    chaoyang = MobileBy.IOS_PREDICATE, "label = '朝阳' AND type = 'XCUIElementTypeCell'"
    # 东城
    dongcheng = MobileBy.IOS_PREDICATE, "label = '东城' AND type = 'XCUIElementTypeCell'"
    # 完成
    complete = MobileBy.IOS_PREDICATE, "name = '完成' AND type = 'XCUIElementTypeButton'"

    # 定位icon
    region_icon = MobileBy.IOS_PREDICATE, "name = '北京' AND type = 'XCUIElementTypeButton'"

    # 更新时间段 Dodo
    time_role = MobileBy.IOS_PREDICATE, "name CONTAINS '更新于' AND type ='XCUIElementTypeStaticText'"

    # 规则
    rule_btn = MobileBy.IOS_PREDICATE, 'name ="规则" AND type ="XCUIElementTypeButton"'

    # 我知道了
    i_know_btn = MobileBy.IOS_PREDICATE, 'label ="我知道了" AND type = "XCUIElementTypeStaticText"'

    # 作品card
    work_card = MobileBy.IOS_PREDICATE, "name = 'workcell' AND type = 'XCUIElementTypeOther'", 1

    # 排名icon
    hottest_icon_first = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.1' AND type = 'XCUIElementTypeImage'"

    # 排名icon
    hottest_icon_sec = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.2' AND type = 'XCUIElementTypeImage'"
    # 排名icon
    hottest_icon_three = MobileBy.IOS_PREDICATE, "name = 'hottest_work_NO.3' AND type = 'XCUIElementTypeImage'"