"""
群聊页
"""
import time

from page.message_page.message_group_chat_page import MessageGroupChatPage


class TestMessageGroupChatPage:
    def test_my_room_btn_click(self, message_group_chat_page: MessageGroupChatPage):
        """
          点击更多+号，点击我的房间
          :param message_group_chat_page:
          :return:
        """
        message_group_chat_page.add_more_btn_click()
        assert message_group_chat_page.add_more_btn_up()
        # time.sleep(2)
        message_group_chat_page.my_room_btn_click()
        # time.sleep(2)
        # print(message_group_chat_page.appium_driver.get_page_source())
        assert message_group_chat_page.my_room_ishow()

    def test_local_record_btn_click(self, message_group_chat_page: MessageGroupChatPage):
        """
          点击更多+号，点击本地录音
          :param message_group_chat_page:
          :return:
        """
        time.sleep(2)
        message_group_chat_page.add_more_btn_click()
        assert message_group_chat_page.add_more_btn_up()
        # time.sleep(2)
        camera_page = message_group_chat_page.local_record_btn_click()
        assert camera_page.in_my_local_record_page()

    def test_take_photo_btn_click(self, message_group_chat_page: MessageGroupChatPage):
        """
          点击更多+号，点击相机
          :param message_group_chat_page:
          :return:
        """
        time.sleep(2)
        message_group_chat_page.add_more_btn_click()
        assert message_group_chat_page.add_more_btn_up()
        camera_page = message_group_chat_page.take_photo_btn_click()
        assert camera_page.in_camera_page()

    def test_photo_album_btn_click(self, message_group_chat_page: MessageGroupChatPage):
        """
        点击+号-相册
        :return:
        """
        time.sleep(2)
        message_group_chat_page.add_more_btn_click()
        assert message_group_chat_page.add_more_btn_up()
        camera_roll_page = message_group_chat_page.photo_album_btn_click()
        assert camera_roll_page.in_camera_roll_page()

    def test_click_emoje_btn(self, message_group_chat_page: MessageGroupChatPage):
        """
        点击emoje按钮
        :param message_group_chat_page:
        :return:
        """
        time.sleep(1)
        message_group_chat_page.emoje_btn_click()
        time.sleep(2)
        assert message_group_chat_page.emoje_btn_up()

    def test_click_add_more_btn(self, message_group_chat_page: MessageGroupChatPage):
        """
        点击底部加号更多按钮
        :param message_group_chat_page:
        :return:
        """
        time.sleep(2)
        message_group_chat_page.add_more_btn_click()
        time.sleep(2)
        assert message_group_chat_page.add_more_btn_up()

    def test_click_voice_btn(self, message_group_chat_page: MessageGroupChatPage):
        """
        点击语音，长按发送语音，查看语音是否发送成功
        :param message_group_chat_page:
        :return:
        """
        time.sleep(1)
        message_group_chat_page.voice_btn_click()
        time.sleep(1)
        assert message_group_chat_page.voice_btn_work()
        message_group_chat_page.speak_btn_long_click_time()
        time.sleep(2)
        assert message_group_chat_page.speak_btn_voice_send()

    def test_click_true_words_btn(self, message_group_chat_page: MessageGroupChatPage):
        """
        点击更多-真心话-发送真心话
        :param message_group_chat_page:
        :return:
        """
        time.sleep(1)
        message_group_chat_page.add_more_btn_click()
        time.sleep(2)
        assert message_group_chat_page.add_more_btn_up()
        message_group_chat_page.true_words_btn_click()
        assert message_group_chat_page.true_words_btn_up()

