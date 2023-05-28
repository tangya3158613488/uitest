import re
import time

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.sing_page.sing_page import SingPage
from page.record_page.record_complete_page import RecordCompletePage


class RecordRecordingPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver, song_name="", singer="", is_hq=False):
        super().__init__()
        self.appium_driver = appium_driver
        self.song_name = song_name
        self.singer = singer
        self.is_hq = is_hq

    def is_hq_accompany(self):
        """
        伴奏是否为hq
        :return:True/False
        """
        return self.appium_driver.element_displayed(self.get_object("hq_tag"))

    def get_song_name(self):
        """
        get 歌名
        :return: 歌名
        """
        return self.appium_driver.find_element(self.get_object("song_name")).text

    def is_exit_btn_shown(self):
        """
        退出按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("exit_btn"))

    def click_exit_btn(self):
        """
        点击左上角放弃按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("exit_btn")))

    def exit_recording(self):
        """
        退出录制方法
        :return: 点歌台页面
        """
        self.click_exit_btn()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("forgive_record_btn")))
        return SingPage(self.appium_driver)

    def is_song_name_shown(self):
        """
        歌名是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("song_name"))

    def is_singer_name_shown(self):
        """
        歌手名是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("singer_name"))

    def is_mode_btn_shown(self):
        """
        音视频录制模式按钮
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("mode_btn"))

    def is_first_guide_shown(self):
        """
        首句助唱按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("first_guide_btn"))

    def click_score_controller(self):
        """
        点击收起/展开打分器按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("score_control_btn")))

    def click_score_controller_unfold(self):
        """
        iOS点击展开打分器按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("score_control_unfold_btn")))
        time.sleep(5)

    def get_score_controller_des(self):
        """
        get 收起/展开打分器
        :return: "收起打分器"/"展开打分器"
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(
                self.get_object("score_control_btn")), "name")
        else:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(
                self.get_object("score_control_btn")), "content-desc")

    def is_score_view_shown(self):
        """
        打分器view是否展示(视频&合唱模式不显示得分等级)
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("score_level_view"))

    def is_score_container_view_shown(self):
        """
        打分器是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("score_container_view"))

    def is_volume_prompt_view_shown(self):
        """
        音量电平是否展示
        :return:True/False
        """
        return self.appium_driver.element_displayed(self.appium_driver.find_element(self.get_object("volume_prompt_view")))

    def is_lyrics_view_shown(self):
        """
        歌词区域是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("score_container_view"))

    def is_first_lyric_help_tip_shown(self):
        """
        首句助唱是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("first_lyric_help"))

    def click_first_lyric_help_tip(self):
        """
        点击首句助唱
        :return: True/False
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("first_lyric_help")))

    def is_original_btn_selected(self):
        """
        领唱是否选中
        """
        return self.appium_driver.find_element(self.get_object("original_btn")).get_attribute("accessible")

    def is_skip_prelude_tip_shown(self):
        """
        跳过前奏是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("skip_prelude"))

    def is_chorus_head_shown(self):
        """
        合唱头像是否展示
        :return: True/False
        """
        print(self.appium_driver.get_page_source())
        if self.appium_driver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.element_displayed(self.get_object("right_photo")) & self.appium_driver.element_displayed(self.get_object("left_photo"))
        return self.appium_driver.element_displayed(self.get_object("chorus_head"))

    def wait_for_recording_complete(self):
        """
        等待录制至【（伴奏的分钟数）*60-5】s，防止整分钟数伴奏因自动化运行的时间不够
        :return:
        """
        # record_time = int(self.get_full_time()[0]) * 60 - 5
        record_time = 30
        time.sleep(record_time)

    # 更多按钮————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def click_more_btn(self):
        """
        点击右上角更多按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn")))

    def is_more_btn_shown(self):
        """
        更多按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("more_btn"))

    # 放大歌词
    def is_enlarge_lyrics_btn_shown(self):
        """
        放大歌词按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("enlarge_lyrics_btn"))

    def click_enlarge_lyrics_btn(self):
        """
        点击放大歌词按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("enlarge_lyrics_btn")))

    # 还原歌词
    def is_restore_lyrics_btn_shown(self):
        """
        还原歌词按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("restore_lyrics_btn"))

    def click_restore_lyrics_btn(self):
        """
        点击还原歌词按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("restore_lyrics_btn")))

    # 功能帮助
    def is_help_btn_shown(self):
        """
        功能帮助按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("help_btn"))

    def click_help_btn(self):
        """
        点击功能帮助按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("help_btn")))

    # 反馈问题
    def is_report_btn_shown(self):
        """
        反馈问题按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("report_btn"))

    def click_report_btn(self):
        """
        点击反馈问题按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("report_btn")))

    def click_cancle_btn(self):
        """
        点击更多actionsheet中的取消
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancle_btn")))

    # 底部btn方法——————————————————————————————————————————————————————————————————————————————————
    def is_recording_state_btn_shown(self):
        """
        演唱按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("recording_state_btn"))

    def get_recording_state_des(self):
        """
        获取播放按钮状态
        :return: 演唱按钮description
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(
                self.get_object("recording_state_btn")), "label")
        else:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(
                self.get_object("recording_state_btn")), "content-desc")

    def get_stop_state_des(self):
        """
        获取暂停按钮状态
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(
            self.get_object("stop_state_btn")), "label")

    def click_sing_state_btn(self):
        """
        点击演唱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("recording_state_btn")))
        print("完成点击")

    def click_stop_state_btn(self):
        """
        点击暂停按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("stop_state_btn")))

    def is_original_btn_shown(self):
        """
        原唱按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("original_btn"))

    def click_original_btn(self):
        """
        点击原唱按钮
        :return: True/False
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("original_btn")))

    def get_original_btn_enabled(self):
        """
        原唱按钮是否置灰
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(
               self.get_object("original_btn")), "enabled")

    def is_volume_btn_shown(self):
        """
        调音台按钮是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("volume_btn"))

    def click_volume_btn(self):
        """
        点击调音台按钮
        :return: True/False
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("volume_btn")))

    def is_re_record_btn_shown(self):
        """
        重唱按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("re_record_btn"))

    def click_re_record_btn(self):
        """
        点击重唱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("re_record_btn")))

    def get_dialog_text(self):
        """
        获取弹窗内容
        :return:text
        """
        return self.appium_driver.find_element(self.get_object("dialog_text")).text

    def is_dialog_shown(self):
        """
        弹窗是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("dialog_text"))

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=True)
    def wait_dialog_displayed(self):
        """
        等待弹框出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("dialog_confirm"))

    def click_dialog_confirm_btn(self):
        """
        点击弹窗-确认按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dialog_confirm")))
        time.sleep(5)

    def click_dialog_cancel_btn(self):
        """
        点击弹窗-取消按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dialog_cancel")))

    def is_finish_btn_shown(self):
        """
        完成按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("finish_btn"))

    def click_finish_btn(self):
        """
        点击完成按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("finish_btn")))

    def get_time(self):
        """
        返回全部录制时间
        :return: Android：00:00/00:00；iOS：当前0分3秒, 总时长4分8秒
        """
        text = str(self.appium_driver.find_element(self.get_object("time_view")).text)
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            print(re.findall(r'\d+', text))
            return re.findall(r'\d+', text)
        else:
            return text.split("/")

    def get_recording_time(self):
        """
        返回录制时长
        :return:
        """
        return self.get_time()[0].split(":")

    def get_full_time(self):
        """
        返回歌曲总时长
        :return:
        """
        return self.get_time()[1].split(":")

    # 调音台方法——————————————————————————————————————————————————————————————————————————————————
    def is_earphone_monitor_txt_shown(self):
        """
        耳机监听txt是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("earphone_monitor_txt"))

    def is_earphone_monitor_btn_shown(self):
        """
        耳机监听btn是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("earphone_monitor_btn"))

    def is_voice_txt_shown(self):
        """
        人声txt是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("voice_txt"))

    def is_voice_bar_shown(self):
        """
        人声bar是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("voice_bar"))

    def get_voice_bar_enabled(self):
        """
        人声bar是否置灰
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(
               self.get_object("voice_bar")), "enabled")

    def is_accompany_txt_shown(self):
        """
        伴奏txt是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("accompany_txt"))

    def is_accompany_bar_shown(self):
        """
        伴奏bar是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("accompany_bar"))

    def get_accompany_bar_enabled(self):
        """
        伴奏bar是否置灰
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(
               self.get_object("accompany_bar")), "enabled")

    def is_tone_txt_shown(self):
        """
        变调txt是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("tone_txt"))

    def is_tone_down_btn_shown(self):
        """
        降调btn是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("tone_down_btn"))

    def click_tone_down_btn(self):
        """
        点击降调btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("tone_down_btn")))

    def get_tone_down_btn_enabled(self):
        """
        降调btn是否置灰
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(
               self.get_object("tone_down_btn")), "enabled")

    def click_tone_up_btn(self):
        """
        点击升调btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("tone_up_btn")))

    def is_tone_up_btn_shown(self):
        """
        升调btn是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("tone_up_btn"))

    def get_tone_up_btn_enabled(self):
        """
        升调btn是否置灰
        :return:
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(
               self.get_object("tone_up_btn")), "enabled")

    def is_tone_bar_shown(self):
        """
        变调bar是否展示
        :return: True/False
        """
        return self.appium_driver.element_displayed(self.get_object("tone_bar"))

    def is_complete_dialog_shown(self):
        """
        合成进度弹窗是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("dialog_content"))


