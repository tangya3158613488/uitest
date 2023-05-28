#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from page.home_page.attention_page.attention_dynamic_page import AttentionDynamicPage


class TestAttentionDynamicPage:
    def test_like_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        首页关注动态点赞
        :return:
        """
        zan = attention_dynamic_page.get_dynamic_zan_num()
        attention_dynamic_page.dynamic_zan_click()
        zan_after = attention_dynamic_page.get_dynamic_zan_num()
        if zan == "点赞":
            assert zan_after == 1;
        elif zan_after == "点赞":
            assert zan == 1
        elif zan > zan_after:
            assert zan == zan_after + 1;
        else:
            assert zan == zan_after - 1;

    def test_head_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        首页关注动态作者头像点击
        :return:
        """
        username_attention = attention_dynamic_page.get_username()
        username_person = attention_dynamic_page.photo_click().get_username()
        assert username_attention in username_person

    # def test_topic_click(self, attention_dynamic_page: AttentionDynamicPage):
    #     """
    #     首页关注动态话题点击
    #     :param attention_all_page:
    #     :return:
    #     """
    #     attention_topic_name = attention_dynamic_page.get_topic_name()
    #     print("attention_topic_name is %s" % attention_topic_name)
    #     topic_page_name = attention_dynamic_page.topic_click().get_topic_name()
    #     print("topic_page_name is %s" % topic_page_name)
    #     assert attention_topic_name in topic_page_name

    def test_dress_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        首页关注动态作者装扮点击
        :return:
        """
        dress_obj = attention_dynamic_page.dress_click()
        try:
            result = dress_obj.title() == dress_obj.assert_title
        except:
            result = attention_dynamic_page.has_open_member()
        print("result is %s" % result)
        assert result is True

    def test_member_grade_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        会员等级存在
        :param attention_all_page:
        :return:
        """
        assert attention_dynamic_page.member_grade_displayed() is True

    def test_dynamic_comment(self, attention_dynamic_page: AttentionDynamicPage):
        """
        动态评论点击
        :param attention_dynamic_page:
        :return:
        """
        assert attention_dynamic_page.moment_time() is True
        assert attention_dynamic_page.dynamic_comment_click().dynamic_details_comment() is True

    def test_dynamic_user_content_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        动态说点什么点击
        :param attention_dynamic_page:
        :return:
        """
        assert attention_dynamic_page.dynamic_user_content_click().dynamic_details_comment_content() is True

    def test_dynamic_content_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        动态详情文字点击
        :param attention_dynamic_page:
        :return:
        """
        dynamic_details_obj = attention_dynamic_page.dynamic_content_click()
        assert dynamic_details_obj.getPageTitle() == dynamic_details_obj.assert_moment_details

    def test_dynamic_image_click(self, attention_dynamic_page: AttentionDynamicPage):
        """
        动态图片点击
        :param attention_dynamic_page:
        :return:
        """
        attention_dynamic_page.dynamic_image()
        assert attention_dynamic_page.publish_preview() is True

    def test_audiobg(self, attention_dynamic_page: AttentionDynamicPage):
        """
        动态语音条存在
        :param attention_dynamic_page:
        :return:
        """
        if attention_dynamic_page.audiobg():
            assert attention_dynamic_page.moment_audio_play() is True


if __name__ == "__main__":
    pytest.main(["-s", "test_attention_dynamic_page.py"])
