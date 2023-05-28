from appium.webdriver.common.mobileby import MobileBy

# 搜索正常伴奏
normal_acc = '简单爱'
# 违规词和违禁词伴奏
illegal_acc = '杀人'
# 搜索无结果伴奏
no_result_acc = 'jhshshdj'
# 最佳伴奏 搜索词
best_acc = '漠河舞厅'
# 搜索联想词 歌手
associate_singer = '周杰伦'

class Android:
    # 搜索框
    search_frame_id = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/searchbar_input_box")'
    # 搜索按钮
    search_btn_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜索")'
    # 历史搜索标题
    history_search_title_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("历史搜索")'
    # 确认清空历史搜索弹窗提示文案
    confirm_clear_popup_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定清空历史搜索吗？")'
    # 二次确认清空历史搜索弹窗确认btn
    confirm_clear_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")'
    # 清除历史搜索btn
    clear_history_search_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/arrow")'
    # 热搜榜标题
    hot_search_list_title_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("热搜榜")'
    # 热搜榜-更多btn
    hot_search_more_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更多")'
    # 热搜榜-第一个cell（text=经典老歌）
    hot_search_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/hot_word")', 0
    # 最佳伴奏歌曲名
    best_acc_cell_song_name = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/text_tv")'
    # 最佳伴奏演唱按钮
    best_acc_sing_btn = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/btn")'
    # 最佳伴奏播放按钮
    best_acc_play_icon = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/img_play_or_pause")'
    # 联想词cell
    associate_word_cell = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/constraint")'
    # 联想词 text
    associate_word_text = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.changba:id/song_name")'


class IOS:
    # 搜索框
    search_frame_id = MobileBy.IOS_PREDICATE, 'type = "XCUIElementTypeSearchField"'
    # 搜索按钮
    search_btn_text = MobileBy.IOS_PREDICATE, 'label in {"搜索", "search"} AND visible=true'
    # 热搜榜标题
    hot_search_list_title_text = MobileBy.IOS_PREDICATE, 'label = "热搜榜" AND type = "XCUIElementTypeStaticText"'
    # 历史搜索标题
    history_search_title_text = MobileBy.IOS_PREDICATE, 'label = "历史搜索" AND type = "XCUIElementTypeStaticText"'
    # 确认清空历史搜索弹窗提示文案
    confirm_clear_popup_text = MobileBy.IOS_PREDICATE, 'label = "确定清空历史搜索吗"'
    # 二次确认清空历史搜索弹窗确认btn
    confirm_clear_btn = MobileBy.IOS_PREDICATE, 'label = "确定"'
    # 清除历史搜索btn
    clear_history_search_btn = MobileBy.IOS_PREDICATE, 'label = "删除搜索历史" AND type ="XCUIElementTypeButton"'
    # 热搜榜-更多btn
    hot_search_more_btn = MobileBy.IOS_PREDICATE, 'label = "更多" AND type ="XCUIElementTypeStaticText"'
    # 热搜榜-第一个cell
    hot_search_cell = MobileBy.IOS_PREDICATE, 'name = "hotSearch"', 0
