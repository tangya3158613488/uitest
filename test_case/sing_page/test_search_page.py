import pytest

from page.sing_page.search_page.search_page import SearchPage
from page.sing_page.sing_page import SingPage
from page.sing_page.search_page import search_page_objects


class TestSingHomeSearchPage:

    def test_page_show_element(self, sing_page: SingPage, search_page: SearchPage):
        """
        页面展示元素：需要先搜索下，才能确保有历史搜索title
        :return:
        """
        self.search_song_util(sing_page, search_page)
        assert search_page.history_title_displayed() is True
        assert search_page.hot_search_rank_title_displayed() is True

    def test_clear_history_search(self, sing_page: SingPage, search_page: SearchPage):
        """
        清除历史搜索
        :return:
        """
        if not search_page.history_title_displayed():
            self.search_song_util(sing_page, search_page)
        search_page.click_clear_history_search_btn().click_confirm_clear_history_btn()
        assert search_page.history_title_displayed() is False

    def test_click_more_btn(self, search_page: SearchPage):
        """
        点击更多按钮
        :return:
        """
        more_hot_search_rank_page_obj = search_page.click_hot_search_more_btn()
        assert more_hot_search_rank_page_obj.page_title_displayed() is True

    def test_click_hot_search_cell(self, search_page: SearchPage):
        """
        点击热搜榜下单个cell
        :return:
        """
        songlist_name = search_page.get_click_songlist_name()
        search_page.click_hot_search_cell()
        result_songlist_name = search_page.get_search_frame_song_name()
        assert (songlist_name == result_songlist_name) is True

    def test_click_best_acc_cell(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击搜索页-最佳伴奏cell
        :return:
        """
        search_page_song_name = search_page_objects.best_acc
        song_details_obj = search_page.click_best_acc_cell(search_page_objects.best_acc)
        song_details_page_song_name = song_details_obj.get_song_name()
        assert song_details_obj.judge_enter_page() is True
        assert (search_page_song_name in song_details_page_song_name) is True

    def test_click_best_acc_sing_btn(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击搜索页-最佳伴奏cell-演唱按钮
        :return:
        """
        search_page_song_name = search_page_objects.best_acc
        record_prepare_page_obj = search_page.click_best_acc_sing_btn(search_page_objects.best_acc)
        record_page_song_name = record_prepare_page_obj.get_song_name()
        assert record_prepare_page_obj.is_change_skin_btn_shown() is True
        assert (search_page_song_name in record_page_song_name) is True

    def test_click_song_associate_word_cell(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击搜索页-歌曲联想词cell
        :return:
        """
        song_associate_word_txt = search_page.get_associate_word_txt(search_page_objects.best_acc)
        search_result_page_obj = search_page.click_song_associate_word_cell(search_page_objects.best_acc)
        search_frame_word = search_result_page_obj.get_search_frame_word()
        search_page_song_name = search_result_page_obj.get_page_song_name()
        assert (song_associate_word_txt == search_frame_word) is True
        assert (search_page_song_name in song_associate_word_txt) is True

    def test_click_singer_associate_word_cell(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击搜索页-歌手联想词cell
        :return:
        """
        singer_associate_word_txt = search_page.get_associate_word_txt(search_page_objects.associate_singer)
        singer_details_page_obj = search_page.click_singer_associate_word_cell(search_page_objects.associate_singer)
        assert singer_details_page_obj.judge_enter_page() is True
        singer_details_page_singer_name = singer_details_page_obj.get_page_singer_name()
        assert (singer_associate_word_txt == singer_details_page_singer_name) is True

    def search_song_util(self, sing_page: SingPage, search_page: SearchPage):
        """
        搜索歌曲流程
        :param sing_page:
        :param search_page:
        :return:
        """
        search_page.search_song_by_keyword(search_page_objects.normal_acc).back_to_sing_page()
        sing_page.search_frame_click().close_input_frame()


if __name__ == "__main__":
    pytest.main(["-s", "test_singer_page.py"])
