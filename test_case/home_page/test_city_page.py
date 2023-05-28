#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.home_page.city_page import CityPage


class TestCityPage:
    def test_check_train_card_displayed(self, city_page: CityPage):
        """
        测试热门tab小火车是否显示,android 点击头像进到直播页或包房页
        :return:
        """
        # if AppiumDriver.get_platform() == PlatformSelector.IOS:
        #     assert city_page.train_card_displayed()
        # else:
        if city_page.train_displayed():
            card_type = city_page.get_state_card()
            if card_type == city_page.LIVE:
                username = city_page.get_train_username()[0:2]
                print("username%s" % username)
                live_page_obj = city_page.go_to_train_userhome()
                if live_page_obj.know_displayed():
                    live_page_obj.know_click()
                print("live name %s" % live_page_obj.get_live_page_name())
                assert username in live_page_obj.get_live_page_name()[0:2]
                live_page_obj.close_live()
            else:
                # ktv_page_obj = city_page.go_to_ktv()
                # assert ktv_page_obj.is_ktv_room()
                # ktv_page_obj.quit_ktv_room()
                pass

    def test_like_click(self, city_page: CityPage):
        """
        首页关注全部点赞
        :return:
        """
        zan = city_page.get_zan_num()
        print("zan is %s" % zan)
        city_page.zan_click()
        zan_after = city_page.get_zan_num()
        print("zan_after is %s" % zan_after)
        if zan == "点赞":
            assert zan_after == 1;
        elif zan_after == "点赞":
            assert zan == 1
        elif zan > zan_after:
            assert zan == zan_after + 1;
        else:
            assert zan == zan_after - 1;

    def test_gift_click(self, city_page: CityPage):
        """
        首页关注全部点击礼物进到播放页
        :return:
        """
        player_page_obj = city_page.gift_click()
        if player_page_obj.sendgift_window_display():
            player_page_obj.sendgift_window_click()
        assert player_page_obj.giftbox_display() is True

    def test_comment_click(self, city_page: CityPage):
        """
        首页关注作品评论点击
        :return:
        """
        assert city_page.comment_click().comment_window() is True

    def test_share_click(self, city_page: CityPage):
        """
        首页关注作品分享点击
        :return:
        """
        assert city_page.share_click().share_window() is True

    def test_head_click(self, city_page: CityPage):
        """
        首页关注作者头像点击
        :return:
        """
        if city_page.head_ktv():
            pass
        else:
            username_attention = city_page.get_username()
            username_person = city_page.photo_click().get_username()
            assert username_attention in username_person

    def test_topic_click(self, city_page: CityPage):
        """
        首页全部话题点击
        :param attention_all_page:
        :return:
        """
        attention_topic_name = city_page.get_topic_name()
        print("attention_topic_name is %s" % attention_topic_name)
        topic_page_name = city_page.topic_click().get_topic_name()
        print("topic_page_name is %s" % topic_page_name)
        assert attention_topic_name in topic_page_name

    def test_work_click(self, city_page: CityPage):
        """
        点击作品进到播放页
        :param attention_all_page:
        :return:
        """
        song_name, song_num = city_page.get_song_name()
        print("song_name is %s" % song_name)
        print("song_num is %s" % song_num)
        assert song_num is True
        player_page_songname = city_page.work_click().song_name()
        print("player_page_songname is %s" % player_page_songname)
        assert song_name in player_page_songname
        assert song_num is True

    def test_member_grade_click(self, city_page: CityPage):
        """
        会员等级存在
        :param attention_all_page:
        :return:
        """
        assert city_page.member_grade_displayed() is True


if __name__ == "__main__":
    pytest.main(["-s", "test_city_page.py"])
