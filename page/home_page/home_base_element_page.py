#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.driver.appium_driver import AppiumDriver
from page.home_page.attention_page.dynamic_details_page import DynamicDetailsPage
from page.home_page.topic_detail_page.topic_detail_page import TopicDetailPage
from page.ktv_page.ktv_page import KtvPage
from page.ktv_page.my_tab_creat_room_page import MyTabCreateRoomPage
from page.live_page.live_page import LivePage
from page.me_page.dress_page import DressPage
from page.me_page.person_page import PersonPage
from page.objects_controller import ObjectsController
from page.home_page.attention_page.release_dynamic_page import PublishDynamicPage
# from page.home_page.attention_all_page import AttentionAllPage
from page.player_page.player_page import PlayerPage


class HomeBaseElementPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        self.LIVE = "直播"
        self.KTV = "KTV"

    def publish_dynamic_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("send_dynamic_id")))
        return PublishDynamicPage(self.appium_driver)

    def zan_click(self):
        self.element_click_util("zan_id")

    def get_zan_num(self):
        for i in range(6):
            if self.appium_driver.element_displayed(self.get_object("zan_id")):
                zan = self.appium_driver.find_element(self.get_object("zan_id")).text
                if str(zan) == "点赞":
                    print("zan is %s " % zan)
                    return str(zan)
                else:
                    return int(zan)

            else:
                self.swipe_up(1000)

    def dynamic_zan_click(self):
        self.element_click_util("dynamic_zan_id")

    def get_dynamic_zan_num(self):
        for i in range(6):
            if self.appium_driver.element_displayed(self.get_object("dynamic_zan_id")):
                zan = self.appium_driver.find_element(self.get_object("dynamic_zan_id")).text
                if str(zan) == "点赞":
                    print("dynamic_zan_id is %s " % zan)
                    return str(zan)
                else:
                    return int(zan)

            else:
                self.swipe_up(1000)

    def swipe_up(self, t):
        device_height = self.appium_driver.device_height()
        end_height = device_height * 0.3
        start_height = device_height * 0.7
        width = self.appium_driver.device_width() * 0.5
        return self.appium_driver.swipe(width, start_height, width, end_height, t)

    def find_els(self, els):
        for i in range(14):
            if self.appium_driver.element_displayed(self.get_object(els)):
                break
            else:
                self.swipe_up(1000)

    def element_click_util(self, els):
        for i in range(8):
            if self.appium_driver.element_displayed(self.get_object(els)):
                self.appium_driver.press_element(self.appium_driver.find_element(self.get_object(els)))
                break
            else:
                self.swipe_up(1000)
        return PlayerPage(self.appium_driver)

    def gift_click(self):
        return self.element_click_util("gift_id")

    def comment_click(self):
        return self.element_click_util("comment_id")

    def share_click(self):
        return self.element_click_util("share_id")

    def get_topic_name(self):
        self.find_els("topic_id")
        topic_name = self.appium_driver.find_element(self.get_object("topic_id")).text
        print("tocpic_name is %s" % topic_name)
        return topic_name

    def topic_click(self):
        self.find_els("topic_id")
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("topic_id")))
        return TopicDetailPage(self.appium_driver)

    def train_displayed(self):
        return self.appium_driver.element_displayed(self.get_object("train_id"))

    def go_to_train_userhome(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("train_id")))
        return LivePage(self.appium_driver)

    def go_to_ktv(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("train_id")))
        return MyTabCreateRoomPage(self.appium_driver)

    def get_train_username(self):
        user_name = self.appium_driver.find_element(self.get_object("train_id")).text
        return user_name

    def get_state_card(self):
        return self.appium_driver.find_element(self.get_object("train_card")).text

    def get_username(self):
        username = self.appium_driver.find_element(self.get_object("head_name")).text
        print("username is %s" % username)
        return username

    def photo_click(self):
        if self.head_ktv():
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("head_btn_id")))
            return MyTabCreateRoomPage(self.appium_driver)
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("head_btn_id")))
            return PersonPage(self.appium_driver)

    def dress_click(self):
        for i in range(10):
            if self.appium_driver.element_displayed(self.get_object("dress_id")):
                self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dress_id")))
                break
            else:
                self.swipe_up(1000)
        return DressPage(self.appium_driver)

    def has_open_member(self):
        return self.appium_driver.element_displayed(self.get_object("open_member"))

    def vip_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("vip")))

    def song_name_displayed(self):
        """
        判断首页全部歌曲songname是否存在
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("song_name"))

    def play_btn_click(self):
        """
        首页播放按钮点击
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_btn")))

    def work_click(self):
        """
        点击首页作品
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("work_id")))
        return PlayerPage(self.appium_driver)

    def get_song_name(self):
        """
        获取首页作品名字
        :return:
        """
        if self.song_name_displayed():
            return self.appium_driver.find_element(self.get_object("song_name")).text[
                   0:6], self.appium_driver.element_displayed(self.get_object("song_num"))
        else:
            self.play_btn_click()
            return self.appium_driver.find_element(self.get_object("song_name")).text[
                   0:6], self.appium_driver.element_displayed(self.get_object("song_num"))

    def work_play_num_displayed(self):
        if self.song_name_displayed():
            return self.appium_driver.find_element(self.get_object("song_name")).text[0:6]
        else:
            self.play_btn_click()
            return self.appium_driver.find_element(self.get_object("song_name")).text[0:6]

    def member_grade_displayed(self):
        """
        首页会员等级点击
        :return:
        """
        for i in range(10):
            if self.appium_driver.element_displayed(self.get_object("member_grade")):
                break
            else:
                self.swipe_up(1000)
        return self.appium_driver.element_displayed(self.get_object("member_grade"))

    def dynamic_comment_util(self, els):
        """
        动态评论点击
        :return:
        """
        for i in range(10):
            if self.appium_driver.element_displayed(self.get_object(els)):
                self.appium_driver.press_element(self.appium_driver.find_element(self.get_object(els)))
                break
            else:
                self.swipe_up(1000)
        return DynamicDetailsPage(self.appium_driver)

    def dynamic_comment_click(self):
        return self.dynamic_comment_util("dynamic_comment_id")

    def dynamic_user_content_click(self):
        """
        说点什么
        :return:
        """
        return self.dynamic_comment_util("dynamic_user_content")

    def dynamic_content_click(self):
        """
        动态评论内容点击
        :return:
        """
        return self.dynamic_comment_util("moment_content")

    def dynamic_image(self):
        """
        动态图片点击
        :return:
        """
        for i in range(10):
            if self.appium_driver.element_displayed(self.get_object("moment_image")):
                self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("moment_image")))
                break
            else:
                self.swipe_up(1000)

    def publish_preview(self):
        return self.appium_driver.element_displayed(self.get_object("publish_preview"))

    def moment_time(self):
        return self.appium_driver.element_displayed(self.get_object("moment_time"))

    def audiobg(self):
        for i in range(10):
            if self.appium_driver.element_displayed(self.get_object("audiobg")):
                break
            else:
                self.swipe_up(1000)
        return self.appium_driver.element_displayed(self.get_object("audiobg"))

    def moment_audio_play(self):
        for i in range(10):
            if self.appium_driver.element_displayed(self.get_object("moment_audio_play")):
                break
            else:
                self.swipe_up(1000)
        return self.appium_driver.element_displayed(self.get_object("moment_audio_play"))

    def head_ktv(self):
        return self.appium_driver.element_displayed(self.get_object("head_ktv"))
