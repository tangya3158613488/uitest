import pytest

from page.sing_page.search_page.search_page import SearchPage
from page.sing_page.sing_page import SingPage
from page.sing_page.search_page import search_page_objects


class TestSearchResultPage:

    def test_normal_acc_page_show(self, sing_page: SingPage, search_page: SearchPage):
        """
        搜索正常歌曲 页面展示元素：伴奏tab、合唱tab、立即反馈按钮btn
        :return:
        """
        search_result_page_obj = search_page.search_song_by_keyword(search_page_objects.normal_acc)
        assert search_result_page_obj.acc_tab_displayed() is True
        assert search_result_page_obj.chorus_tab_displayed() is True
        assert search_result_page_obj.feedback_now_btn_displayed() is True

    def test_illegal_acc_page_show(self, sing_page: SingPage, search_page: SearchPage):
        """
        搜索违规词、违禁词伴奏页面展示元素：
        :return:
        """
        search_result_page_obj = search_page.search_song_by_keyword(search_page_objects.illegal_acc)
        assert search_result_page_obj.acc_tab_displayed() is True
        assert search_result_page_obj.chorus_tab_displayed() is True
        assert search_result_page_obj.illegal_acc_page_show() is True

    def test_no_result_acc_page_show(self, sing_page: SingPage, search_page: SearchPage):
        """
        搜索无结果伴奏页面展示元素：
        :return:
        """
        search_result_page_obj = search_page.search_song_by_keyword(search_page_objects.no_result_acc)
        assert search_result_page_obj.acc_tab_displayed() is True
        assert search_result_page_obj.chorus_tab_displayed() is True
        assert search_result_page_obj.no_result_acc_page_show() is True

    def test_click_feefback_now(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击立即反馈按钮
        :return:
        """
        search_result_page_obj = search_page.search_song_by_keyword(search_page_objects.normal_acc)
        assert search_result_page_obj.click_feedback_now_btn().page_title_displayed() is True

    def test_click_all_version(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击全部版本
        """
        search_result_page_obj = search_page.search_song_by_keyword(search_page_objects.normal_acc)
        assert search_result_page_obj.click_more_version_btn().click_view_all_version_btn().page_title_displayed() is True

    def test_click_chrous_tab(self, sing_page: SingPage, search_page: SearchPage):
        """
        点击合唱tab
        :return:
        """
        chrous_tab_obj = search_page.search_song_by_keyword(search_page_objects.normal_acc).click_chrous_tab()
        assert chrous_tab_obj.only_show_video_chrous_txt_display()


if __name__ == "__main__":
    pytest.main(["-s", "test_search_result_page.py"])
