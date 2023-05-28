import time

import pytest

from page.home_page.home_search_page.home_search_page import HomeSearchPage
from page.home_page.hot_page import HotPage


class TestPlayerPage:
    def test_i_want_sing_displayed(self, home_search_page: HomeSearchPage):
        """
        我要唱icon可见
        :return:
        """
        assert home_search_page.in_home_search_song_page()
        home_search_result_obj = home_search_page.search_song_by_keyword(keyword="清唱")
        # home_search_result_obj.click_work_search_tab()
        i_want_sing_obj = home_search_result_obj.click_search_work_card()
        assert i_want_sing_obj.i_want_sing_displayed() is True

    def test_i_want_sing_goto_cantata_displayed(self, home_search_page: HomeSearchPage):
        """
        播放页点击"我要唱"进入清唱录制页
        :return:
        """
        assert home_search_page.in_home_search_song_page()
        home_search_result_obj = home_search_page.search_song_by_keyword(keyword="清唱")
        # home_search_result_obj.click_work_search_tab()
        i_want_sing_obj = home_search_result_obj.click_search_work_card()
        assert i_want_sing_obj.i_want_sing_displayed() is True
        i_want_sing_obj.i_want_sing_btn_click()
        assert i_want_sing_obj.cantata_title_displayed() is True

    def test_goto_work_play_page(self, hot_page: HotPage):
        """
        进入播放页
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        assert work_play_page_obj.details_tab() is True

    def test_live_head_photo_displayed(self, hot_page: HotPage):
        """
        直播导流icon可见
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        assert work_play_page_obj.live_head_photo_displayed() is True or False

    def test_lyric_text_displayed(self, hot_page: HotPage):
        """
        播放页歌词可见
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        assert work_play_page_obj.lyric_text_displayed() is True

    def test_export_song_displayed(self, hot_page: HotPage):
        """
        导出歌曲 按钮 可见
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        assert more_page_obj.export_song_displayed()

    def test_export_mp3_opening_member(self, hot_page: HotPage):
        """
        导出mp3歌曲充值会员
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        more_page_obj.export_song_btn_click()
        assert more_page_obj.export_mp3_btn_displayed()
        more_page_obj.export_mp3_btn_click()

        # assert more_page_obj.renewal_btn_displayed()
        # more_page_obj.renewal_btn_click()
        assert more_page_obj.opening_member_btn_displayed()

    def test_export_mp4_opening_member(self, hot_page: HotPage):
        """
        导出mp4歌曲充值会员
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        more_page_obj.export_song_btn_click()
        assert more_page_obj.export_mp4_btn_displayed()
        more_page_obj.export_mp4_btn_click()
        # assert more_page_obj.renewal_btn_displayed()
        # more_page_obj.renewal_btn_click()
        assert more_page_obj.opening_member_btn_displayed()

    def test_goto_my_export_record(self, hot_page: HotPage):
        """
        进入我的导出记录列表页面
        :param hot_page:
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        more_page_obj.export_song_btn_click()
        assert more_page_obj.my_export_record_btn_displayed()
        more_page_obj.my_export_record_btn_click()
        assert more_page_obj.my_export_record_title_displayed()

    def test_goto_song_home(self, hot_page: HotPage):
        """
        进入歌曲主页
        :param hot_page:
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        if more_page_obj.view_song_home_displayed() is True:
            more_page_obj.view_song_home_click()
            assert more_page_obj.singing_btn_displayed()
        else:
            assert more_page_obj.my_barrage_btn()

    def test_includ_song_list(self, hot_page: HotPage):
        """
        收录歌曲至我的歌单
        :param hot_page:
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        assert more_page_obj.includ_playlist_btn_displayed()
        more_page_obj.includ_playlist_btn_click()
        assert more_page_obj.my_song_list_displayed()
        assert more_page_obj.my_song_list_click()

    def test_guest_average_user_set_ringing(self, hot_page: HotPage):
        """
        客态非会员设置振铃
        :param hot_page:
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        assert more_page_obj.set_ringing_btn_displayed()
        more_page_obj.set_ringing_btn_click()
        if more_page_obj.renewal_btn_displayed():
            more_page_obj.renewal_btn_click()
            assert more_page_obj.opening_member_btn_displayed()
        elif more_page_obj.opening_member_btn_displayed():
            more_page_obj.opening_member_btn_click()
            assert more_page_obj.opening_member_btn_displayed()
        else:
            assert more_page_obj.get_android_toast() == "由于作者设置，当前作品暂不支持导出"

    def test_skip_prelude(self, hot_page: HotPage):
        """
        自动跳过前奏
        :param hot_page:
        :return:
        """
        work_play_page_obj = hot_page.work_card_click()
        more_page_obj = work_play_page_obj.more_btn_click()
        if more_page_obj.skip_prelude_btn_displayed():
            more_page_obj.skip_prelude_btn_click()
            more_page_obj = work_play_page_obj.more_btn_click()
            assert more_page_obj.cancel_skip_prelude_btn_displayed()

        elif more_page_obj.cancel_skip_prelude_btn_displayed():
            more_page_obj.cancel_skip_prelude_btn_click()
            more_page_obj = work_play_page_obj.more_btn_click()
            assert more_page_obj.skip_prelude_btn_displayed()


if __name__ == "__main__":
    pytest.main(["-s", "test_player_page.py"])
