#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
私聊页
"""
import pytest
import time

from page.message_page.message_private_chat_page import MessagePrivateChatPage


class TestMessagePrivateChatPage:

    def test_my_room_btn_click(self, message_private_chat_page: MessagePrivateChatPage):
        """
          点击更多+号，点击我的房间
          :param message_private_chat_page:
          :return:
        """
        time.sleep(1)
        message_private_chat_page.add_more_btn_click()
        assert message_private_chat_page.add_more_btn_up()
        message_private_chat_page.my_room_btn_click()
        time.sleep(2)
        assert message_private_chat_page.my_room_ishow()

    def test_local_record_btn_click(self, message_private_chat_page: MessagePrivateChatPage):
        """
          点击更多+号，点击本地录音
          :param message_private_chat_page:
          :return:
        """
        time.sleep(1)
        message_private_chat_page.add_more_btn_click()
        assert message_private_chat_page.add_more_btn_up()
        camera_page = message_private_chat_page.local_record_btn_click()
        assert camera_page.in_my_local_record_page()

    def test_take_photo_btn_click(self, message_private_chat_page: MessagePrivateChatPage):
        """
          点击更多+号，点击相机
          :param message_private_chat_page:
          :return:
        """
        time.sleep(1)
        message_private_chat_page.add_more_btn_click()
        assert message_private_chat_page.add_more_btn_up()
        camera_page = message_private_chat_page.take_photo_btn_click()
        assert camera_page.in_camera_page()

    def test_photo_album_btn_click(self, message_private_chat_page: MessagePrivateChatPage):
        """
        点击+号-相册
        :return:
        """
        time.sleep(1)
        message_private_chat_page.add_more_btn_click()
        assert message_private_chat_page.add_more_btn_up()
        camera_roll_page = message_private_chat_page.photo_album_btn_click()
        assert camera_roll_page.in_camera_roll_page()

    def test_goto_global_player_page(self, message_private_chat_page: MessagePrivateChatPage):
        """
        进入全局播放页
        :return:
        """
        time.sleep(1)
        global_player_page_obj = message_private_chat_page.global_player_btn_click()
        assert global_player_page_obj.in_gloabl_play_page()

    def test_click_emoje_btn(self, message_private_chat_page: MessagePrivateChatPage):
        """
        点击emoje按钮
        :param message_private_chat_page:
        :return:
        """
        time.sleep(1)
        message_private_chat_page.emoje_btn_click()
        time.sleep(1)
        assert message_private_chat_page.emoje_btn_up()

    def test_click_add_more_btn(self, message_private_chat_page: MessagePrivateChatPage):
        """
        点击底部加号更多按钮
        :param message_private_chat_page:
        :return:
        """
        time.sleep(1)
        message_private_chat_page.add_more_btn_click()
        time.sleep(2)
        assert message_private_chat_page.add_more_btn_up()

    def test_click_voice_btn(self, message_private_chat_page: MessagePrivateChatPage):
        """
        点击语音，长按发送语音，查看语音是否发送成功
        :param message_private_chat_page:
        :return:
        """
        time.sleep(1)
        message_private_chat_page.voice_btn_click()
        time.sleep(1)
        assert message_private_chat_page.voice_btn_work()
        message_private_chat_page.speak_btn_long_click_time()
        time.sleep(1)
        assert message_private_chat_page.speak_btn_voice_send()

    def test_click_true_words_btn(self, message_private_chat_page: MessagePrivateChatPage):
        """
        点击更多-真心话-发送真心话
        :param message_private_chat_page:
        :return:
        """
        time.sleep(1)
        message_private_chat_page.add_more_btn_click()
        time.sleep(1)
        assert message_private_chat_page.add_more_btn_up()
        message_private_chat_page.true_words_btn_click()
        assert message_private_chat_page.true_words_btn_up()


if __name__ == '__main__':
    pytest.main(["-s", "test_message_private_chat_page.py"])
