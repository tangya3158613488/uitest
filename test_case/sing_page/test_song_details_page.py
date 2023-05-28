import re
from time import sleep

import pytest

from page.sing_page.sing_page import SingPage
from page.sing_page.song_details_page import SongDetailsPage


class TestSongDetailsPage:

    def test_click_page_tab(self, sing_page: SingPage, song_details_page: SongDetailsPage):
        """
        切换页面tab
        :return:
        """
        history_best_tab_obj = song_details_page.click_years_best_tab().click_history_best_tab()
        assert history_best_tab_obj.judge_history_best_tab_selected() is True

        years_best_tab_obj = song_details_page.click_history_best_tab().click_years_best_tab()
        assert years_best_tab_obj.judge_years_best_tab_selected() is True

        today_best_tab_obj = song_details_page.click_today_best_tab()
        assert today_best_tab_obj.judge_today_best_tab_selected() is True

        add_duet_tab_obj = song_details_page.click_add_duet_tab()
        assert add_duet_tab_obj.judge_add_duet_tab_selected() is True

    def test_click_singer_name(self, song_details_page: SongDetailsPage):
        """
        点击歌手名
        :param song_details_page:
        :return:
        """
        if song_details_page.judge_singer_name_is_clicked():
            song_details_page_singer_name = song_details_page.get_singer_name()
            singer_page_obj = song_details_page.click_singer_name()
            singer_page_singer_name = singer_page_obj.get_page_singer_name()
            assert (singer_page_singer_name in song_details_page_singer_name) is True

    def test_click_sing_btn(self, song_details_page: SongDetailsPage):
        """
        点击 我要演唱 按钮
        :return:
        """
        # 如果歌曲详情页歌曲名太长打点显示了，取前12个字。最多展示12个字
        details_page_song_name = song_details_page.get_song_name()
        if "..." in song_details_page.get_song_name():
            details_page_song_name = details_page_song_name[:12]
        record_prepare_page_obj = song_details_page.click_sing_btn()
        record_page_song_name = record_prepare_page_obj.get_song_name()
        details_page_song_name = re.sub('\s+', "", details_page_song_name)
        record_page_song_name = re.sub('\s+', "", record_page_song_name)
        assert record_prepare_page_obj.is_change_skin_btn_shown() is True
        assert (details_page_song_name in record_page_song_name) is True

    def test_click_first_classify(self, song_details_page: SongDetailsPage):
        """
        点击页面内第一个歌曲分类
        :return:
        """
        song_details_classify_name = song_details_page.get_first_classify()
        classify_detail_page_obj = song_details_page.click_first_classify()
        classify_page_title_name = classify_detail_page_obj.get_page_title()
        assert (song_details_classify_name == classify_page_title_name) is True

    def test_swipe_page_btn(self, song_details_page: SongDetailsPage):
        """
        滑动页面后按钮展示
        :return:
        """
        sleep(1)
        after_page_obj = song_details_page.swipe_page()
        assert (after_page_obj.swipe_after_sing_btn_displayed() and after_page_obj.judge_enter_page()) is True


if __name__ == "__main__":
    pytest.main(["-s", "test_song_details_page.py"])
