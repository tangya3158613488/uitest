import pytest

from page.home_page.home_search_page.home_search_page import HomeSearchPage
from page.webview_page.webview_page import WebViewPage

"""

"""


class TestHomeSearchPage:

    def test_hum_song_page(self, home_search_page: HomeSearchPage):
        """
        点击哼唱搜搜弹出哼唱弹窗
        :return:
        """
        home_search_page_obj = home_search_page.click_hum_song_btn()
        assert home_search_page_obj.hum_song_window_displayed()

    def test_click_hot_search_jump(self, home_search_page: HomeSearchPage):
        """
        check 显示热搜词，点击热搜词可以跳转到h5或者搜索结果页
        :return:
        """
        home_search_page_obj = home_search_page.click_hot_search_tab()
        assert home_search_page_obj.get_hot_search_word_list_len() > 0
        home_search_result_page_obj = home_search_page.click_hot_search_word(index=0)
        web_view_page_obj = WebViewPage(home_search_page.appium_driver)
        is_home_search_result_page = home_search_result_page_obj.in_home_search_result_page()
        if not is_home_search_result_page:
            assert web_view_page_obj.in_web_view_page()

    def test_click_hot_activity_jump(self, home_search_page: HomeSearchPage):
        """
        check 显示精彩活动，点击热门精彩活动转到h5页
        :return:
        """
        home_search_page_obj = home_search_page.click_hot_activity_tab()
        assert home_search_page_obj.get_hot_activity_list_len() > 0
        web_view_page_obj = home_search_page.click_hot_activity_cell(index=0)
        assert web_view_page_obj.in_web_view_page()

    def test_click_hot_activity_more_btn_jump(self, home_search_page: HomeSearchPage):
        """
        check 点击热门精彩活动查看更多跳转精彩活动页面
        :return:
        """
        home_search_page_obj = home_search_page.click_hot_activity_tab()
        web_view_page_obj = home_search_page_obj.click_hot_activity_more()
        assert web_view_page_obj.in_web_view_page()

    def test_click_topic_jump(self, home_search_page: HomeSearchPage):
        """
        check 显示热门话题，点击热门话题进入话题详情页
        :return:
        """
        home_search_page_obj = home_search_page.click_hot_topic_tab()
        assert home_search_page_obj.get_hot_topic_list_len() > 0
        topic_detail_page_obj = home_search_page.click_hot_topic_cell(index=2)
        assert topic_detail_page_obj.in_topic_detail_page()

    def test_click_more_topic_jump(self, home_search_page: HomeSearchPage):
        """
        check 热门话题tab点击更多进入话题广场
        :return:
        """
        home_search_page_obj = home_search_page.click_hot_topic_tab()
        assert home_search_page_obj.get_hot_topic_list_len() > 0
        topic_square_page_obj = home_search_page.click_hot_topic_more()
        assert topic_square_page_obj.topic_square_page_displayed()

    def test_show_recommend(self, home_search_page: HomeSearchPage):
        """
        check 搜索页是否显示推荐
        :return:
        """
        home_search_page_obj = home_search_page.swipe_down()
        assert home_search_page_obj.recommend_title_displayed()

    def test_search_song(self, home_search_page: HomeSearchPage):
        """
        check 搜素歌曲进入搜素结果页
        :return:
        """
        home_search_result_page_obj = home_search_page.search_song_by_keyword(keyword="告白气球")
        assert home_search_result_page_obj.in_home_search_result_page()

    def test_search_history_jump(self, home_search_page: HomeSearchPage):
        """
        check 点击搜索历史可以跳转
        :return:
        """
        if not home_search_page.search_history_displayed():
            home_search_result_page_obj = home_search_page.search_song_by_keyword(keyword="告白气球")
            assert home_search_result_page_obj.in_home_search_result_page()
            home_search_result_page_obj.click_clear_text_btn()
            assert home_search_page.in_home_search_song_page()
            assert home_search_page.search_history_displayed()
        home_search_result_page_obj = home_search_page.click_search_history()
        assert home_search_result_page_obj.in_home_search_result_page()


if __name__ == "__main__":
    pytest.main(["-s", "test_home_search_page.py"])
