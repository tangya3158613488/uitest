from appium.webdriver.common.mobileby import MobileBy


class Android:
    # 副房主按钮
    vice_house_owner_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cell_layout")',2
    # 游戏模式副房主
    vice_house_owner_btn1 = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cell_layout")',3
    # 管理员按钮按钮
    administrator_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cell_layout")',3
    # 游戏模式管理员按钮
    administrator_btn1 = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cell_layout")', 4
    #签约主播按钮
    sign_anchor_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cell_layout")',4
    # 游戏模式签约主播按钮
    sign_anchor_btn1 = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/cell_layout")', 5
    #定制房间专属按钮
    room_exclusive_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("订制房间专属歌曲")'
    #歌曲cell
    song_nane_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/songname")'
    #房间专属歌曲编辑按钮
    room_exclusive_edit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("编辑")'
    #房间专属歌曲全选按钮
    room_exclusive_choose_all_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/choose_all")'
    #房间专属歌曲删除按钮
    room_exclusive_delete_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/delete")'
    #房间专属歌曲页面，添加歌曲页面
    add_room_exclusive_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("添加歌曲")'
    #房间专属搜索歌曲框cell
    searchbar_input_box_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_input_box")'
    #搜索按钮cell
    searchbar_search_submit_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_search_submit")'
    #房间专属歌曲添加按钮
    add_song_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn")',0
    #房间专属歌曲搜索页面取消按钮
    cancel_search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("取消")'
    #房间专属歌曲title
    room_exclusive_song_page_title = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("房间专属歌曲")'


class IOS:
    pass