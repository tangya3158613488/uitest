from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 歌手名
    singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/singer_name")'
    # 伴奏tab
    acc_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("伴奏")'
    # 合唱tab
    chrous_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("合唱")'
    # 演唱按钮
    sing_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("演唱")'
    # 伴奏tab-演唱按钮
    acc_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn")'
    # 伴奏tab-cell
    acc_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/content_layout")'
    # 伴奏tab-歌手名称
    acc_tab_singer_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/singername")'
    # 伴奏tab-歌曲名称
    acc_tab_song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 作品tab-用户头像
    work_user_headphoto = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/user_head")'
    # 作品tab-作品cell
    work_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/feed_work_bg")'
    # 作品tab-用户昵称
    work_user_nickname = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 作品tab-作品描述
    work_work_content = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/work_content")'
    # 合唱tab-仅显示视频合唱-txt
    only_show_video_chrous_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("仅显示视频合唱")'
    # 合唱tab-仅显示视频合唱-btn
    only_show_video_chrous_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/chorus_only")'
    # 合唱tab-合唱btn
    chrous_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_item")'
    # 合唱tab-MV合唱btn
    chrous_mv_chrous_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MV合唱")'
    # 合唱tab-用户头像
    chrous_user_headphoto = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/headphoto")'
    # 合唱tab-作品cell
    chrous_work_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/chorusinfo")'


class IOS:
    # 歌手名
    singer_name = MobileBy.IOS_PREDICATE, "name='starName'"
    # 伴奏tab
    acc_tab = MobileBy.IOS_PREDICATE, "label='伴奏'"
    # 合唱tab
    chrous_tab = MobileBy.IOS_PREDICATE, "label='合唱'"
    # 作品tab
    work_tab = MobileBy.IOS_PREDICATE, "label='作品'"
    # 伴奏tab-演唱按钮
    acc_sing_btn = MobileBy.IOS_PREDICATE, "label='演唱'"
    # 伴奏tab-cell
    acc_cell = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeCell"'
    # 伴奏tab-歌手名称
    acc_tab_singer_name = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/singername")'
    # 伴奏tab-歌曲名称
    acc_tab_song_name = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 作品tab-用户头像
    work_user_headphoto = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/user_head")'
    # 作品tab-作品cell
    work_cell = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/feed_work_bg")'
    # 作品tab-用户昵称
    work_user_nickname = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 作品tab-作品描述
    work_work_content = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/work_content")'
    # 合唱tab-仅显示视频合唱-txt
    only_show_video_chrous_txt = MobileBy.IOS_PREDICATE, 'new UiSelector().text("仅显示视频合唱")'
    # 合唱tab-仅显示视频合唱-btn
    only_show_video_chrous_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/chorus_only")'
    # 合唱tab-合唱btn
    chrous_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/right_item")'
    # 合唱tab-MV合唱btn
    chrous_mv_chrous_btn = MobileBy.IOS_PREDICATE, 'new UiSelector().text("MV合唱")'
    # 合唱tab-用户头像
    chrous_user_headphoto = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/headphoto")'
    # 合唱tab-作品cell
    chrous_work_cell = MobileBy.IOS_PREDICATE, 'new UiSelector().resourceId("com.changba:id/chorusinfo")'
