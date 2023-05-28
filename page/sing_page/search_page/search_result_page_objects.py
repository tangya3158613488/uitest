from appium.webdriver.common.mobileby import MobileBy

# 搜索结果：预期歌名
song_name_except_result = '简单爱'
# 搜索结果：预期歌手名
singer_name_except_result = "周杰伦"


class Android:
    # 搜索框
    search_frame_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_input_box")'
    # 伴奏tab
    acc_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("伴奏")'
    # 合唱tab
    chorus_tab = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("合唱")'
    # 歌曲名称
    song_name_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")', 0
    # 歌手名称
    singer_name_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/singername")', 0
    # 更多版本 按钮
    more_version_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更多版本")', 0
    # 查看全部版本 按钮
    view_all_version_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查看全部版本")'
    # # 搜索违规词和违禁词时 当前暂时没有数据 文案展示
    # search_illegal_word_show_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("很抱歉，未找到相关结果     我要反馈 >")'
    # 搜索违禁词，提示很抱歉，未找到相关结果
    search_illegal_word_show = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/rv_with_footer_empty_title")'
    # 未搜索到歌曲时-当前暂时没有数据-文案展示
    no_result_show_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("你会唱的歌也太多了吧~小唱居然没找到呢")'
    # 未搜索到歌曲时-立即反馈btn
    no_result_feedback_now_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/feedback_btn")'
    # 未搜索到歌曲时-上传伴奏btn 上传伴奏
    no_result_upload_acc_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("上传伴奏")'
    # 底部立即反馈btn feedback_view2
    down_feedback_now_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/feedback_view2")'
    # 仅显示视频合唱 text
    only_show_video_chrous_txt = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("仅显示视频合唱")'
    # 开启仅显示视频合唱 btn
    open_only_show_video_chrous = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/chorus_only")'
    # 待唱 btn
    wait_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_add")'
    # 合唱按钮 right_item
    chorus_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/right_item")'
    # mv合唱按钮
    mv_chorus_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MV合唱")'

class IOS:
    # 伴奏tab
    acc_tab = MobileBy.IOS_PREDICATE, 'label = "伴奏" AND type = "XCUIElementTypeButton"'
    # 合唱tab
    chorus_tab = MobileBy.IOS_PREDICATE, 'label = "合唱" AND type = "XCUIElementTypeButton"'
    # todo 歌曲名称和歌手名称获取不到
    # 更多版本 按钮
    more_version_btn = MobileBy.IOS_PREDICATE, 'label = "更多版本" AND type = "XCUIElementTypeButton"'
    # 查看全部版本 按钮
    view_all_version_btn = MobileBy.IOS_PREDICATE, 'label = "查看全部版本" AND type = "XCUIElementTypeStaticText"'
    # 搜索违规词和违禁词时 当前暂时没有数据 文案展示
    search_illegal_word_show_text = MobileBy.IOS_PREDICATE, 'label = "你会唱的歌也太多了吧~小唱居然没找到呢" AND type = "XCUIElementTypeStaticText"'
    # 未搜索到歌曲时-你会唱的歌也太多了吧~小唱居然没找到呢-文案展示
    no_result_show_text = MobileBy.IOS_PREDICATE, 'label = "你会唱的歌也太多了吧~小唱居然没找到呢" AND type = "XCUIElementTypeStaticText"'
    # 未搜索到歌曲时-立即反馈btn
    no_result_feedback_now_btn = MobileBy.IOS_PREDICATE, 'label = "立即反馈" AND type = "XCUIElementTypeButton"'
    # 未搜索到歌曲时-上传伴奏btn 上传伴奏
    no_result_upload_acc_btn = MobileBy.IOS_PREDICATE, 'label = "上传伴奏" AND type = "XCUIElementTypeButton"'
    # 底部立即反馈btn feedback_view2
    down_feedback_now_btn = MobileBy.IOS_PREDICATE, 'label = "立即反馈" AND type = "XCUIElementTypeButton"'
