import time

from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.record_page.skin_choose_page import SkinChoosePage
from common.driver.platform_selector import PlatformSelector


class RecordPreparePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver, song_name="", singer=""):
        super().__init__()
        self.appium_driver = appium_driver
        self.song_name = song_name
        self.singer = singer
        self.is_hq = False

    def is_record_prepare_page(self):
        return self.appium_driver.element_displayed(self.get_object("recording_state_btn"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def get_song_name(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("song_name")).text
        else:
            return self.appium_driver.find_element(self.get_object("song_name")).get_attribute("label")

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def get_singer_name(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("singer_name")).text
        else:
            return self.appium_driver.find_element(self.get_object("singer_name")).get_attribute("label")

    def click_exit_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("exit_btn")))

    def is_song_name_shown(self):
        return self.appium_driver.element_displayed(self.get_object("song_name"))

    def wait_for_download(self):
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            text = self.appium_driver.find_element(self.get_object("recording_state_btn")).get_attribute("label")
        else:
            text = self.appium_driver.find_element(self.get_object("recording_state_btn")).get_attribute("content-desc")
        while text != "演唱":
            if AppiumDriver.get_platform() == PlatformSelector.IOS:
                self.appium_driver.wait_for(5, False)
                text = self.appium_driver.find_element(self.get_object("recording_state_btn")).get_attribute(
                    "label")
            else:
                self.appium_driver.wait_for(5, False)
                text = self.appium_driver.find_element(self.get_object("recording_state_btn")).get_attribute(
                    "content-desc")

    def is_singer_name_shown(self):
        return self.appium_driver.element_displayed(self.get_object("singer_name"))

    def is_exit_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("exit_btn"))

    def is_recording_state_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("recording_state_btn"))

    def is_change_skin_btn_shown(self):
        return self.appium_driver.element_displayed(self.get_object("change_skin_btn"))

    def is_clip_sing_btn_selected(self):
        return self.appium_driver.find_element(self.get_object("clip_sing_btn")).is_selected()

    def is_all_sing_btn_selected(self):
        return self.appium_driver.find_element(self.get_object("all_sing_btn")).is_selected()

    def is_duet_sing_btn_selected(self):
        return self.appium_driver.find_element(self.get_object("duet_sing_btn")).is_selected()

    def is_single_sing_btn_selected(self):
        return self.appium_driver.find_element(self.get_object("single_sing_btn")).is_selected()

    def click_my_order_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_order_btn")))

    def click_others_order_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("others_order_btn")))

    def click_agent_distinguish_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("agent_distinguish_btn")))

    def is_my_order_btn_selected(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("my_order_btn")).is_selected()
        return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("my_order_btn")),
                                                "value") == "1"

    def is_others_order_btn_selected(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("others_order_btn")).is_selected()
        return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("others_order_btn")),
                                                "value") == "1"

    def is_agent_distinguish_btn_selected(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.find_element(self.get_object("agent_distinguish_btn")).is_selected()
        return self.appium_driver.get_attribute(
            self.appium_driver.find_element(self.get_object("agent_distinguish_btn")),
            "value") == "1"

    def is_mode_btn_shown(self):
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.appium_driver.element_displayed(self.get_object("change_to_video_mode_btn"))
        else:
            return self.appium_driver.element_displayed(self.get_object("mode_btn"))

    def is_earphone_tip_shown(self):
        return self.appium_driver.element_displayed(self.get_object("earphone_tip"))

    def click_all_sing_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("all_sing_btn")))

    def click_clip_sing_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clip_sing_btn")))

    def click_duet_sing_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("duet_sing_btn")))

    def click_skin_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("change_skin_btn")))
        return SkinChoosePage(self.appium_driver)

    def is_hq_accompany(self):
        text = self.appium_driver.find_element(self.get_object("hq_tag")).text
        return 0 if text == "切换为HQ高清伴奏" else 1

    def click_sing_state_btn(self):
        print(time.localtime(time.time()))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("recording_state_btn")))

    # 安卓切模式，iOS切换成音频模式
    def click_change_to_audio_btn(self):
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            self.appium_driver.press_element(
                self.appium_driver.find_element(self.get_object("change_to_audio_mode_btn")))
        else:
            self.appium_driver.press_element(
                self.appium_driver.find_element(self.get_object("mode_btn")))

    # iOS切换成视频模式
    def click_change_to_video_btn(self):
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("change_to_video_mode_btn")))

    def is_audio_mode(self):
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            if self.appium_driver.element_displayed(self.get_object("change_to_video_mode_btn")):
                return True
            else:
                return False
        else:
            text = self.appium_driver.find_element(self.get_object("mode_btn")).get_attribute("content-desc")
            if text == "音视频切换按钮,当前音频录制模式":
                return True
            else:
                return False

    def close_tip(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_img")))
            return
        w = self.appium_driver.find_element(self.get_object("earphone_tip")).size["width"]
        h = self.appium_driver.find_element(self.get_object("earphone_tip")).size["height"]
        x = self.appium_driver.find_element(self.get_object("earphone_tip")).location['x'] + w - w * 1 / 10
        y = self.appium_driver.find_element(self.get_object("earphone_tip")).location['y'] + h / 2
        print("width is {},height is {},x is {},y is {}".format(w, h, x, y))
        return self.appium_driver.press_location(x, y)

    def is_my_order_btn_shown(self):
        """
        我先唱按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_order_btn"))

    def is_others_order_btn_shown(self):
        """
        我后唱按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("others_order_btn"))

    def is_agent_distinguish_btn_shown(self):
        """
        智能识别按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("agent_distinguish_btn"))

    def is_left_photo_shown(self):
        """
        发起合唱左侧头像是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("left_photo"))

    def is_right_photo_shown(self):
        """
        发起合唱左侧头像是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("right_photo"))
