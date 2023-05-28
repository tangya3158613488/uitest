#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
消息-私聊页
"""
from common.driver.appium_driver import AppiumDriver
from page.global_player_page.global_player_page import GlobalPlayerPage
from page.message_page.camera_roll_page import CameraRollPage
from page.objects_controller import ObjectsController
from page.public_page.camera_page import CameraPage
from page.record_page.my_local_record_page import MyLocalRecordPage



class MessagePrivateChatPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_message_private_page(self):
        """
        判断是否在私聊页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("voice_btn"))

    def more_btn_click(self):
        """
        更多按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn")))

    def voice_btn_click(self):
        """
        语音按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("voice_btn")))


    def emoje_btn_click(self):
        """
        表情包按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("emoji_btn")))


    def add_more_btn_click(self):
        """
        输入框更多点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("add_more_btn")))


    def global_player_btn_click(self):
        """
        全局播放器点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("global_player_btn")))

        return GlobalPlayerPage(self.appium_driver)

    def emoje_btn_up(self):
        """
        查看最近使用按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("recently_used_btn"))

    def add_more_btn_up(self):
        """
        查看相册按钮是否展示
        :return:
        """
        photo_album =  self.appium_driver.element_displayed(self.get_object("photo_album_btn"))
        take_photo =  self.appium_driver.element_displayed(self.get_object("take_photo_btn"))
        local_record =  self.appium_driver.element_displayed(self.get_object("local_record_btn"))
        my_production =  self.appium_driver.element_displayed(self.get_object("my_production_btn"))
        true_words =  self.appium_driver.element_displayed(self.get_object("true_words_btn"))
        my_room =  self.appium_driver.element_displayed(self.get_object("my_room_btn"))
        return photo_album and take_photo and local_record and my_production and true_words and my_room

    def voice_btn_work(self):
        """
        语音输入按钮是否起作用
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("speak_btn"))

    def speak_btn_long_click_time(self):
        """
        长按说话按钮4s
        :return:
        """
        self.appium_driver.long_press_element(self.appium_driver.find_element(self.get_object("speak_btn")), 4000)

    def speak_btn_voice_send(self):
        """
        查看页面是否有展示语音消息
        :return:
        """
        self.appium_driver.swipe_up(500)
        return self.appium_driver.element_displayed(self.get_object("send_voice"))

    def true_words_btn_click(self):
        """
        真心话点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("true_words_btn")))

    def true_words_btn_up(self):
        """
        真心话选项弹出
        :return:
        """
        common_question = self.appium_driver.element_displayed(self.get_object("common_question_btn"))
        # sensitive_question = self.appium_driver.element_displayed(self.get_object("sensitive_question_btn"))
        # custom_question = self.appium_driver.element_displayed(self.get_object("custom_question_btn"))
        return common_question

    def photo_album_btn_click(self):
        """
        点击更多+号~相册
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("photo_album_btn")))
        return CameraRollPage(self.appium_driver)

    def take_photo_btn_click(self):
        """
        点击更多+号，拍照
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("take_photo_btn")))
        return CameraPage(self.appium_driver)

    def local_record_btn_click(self):
        """
        点击更多+号，本地录音
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("local_record_btn")))
        return MyLocalRecordPage(self.appium_driver)

    def my_room_btn_click(self):
        """
        点击更多+号，我的房间
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_room_btn")))

    def my_room_ishow(self):
        """
        判断房间是否展示
        :return:
        """
        self.appium_driver.swipe_up(500)
        return self.appium_driver.element_displayed(self.get_object("my_room"))