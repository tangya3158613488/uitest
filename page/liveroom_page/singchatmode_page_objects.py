from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 工具箱清空魅力值按钮文案
    clear_charm_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清空全部魅力值")'
    # 房间cell元素
    report_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("举报")'
    #在线成员列表元素
    room_users_info_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/room_users_info")'
    #在线成员列表标题
    room_users_info_title_display = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("在线成员列表")'
    #1麦元素
    image_one_seat_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/name")',0
    #点歌按钮cell
    select_song_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/room_play_select_song_tv")'
    #点歌台第一首歌曲排麦按钮
    first_song_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn")',0
    #演唱者姓名cell
    singer_name_displayed = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/room_play_sing_lrcview_tv")'
    #演唱页面设置按钮cell
    song_setting_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/room_play_sing_main_setting")'
    #切歌按钮cell
    finish_song_btn_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("切歌")'
    #判断演唱区是否展示
    singing_area_displayed_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("戴上耳机演唱效果更好哦~")'



class IOS:
    pass