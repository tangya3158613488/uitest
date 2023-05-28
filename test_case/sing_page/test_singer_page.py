import pytest

from page.sing_page.sing_page import SingPage
from page.sing_page.singer_page.singer_details_page import SingerDetailsPage
from page.sing_page.singer_page.singer_page import SingerPage


class TestSingerPage:

    def test_into_hot_singer_page(self, sing_page: SingPage):
        """
        进入热门歌手二级页面
        :return:
        """
        hot_singer_page_obj = sing_page.singer_btn_click().hot_see_more_btn_click()
        assert hot_singer_page_obj.page_title_displayed() is True

    def test_into_singer_details_page(self, singer_page: SingerPage):
        """
        进入歌手详情页
        :return:
        """
        singer_classify_page = singer_page.hot_see_more_btn_click()
        singer_classify_page_singer_name = singer_classify_page.get_single_cell_singer_name()
        singer_details_page = singer_classify_page.click_single_cell()
        assert singer_details_page.judge_enter_page() is True
        singer_details_page_singer_name = singer_details_page.get_page_singer_name()
        assert (singer_classify_page_singer_name == singer_details_page_singer_name) is True

    def test_click_acc_tab_cell(self, singer_details_page: SingerDetailsPage, singer_page: SingerPage):
        """
        点击伴奏tab下单个cell
        :return:
        """
        acc_tab_obj = singer_details_page.click_acc_tab()
        assert acc_tab_obj.judge_acc_tab_selected() is True
        singer_details_page_song_name = acc_tab_obj.get_acc_tab_song_name()
        song_details_page_obj = acc_tab_obj.click_acc_single_cell()
        song_details_page_song_name = song_details_page_obj.get_song_name()
        assert song_details_page_obj.judge_enter_page() is True
        assert (singer_details_page_song_name in song_details_page_song_name) is True

    def test_click_acc_tab_sing_btn(self, singer_details_page: SingerDetailsPage, singer_page: SingerPage):
        """
        点击伴奏tab下演唱按钮
        :return:
        """
        acc_tab_obj = singer_details_page.click_acc_tab()
        assert acc_tab_obj.judge_acc_tab_selected() is True
        singer_details_page_song_name = acc_tab_obj.get_acc_tab_song_name()
        record_prepare_page_obj = acc_tab_obj.click_acc_tab_sing_btn()
        record_prepare_page_song_name = record_prepare_page_obj.get_song_name()
        assert record_prepare_page_obj.is_change_skin_btn_shown() is True
        assert (singer_details_page_song_name == record_prepare_page_song_name) is True

    # 最近几个版本歌手详情页下面无作品tab
    # def test_click_work_tab_work_cell(self, singer_details_page: SingerDetailsPage, singer_page: SingerPage):
    #     """
    #     点击作品tab下作品cell
    #     :param singer_details_page:
    #     :param singer_page:
    #     :return:
    #     """
    #     work_tab_obj = singer_details_page.click_work_tab()
    #     play_page_obj = work_tab_obj.click_work_tab_work_cell()
    #     assert play_page_obj.details_tab() is True

    def test_click_chrous_tab_work_cell(self, singer_details_page: SingerDetailsPage, singer_page: SingerPage):
        """
        点击合唱tab下作品cell
        :param singer_details_page:
        :param singer_page:
        :return:
        """
        chrous_tab_obj = singer_details_page.click_chrous_tab()
        semi_chrous_player_page_obj = chrous_tab_obj.click_chrous_tab_work_cell()
        assert (semi_chrous_player_page_obj.friends_chrous_btn_displayed()
                or semi_chrous_player_page_obj.today_best_chrous_btn_displayed()
                or semi_chrous_player_page_obj.history_best_chrous_btn_displayed()) \
               and (semi_chrous_player_page_obj.join_chrous_btn_displayed()) is True


if __name__ == "__main__":
    pytest.main(["-s", "test_singer_page.py"])
