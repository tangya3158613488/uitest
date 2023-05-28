import pytest

from page.home_page.hot_page import HomePage

"""
check 

4. 断言进入全局播放页
"""


class TestHomePage:

    def test_goto_global_player_page(self, home_page: HomePage):
        """
        进入全局播放页
        :return:
        """
        global_player_page_obj = home_page.global_player_btn_click()
        assert global_player_page_obj.in_gloabl_play_page()

    def test_goto_rank_page(self, home_page: HomePage):
        """
        进入榜单页
        :return:
        """
        rank_page_obj = home_page.click_rank_btn()
        assert rank_page_obj.in_rank_page()

    def test_goto_home_search_page(self, home_page: HomePage):
        """
        进入首页搜索
        :return:
        """
        home_search_page_obj = home_page.click_search_btn()
        assert home_search_page_obj.in_home_search_song_page()


if __name__ == "__main__":
    pytest.main(["-s", "test_home_page.py"])
