#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from page.home_page.attention_page.attention_work_page import AttentionWorkPage


class TestAttentionWorkPage:
    def test_like_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作品点赞
        :return:
        """
        zan = attention_work_page.get_zan_num()
        attention_work_page.zan_click()
        zan_after = attention_work_page.get_zan_num()
        if zan == "点赞":
            assert zan_after == 1;
        elif zan_after == "点赞":
            assert zan == 1
        elif zan > zan_after:
            assert zan == zan_after + 1;
        else:
            assert zan == zan_after - 1;

    def test_gift_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作品点击礼物进到播放页
        :return:
        """
        player_page_obj = attention_work_page.gift_click()
        if player_page_obj.sendgift_window_display():
            player_page_obj.sendgift_window_click()
        assert player_page_obj.giftbox_display() is True

    def test_comment_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作品评论点击
        :return:
        """
        assert attention_work_page.comment_click().comment_window() is True

    def test_share_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作品分享点击
        :return:
        """
        assert attention_work_page.share_click().share_window() is True

    def test_head_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作者头像点击
        :return:
        """
        username_attention = attention_work_page.get_username()
        username_person = attention_work_page.photo_click().get_username()
        assert username_attention in username_person

    def test_topic_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作品话题点击
        :param attention_all_page:
        :return:
        """
        attention_topic_name = attention_work_page.get_topic_name()
        print("attention_topic_name is %s" % attention_topic_name)
        topic_page_name = attention_work_page.topic_click().get_topic_name()
        print("topic_page_name is %s" % topic_page_name)
        assert attention_topic_name in topic_page_name

    def test_work_click(self, attention_work_page: AttentionWorkPage):
        """
        点击作品进到播放页
        :param attention_all_page:
        :return:
        """
        song_name, song_num = attention_work_page.get_song_name()
        print("song_name is %s" % song_name)
        print("song_name is %s" % song_num)
        assert song_num is True
        player_page_songname = attention_work_page.work_click().song_name()
        print("player_page_songname is %s" % player_page_songname)
        assert song_name in player_page_songname
        assert song_num is True

    def test_dress_click(self, attention_work_page: AttentionWorkPage):
        """
        首页关注作者装扮点击
        :return:
        """
        dress_obj = attention_work_page.dress_click()
        try:
            result = dress_obj.title() == dress_obj.assert_title
        except:
            result = attention_work_page.has_open_member()
        print("result is %s" % result)
        assert result is True


    def test_member_grade_click(self, attention_work_page: AttentionWorkPage):
        """
        会员等级存在
        :param attention_all_page:
        :return:
        """
        assert attention_work_page.member_grade_displayed() is True


if __name__ == "__main__":
    pytest.main(["-s", "test_attention_work_page.py"])
