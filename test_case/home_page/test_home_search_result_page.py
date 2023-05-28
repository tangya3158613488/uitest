from time import sleep

import pytest

from page.home_page.home_search_page.home_search_result_page import HomeSearchResultPage

"""
测试搜索结果页
"""

search_data = {"comprehensive": [{"keyword": "关爱模式", "expected": "关爱模式"}],
               "song": [{"keyword": "简单爱", "expected": "简单爱"}, {"keyword": "告白气球", "expected": "告白气球"}],
               "group": [{"keyword": "吃饭测试群", "expected": "吃饭测试群"}],
               "user": [{"keyword": "xiaofan772", "expected": "xiaofan772"}],
               "duet": [{"keyword": "简单爱", "expected": "简单爱"}, {"keyword": "告白气球", "expected": "告白气球"}]}


class TestHomeSearchResultPage:

    # @pytest.mark.parametrize("home_search_result_page", search_data["comprehensive"], indirect=True)
    # def test_search_comprehensive(self, home_search_result_page: HomeSearchResultPage):
    #     """
    #     check 搜素歌曲进入搜素结果页
    #     :return:
    #     """
    #     home_search_result_page, param = home_search_result_page
    #     home_search_result_page.click_comprehensive_search_tab()
    #     sleep(5)
    #     print(home_search_result_page.appium_driver.get_page_source())

    # @pytest.mark.parametrize("home_search_result_page", search_data["song"], indirect=True)
    # def test_search_song(self, home_search_result_page: HomeSearchResultPage):
    #     """
    #     check 搜索歌曲进入搜素结果页
    #     :return:
    #     """
    #     home_search_result_page, param = home_search_result_page
    #     home_search_result_page.click_accompaniment_search_tab()
    #     sleep(5)
    #     print(home_search_result_page.appium_driver.get_page_source())

    # @pytest.mark.parametrize("home_search_result_page", search_data["group"], indirect=True)
    # def test_search_group(self, home_search_result_page: HomeSearchResultPage):
    #     """
    #     check 搜索群组
    #     :return:
    #     """
    #     home_search_result_page, param = home_search_result_page
    #     home_search_result_page.click_group_search_tab()
    #     sleep(5)
    #     print(home_search_result_page.appium_driver.get_page_source())

    @pytest.mark.parametrize("home_search_result_page", search_data["user"], indirect=True)
    def test_search_user(self, home_search_result_page: HomeSearchResultPage):
        """
        check 搜索用户，第一条和预期结果一致
        :return:
        """
        home_search_result_page, param = home_search_result_page
        home_search_result_page.click_user_search_tab()
        nickname = home_search_result_page.get_user_nickname()
        assert nickname == param["expected"]

    @pytest.mark.parametrize("home_search_result_page", search_data["duet"], indirect=True)
    def test_search_duet(self, home_search_result_page: HomeSearchResultPage):
        """
        check 搜索合唱，第一条和预期结果一致
        :return:
        """
        home_search_result_page, param = home_search_result_page
        home_search_result_page.click_duet_search_tab()
        duet_song_name = home_search_result_page.get_duet_song_name()
        print(duet_song_name)
        assert duet_song_name == param["expected"]


if __name__ == "__main__":
    pytest.main(["-s", "test_home_search_result_page.py"])
