import time

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController


class RecordCompletePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver, song_name="", singer="", is_hq=False):
        super().__init__()
        self.appium_driver = appium_driver
        self.song_name = song_name
        self.singer = singer
        self.is_hq = is_hq

    def is_background_view_shown(self):
        """
        背景区域是否显示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("background_view"))

    def get_song_name(self):
        """
        get 歌名
        :return: 歌名
        """
        return self.appium_driver.find_element(self.get_object("song_name")).text

    def is_generate_btn_shown(self):
        """
        合成进度是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("generate_btn"))

    def is_score_btn_shown(self):
        """
        单句得分入口是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("score_icon"))

    def click_change_background_btn(self):
        """
        点击换背景按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("change_background_btn")))

    def is_change_background_btn_shown(self):
        """
        换背景按钮是否展示（视频不应展示，音频基本都展示）
        :return:True/Fasle
        """
        return self.appium_driver.element_displayed(self.get_object("change_background_btn"))

    def click_lyrics_btn(self):
        """
        点击歌词特效按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("lyrics_btn")))

    def is_lyrics_btn_shown(self):
        """
        歌词特效按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("lyrics_btn"))

    def is_full_screen_btn_shown(self):
        """
        视频录制完成页全屏按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("full_screnn_btn"))

    def click_generate_btn(self):
        """
        点击生成作品按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("generate_work")))

    def click_save_btn(self):
        """
        点击保存作品按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("save_work")))

    def is_process_view_shown(self):
        """
        合成进度是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("generate_process_view"))

    def click_close_btn(self):
        """
        点击关闭按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_btn")))

    def is_close_btn_shown(self):
        """
        关闭按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("close_btn"))

    def click_forgive_btn(self):
        """
        点击放弃按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("forgive_save_btn")))

    def is_play_btn_shown(self):
        """
        播放按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("play_btn"))

    def click_dialog_confirm_btn(self):
        """
        点击弹窗-确认按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dialog_confirm")))
        time.sleep(2)

    def is_dialog_confirm_btn(self):
        """
        弹窗-确认按钮是否展示
        :return:
        """
        self.appium_driver.element_displayed(self.get_object("dialog_confirm"))

    def get_left_time(self):
        """
        返回时间轴左侧时间
        :return: list = (00:00).split(':')
        """
        text = str(self.appium_driver.find_element(self.get_object("left_time")).text)
        return text.split(":")

    def get_right_time(self):
        """
        返回时间轴右侧时间
        :return: list = (00:00).split(':')
        """
        text = str(self.appium_driver.find_element(self.get_object("right_time")).text)
        return text.split(":")
    # 换背景list——————————————————————————————————————————————————————————————————————————————————————————————
    def is_choose_gif_img_shown(self):
        """
        GIF动图按钮是否展示
        :return: Boolean
        """
        return self.appium_driver.element_displayed(self.get_object("choose_gif_img"))

    def click_choose_gif_img(self):
        """
        点击GIF动图
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("choose_gif_img")))

    def is_local_img_shown(self):
        """
        本地相册按钮是否展示
        :return: Boolean
        """
        return self.appium_driver.element_displayed(self.get_object("local_img"))

    def click_local_img(self):
        """
        点击本地相册
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("local_img")))

    def is_headphoto_img_shown(self):
        """
        头像相册按钮是否展示
        :return: Boolean
        """
        return self.appium_driver.element_displayed(self.get_object("headphoto_img"))

    def click_headphoto_img(self):
        """
        点击头像相册
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("headphoto_img")))

    def is_clear_img_shown(self):
        """
        清空按钮是否展示
        :return: Boolean
        """
        return self.appium_driver.element_displayed(self.get_object("clear_img"))

    def click_clear_img(self):
        """
        点击清空
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clear_img")))

    def is_cancel_choose_img_shown(self):
        """
        取消按钮是否展示
        :return: Boolean
        """
        return self.appium_driver.element_displayed(self.get_object("cancel_choose_img"))

    def click_cancel_choose_img(self):
        """
        点击取消
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_choose_img")))
    # 歌词特效面板———————————————————————————————————————————————————————————————————————————————————————————————————————————-
    def is_lyrics_board_shown(self):
        """
        歌词特效面板是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("lyrics_board_text"))

    def is_lyrics_board_option_shown(self):
        """
        歌词特效面板无特效按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("lyrics_board_none_btn"))

    def close_lyrics_board(self):
        """
        关闭歌词特效面板
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("lyrics_board_close_btn")))

    # 单句得分页面———————————————————————————————————————————————————————————————————————————————————————————————————————————-
    def click_score_btn(self):
        """
        点击单句得分入口
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("score_icon")))

    def is_score_title_show(self):
        """
        单句得分页面title是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("score_page_title"))

    def close_score_page(self):
        """
        关闭单句得分页面
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("score_page_close")))

    def click_show_off_score_btn(self):
        """
        点击晒成绩入口
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("show_off_score_btn")))

    def is_show_off_score_title_shown(self):
        """
        晒成绩页面title是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("show_off_score_page_title"))

    def back_to_score_page(self):
        """
        点击返回到单句得分页面
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("show_off_score_page_back")))

    # 底部tab———————————————————————————————————————————————————————————————————————————————————————————————————————————-
    def click_fix_tab(self):
        """
        点击修音tab
        :return: True/False
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("fix_tab")))

    def is_fix_tab_selected(self):
        """
        修音tab是否选中
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("fix_tab")).is_selected()

    def is_ios_fix_tab_selected(self):
        """
        修音tab是否选中
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("fix_tab_selected"))

    def click_effect_tab(self):
        """
        点击混响tab
        :return: True/False
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("effect_tab")))

    def is_effect_tab_selected(self):
        """
        混响tab是否选中
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("effect_tab")).is_selected()

    def is_ios_effect_tab_selected(self):
        """
        混响tab是否选中
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("effect_tab_selected"))

    def click_timbre_tab(self):
        """
        点击音色tab
        :return: True/False
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("timbre_tab")))

    def is_timbre_tab_selected(self):
        """
        音色tab是否选中
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("timbre_tab")).is_selected()

    def is_ios_timbre_tab_selected(self):
        """
        音色tab是否选中
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("timbre_tab_selected"))

    def click_denoise_tab(self):
        """
        点击降噪tab
        :return: True/False
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("denoise_tab")))

    def is_denoise_tab_selected(self):
        """
        降噪tab是否选中
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("denoise_tab")).is_selected()

    def is_ios_denoise_tab_selected(self):
        """
        降噪tab是否选中
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("denoise_tab_selected"))

    def click_volume_tab(self):
        """
        点击音量tab
        :return: True/False
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("volume_tab")))

    def is_volume_tab_selected(self):
        """
        音量tab是否选中
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("volume_tab")).is_selected()

    def is_ios_volume_tab_selected(self):
        """
        音量tab是否选中
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("volume_tab_selected"))

    def click_re_record(self):
        """
        点击重唱按钮
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("re_record")))

    # 混响tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    def is_pop_btn_shown(self):
        """
        流行按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("pop"))

    # 音色tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    def is_fast_adjust_btn_shown(self):
        """
        快速调节按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("fast_adjust_btn"))

    # 降噪tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    def is_lite_denoise_btn_shown(self):
        """
        轻度降噪按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("lite_denoise_btn"))

    # 音量tab——————————————————————————————————————————————————————————————————————————————————————————————————————
    def is_volume_view_shown(self):
        """
        "伴奏"是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("volume_view"))

    def is_accompany_view_shown(self):
        """
        "人声"是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("accompany_view"))

    # 视频录制完成页——更多按钮——————————————————————————————————————————————————————————————————————————————————————————————————————

    def more_btn_click(self):
        """
        更多按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn")))

    def click_cancel_btn(self):
        """
        点击更多actionsheet中的取消
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_btn")))

    def is_clips_blue_btn_gray(self):
        """
        片段补录是否置灰
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("clips_blue")).get_attribute("enabled")

    def is_clips_cut_btn_gray(self):
        """
        片段截取是否置灰
        :return: True/False
        """
        return self.appium_driver.find_element(self.get_object("clips_cut")).get_attribute("enabled")

    def is_clips_cut_btn_shown(self):
        """
        片段截取是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("clips_cut"))

    def click_help_btn(self):
        """
        点击反馈问题按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("help_btn")))

    def click_report_btn(self):
        """
        点击反馈问题按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("report_btn")))

    def report_actionsheet_shown(self):
        """
        问题反馈的actionsheet内容
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("report_btn")))

    # 视频录制完成页——全屏页面——————————————————————————————————————————————————————————————————————————————————————————————————————
    def click_full_screen_btn(self):
        """
        点击全屏按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("full_screen_btn")))

    def click_close_full_screen_btn(self):
        """
        点击关闭全屏按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_full_screen_btn")))

    def click_full_screen_stop_btn(self):
        """
        全屏页面点击暂停按钮
        :return:
        """
        print("点击暂停按钮")
        self.appium_driver.press_element(
            self.appium_driver.find_elements(self.get_object("stop_btn_in_full_screen_page"))[1])

    def click_full_screen_play_btn(self):
        """
        全屏页面点击播放按钮
        :return:
        """
        print("点击播放按钮")
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_btn_in_full_screen_page")))
            return
        self.appium_driver.press_element(
            self.appium_driver.find_elements(self.get_object("play_btn_in_full_screen_page"))[1])

    def get_full_screen_play_btn_text(self):
        """
        全屏页面获取播放按钮文案
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("play_btn_in_full_screen_page")).get_attribute("content-desc")
        return self.appium_driver.find_elements(self.get_object("play_btn_in_full_screen_page"))[1].get_attribute("label")

    def get_full_screen_stop_btn_text(self):
        """
        全屏页面获取暂停按钮文案
        :return:
        """
        return self.appium_driver.find_elements(self.get_object("stop_btn_in_full_screen_page"))[1].get_attribute("label")

    def is_clips_title_shown(self):
        """
        截取片段半屏title是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("clips_title"))

    def is_reset_clip_btn_shown(self):
        """
        还原整段按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("reset_clip_btn"))

    def click_reset_clip_btn(self):
        """
        点击还原整段按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("reset_clip_btn")))

    def click_clip_confirm(self):
        """
        点击截取片段-确认
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clip_confirm")))

    def click_clip_cancel(self):
        """
        点击截取片段-取消
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clip_cancel")))

    def click_clip_cut(self):
        """
        点击X-截取片段按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clips_cut")))

    def input_text(self, text):
        """
        在弹窗中输入文字
        :param text:
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("input_text")),text)

    def is_input_text_shown(self):
        """
        输入歌名弹窗是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("input_text"))

    def get_input_text_text(self):
        """
        获取输入弹窗默认文案
        :return:
        """
        return self.appium_driver.find_element(self.get_object("input_text")).text
