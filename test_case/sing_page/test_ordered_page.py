import pytest

from page.sing_page.ordered_page.ordered_page import OrderedPage
from page.sing_page.sing_page import SingPage


class TestOrderedPage:

    def test_import_local_acc(self, ordered_page: OrderedPage):
        """
        导入本地伴奏
        :return:
        """
        local_acc_page_obj = ordered_page.click_import_acc_btn().click_import_local_acc()
        local_acc_page_song_name = local_acc_page_obj.get_song_name()

        record_prepare_page_obj = local_acc_page_obj.click_acc_el().click_sing_btn()
        record_page_song_name = record_prepare_page_obj.get_song_name()

        assert record_prepare_page_obj.is_change_skin_btn_shown() is True
        assert (local_acc_page_song_name == record_page_song_name) is True

    def test_click_acc_cell(self, sing_page: SingPage, ordered_page: OrderedPage):
        """
        点击伴奏cell热区
        :return:
        """
        ordered_page_acc_name = ordered_page.get_click_acc_cell_song_name()
        song_details_page = sing_page.song_cell_click()
        song_details_page_song_name = song_details_page.get_song_name()
        assert (ordered_page_acc_name == song_details_page_song_name) is True

    def test_click_sing_btn(self, ordered_page: OrderedPage):
        """
        点击演唱按钮
        :return:
        """
        ordered_page_acc_name = ordered_page.get_click_acc_cell_song_name()
        record_prepare_page_obj = ordered_page.click_acc_sing_btn()
        record_page_song_name = record_prepare_page_obj.get_song_name()

        assert record_prepare_page_obj.is_change_skin_btn_shown() is True
        assert (ordered_page_acc_name == record_page_song_name) is True


if __name__ == "__main__":
    pytest.main(["-s", "test_ordered_page.py"])
