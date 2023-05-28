#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.home_page.attention_page.attention_all_page import AttentionAllPage


class TestAttentionPage:
    def test_go_to_release_dynamic(self, attention_all_page: AttentionAllPage):
        """
        首页关注进到发动态页面
        ios 不能直接获取title
        :return:
        """
        publish_dynamic_page_obj = attention_all_page.publish_dynamic_click()
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            assert publish_dynamic_page_obj.in_public_dynamic_page()
        else:
            assert publish_dynamic_page_obj.title() == publish_dynamic_page_obj.assert_title
        publish_dynamic_page_obj.cancel_publish_dynamic()

    def test_like_click(self, attention_all_page: AttentionAllPage):
        """
        首页关注全部点赞
        :return:
        """
        zan = attention_all_page.get_zan_num()
        attention_all_page.zan_click()
        zan_after = attention_all_page.get_zan_num()
        if zan == "点赞":
            assert zan_after == 1;
        elif zan_after == "点赞":
            assert zan == 1
        elif zan > zan_after:
            assert zan == zan_after + 1;
        else:
            assert zan == zan_after - 1;

    def test_gift_click(self, attention_all_page: AttentionAllPage):
        """
        首页关注全部点击礼物进到播放页
        :return:
        """
        player_page_obj = attention_all_page.gift_click()
        if player_page_obj.sendgift_window_display():
            player_page_obj.sendgift_window_click()
        assert player_page_obj.giftbox_display() is True

    def test_go_to_live(self, attention_all_page: AttentionAllPage):
        """
        首页顶部小火车点击，ios定位不到单个小火车
        :return:
        """
        if attention_all_page.train_displayed():
            card_type = attention_all_page.get_state_card()
            if card_type == attention_all_page.LIVE:
                username = attention_all_page.get_train_username()[0:2]
                print("username%s" % username)
                live_page_obj = attention_all_page.go_to_train_userhome()
                if live_page_obj.know_displayed():
                    live_page_obj.know_click()
                print("live name %s" % live_page_obj.get_live_page_name())
                live_name = live_page_obj.get_live_page_name()[0:2]
                live_page_obj.close_live()
                assert username in live_name
            else:
                pass
                # ktv_page_obj = attention_all_page.go_to_ktv()
                # assert ktv_page_obj.is_ktv_room()
                # ktv_page_obj.quit_ktv_room()

    def test_comment_click(self, attention_all_page: AttentionAllPage):
        """
        首页关注作品评论点击
        :return:
        """
        assert attention_all_page.comment_click().comment_window() is True

    def test_share_click(self, attention_all_page: AttentionAllPage):
        """
        首页关注作品分享点击
        :return:
        """
        assert attention_all_page.share_click().share_window() is True

    def test_head_click(self, attention_all_page: AttentionAllPage):
        """
        首页关注作者头像点击
        :return:
        """
        username_attention = attention_all_page.get_username()
        username_person = attention_all_page.photo_click().get_username()
        assert username_attention in username_person

    def test_dress_click(self, attention_all_page: AttentionAllPage):
        """
        首页关注作者装扮点击
        :return:
        """
        dress_obj = attention_all_page.dress_click()
        try:
            result = dress_obj.title() == dress_obj.assert_title
        except:
            result = attention_all_page.has_open_member()
        print("result is %s" % result)
        assert result is True

    def test_recommend_user_click(self, attention_all_page: AttentionAllPage):
        """
        首页推荐用户头像点击
        :return:
        """
        recommend_username = attention_all_page.get_recommend_user_name()[0:6]
        print("recommend_user_name %s" % recommend_username)
        person_page_username = attention_all_page.recommend_user_click().get_username()
        print("person_page_username %s" % person_page_username)
        assert recommend_username in person_page_username

    def test_recommend_user_attention(self, attention_all_page: AttentionAllPage):
        """
        首页推荐用户关注点击
        :return:
        """
        if "关注" in attention_all_page.get_recommend_user_attention_status():
            attention_all_page.recommend_attention_click()
            attention_status = attention_all_page.get_recommend_user_attention_status()
            print("attention_status %s" % attention_status)
            person_attention_status = attention_all_page.recommend_user_click().get_attention_status()
            print("person_attention_status %s" % person_attention_status)
            assert "已关注" in attention_status and person_attention_status == " "

    def test_topic_click(self, attention_all_page: AttentionAllPage):
        """
        首页全部话题点击
        :param attention_all_page:
        :return:
        """
        attention_topic_name = attention_all_page.get_topic_name()
        print("attention_topic_name is %s" % attention_topic_name)
        if attention_topic_name == attention_all_page.chorus:
            song_name = attention_all_page.get_song_name()
            print("attention_song_name is %s" % song_name)
            singpage_song_name = attention_all_page.topic_click().get_topic_name()
            assert song_name in singpage_song_name
        else:
            topic_page_name = attention_all_page.topic_click().get_topic_name()
            print("topic_page_name is %s" % topic_page_name)
            assert attention_topic_name in topic_page_name

    def test_work_click(self, attention_all_page: AttentionAllPage):
        """
        点击作品进到播放页
        :param attention_all_page:
        :return:
        """
        song_name, song_num = attention_all_page.get_song_name()
        print("song_name is %s" % song_name)
        print("song_name is %s" % song_num)
        assert song_num is True
        player_page_songname = attention_all_page.work_click().song_name()
        print("player_page_songname is %s" % player_page_songname)
        assert song_name in player_page_songname
        assert song_num is True

    def test_member_grade_click(self, attention_all_page: AttentionAllPage):
        """
        会员等级存在
        :param attention_all_page:
        :return:
        """
        assert attention_all_page.member_grade_displayed() is True


if __name__ == "__main__":
    pytest.main(["-s", "test_attention_all_page.py"])
