import time

import pytest

from page.global_player_page.global_player_listening_page import GlobalPlayerListeningPage
from page.global_player_page.global_player_my_page import GlobalPlayerMyPage
from page.global_player_page.global_player_page import GlobalPlayerPage
from page.player_page.player_page import PlayerPage
from page.public_page.navigationbar_page import NavigationBarPage

"""

"""


class TestGlobalPlayerPage:

    def test_play_and_pause(self, global_player_page: GlobalPlayerPage):
        """
        1、测试播放、暂停功能
        :param listening_page:
        :return:
        """
        global_player_page.switch_to_xiaochang_fm_tab().click_play_all_btn()
        assert not global_player_page.paused()
        # 暂停，看是否暂停成功
        global_player_page.click_play_btn()
        assert global_player_page.paused()

    def test_player_silder_displayed(self, global_player_page: GlobalPlayerPage):
        """
        2、测试播放进度条是否可点 you bug
        :param global_player_page:
        :return:
        """
        listening_obj = global_player_page.switch_to_listening_tab()
        if not listening_obj.empty_page():
            listening_obj.click_clear_btn()
            listening_obj.click_clear_sure_btn()
        assert not global_player_page.player_slider_displayed()

    def test_prev_and_next(self, global_player_page: GlobalPlayerPage):
        """
        3、测试上一首、下一首功能
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 1
        if xiaochang_fm_obj.work_playing_by_index(index):
            index = index + 1
        xiaochang_fm_obj.click_work_by_index(index)
        assert xiaochang_fm_obj.work_playing_by_index(index)
        assert not xiaochang_fm_obj.work_playing_by_index(index + 1)
        global_player_page.click_next_btn()
        assert not xiaochang_fm_obj.work_playing_by_index(index)
        assert xiaochang_fm_obj.work_playing_by_index(index + 1)
        global_player_page.click_prev_btn()
        assert xiaochang_fm_obj.work_playing_by_index(index)
        assert not xiaochang_fm_obj.work_playing_by_index(index + 1)

    def test_play_model_switch(self, global_player_page: GlobalPlayerPage):
        """
        4、测试单曲循环、列表循环,随机播放
        :param global_player_page:
        :return:
        """
        play_model_list = ["循环", "单曲循环", "随机"]
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 0
        if not xiaochang_fm_obj.work_playing_by_index(index):
            xiaochang_fm_obj.click_work_by_index(index)
        assert xiaochang_fm_obj.work_playing_by_index(index)
        play_model = global_player_page.get_play_model()
        play_model_index = play_model_list.index(play_model)
        print(play_model_index)
        for model_index in range(3):
            play_model = global_player_page.get_play_model()
            if play_model != play_model_list[2]:
                global_player_page.click_next_btn()
                index = index + 1
                assert xiaochang_fm_obj.work_playing_by_index(index)
            global_player_page.click_play_model()
            after_click_play_model = global_player_page.get_play_model()

            if play_model_index == len(play_model_list) - 1:
                play_model_index = 0
            else:
                play_model_index = play_model_index + 1
            print("after_click_play_model {} play_model_index {}".format(after_click_play_model, play_model_index))
            assert after_click_play_model == play_model_list[play_model_index]

    def test_collect_and_cancel_collect_listening_tab(self, global_player_page: GlobalPlayerPage):
        """
        5、测试收藏、取消收藏
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 1
        if xiaochang_fm_obj.work_playing_by_index(index):
            index = index + 1
        xiaochang_fm_obj.click_work_by_index(index)
        collected = global_player_page.pause_utils().collected()
        if collected:
            global_player_page.click_collect_btn()
            assert not global_player_page.pause_utils().collected()
        global_player_page.click_collect_btn()
        assert global_player_page.pause_utils().collected()
        # 取消收藏
        global_player_page.click_collect_btn()
        assert not global_player_page.pause_utils().collected()

    def test_remove_all_in_listeninng_tab(self, global_player_page: GlobalPlayerPage):
        """
        6、清空正在播放的列表
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        xiaochang_fm_obj.click_play_all_btn()
        listening_page_obj = global_player_page.switch_to_listening_tab().click_clear_btn()
        assert listening_page_obj.empty_page()

    def test_jump_to_xiaochang_fm_tab_from_listeninng_tab(self, global_player_page: GlobalPlayerPage):
        """
        7、点击进入小唱Fm
        :param global_player_page:
        :return:
        """

        listening_page_obj = global_player_page.switch_to_listening_tab()
        if not listening_page_obj.empty_page():
            listening_page_obj.click_clear_btn()
        listening_page_obj.click_xiaochang_btn()
        assert global_player_page.xiaochang_fm_tab_selected()

    def test_jump_to_playpage_from_xiaochang_fm_tab(self, global_player_page: GlobalPlayerPage):
        """
        8、点击两次进入播放页
        :param global_player_page:
        :return:
        """

        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 0
        if not xiaochang_fm_obj.work_playing_by_index(index):
            print("没播放点击有一次")
            xiaochang_fm_obj.click_work_by_index(index)
        print("在点一次")
        xiaochang_fm_obj.click_work_by_index(index)
        assert PlayerPage(xiaochang_fm_obj.appium_driver).in_player_page()

    def test_play_all_in_xiaochang_fm_tab(self, global_player_page: GlobalPlayerPage):
        """
        9、测试播放全部
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        xiaochang_fm_obj.click_play_all_btn()
        index = 0
        assert xiaochang_fm_obj.work_playing_by_index(index)

    def test_replace_fm_in_xiaochang_fm_tab(self, global_player_page: GlobalPlayerPage):
        """
        10、测试小唱FM换一批
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 1
        worknname = xiaochang_fm_obj.work_name_by_index(index)
        print(worknname)
        xiaochang_fm_obj.click_replace_all_btn()
        worknname_after_replace = xiaochang_fm_obj.work_name_by_index(index)
        print(worknname_after_replace)
        assert worknname != worknname_after_replace

    def test_play_all_in_my_tab(self, global_player_page: GlobalPlayerPage):
        """
        11、测试我的tab播放全部
        :param global_player_page:
        :return:
        """
        global_player_my_page_obj = global_player_page.switch_to_my_tab().click_play_all_btn()
        assert global_player_my_page_obj.work_playing_by_index(0)

    def test_jump_playlist_page_in_my_tab(self, global_player_my_page: GlobalPlayerMyPage):
        """
        12、测试我的tab跳转歌单
        :param global_player_my_page:
        :return:
        """
        assert global_player_my_page.click_my_playlist_entrance().in_my_playlist_page()

    def test_my_collect_page_in_my_tab(self, global_player_page: GlobalPlayerPage):
        """
        13、测试我的tab-收藏页面 取消收藏与收藏
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 0
        workcell = xiaochang_fm_obj.work_name_by_index(index)
        print(workcell)
        song_name = workcell.split(",")[-1]
        print(song_name)
        if not xiaochang_fm_obj.work_playing_by_index(index):
            xiaochang_fm_obj.click_work_by_index(index)
        collected = global_player_page.collected()
        if not collected:
            global_player_page.click_collect_btn()
        else:
            #  收藏了，先取消再收藏，让他到收藏列表第一位
            global_player_page.click_collect_btn().click_collect_btn().pause_utils()
        global_player_my_page_obj = global_player_page.switch_to_my_tab()
        my_collect_page_obj = global_player_my_page_obj.click_collect_entrance()
        assert my_collect_page_obj.in_my_collect_page()
        collected_song_name = my_collect_page_obj.get_songname_by_index(0)
        print(collected_song_name)
        NavigationBarPage(my_collect_page_obj.appium_driver).back_btn_click()
        # 取消收藏
        global_player_page.click_collect_btn()
        global_player_my_page_obj.click_collect_entrance()
        try:
            first_collect_song_name = my_collect_page_obj.get_songname_by_index(0)
        except Exception as e:
            print(e)
            # 找不到刚的数据
            first_collect_song_name = ""
        print("after_cancel_collect_song_name {}".format(first_collect_song_name))
        assert first_collect_song_name != collected_song_name

    def test_jump_play_history_page_and_play_in_my_tab(self, global_player_page: GlobalPlayerPage):
        """
        14、测试我的tab跳转到播放历史,显示最新的播放,进入播放页
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        index = 0
        workcell = xiaochang_fm_obj.work_name_by_index(index)
        print(workcell)
        song_name = workcell.split(",")[-1]
        print(song_name)
        if not xiaochang_fm_obj.work_playing_by_index(index):
            xiaochang_fm_obj.click_work_by_index(index)
        global_player_my_page_obj = global_player_page.switch_to_my_tab()
        player_history_page_obj = global_player_my_page_obj.click_player_history_entrance()
        assert player_history_page_obj.in_player_history_page()
        first_song_name = player_history_page_obj.get_songname_by_index(index)
        print(first_song_name)
        assert song_name == first_song_name
        assert player_history_page_obj.click_workcell_by_index(index).in_player_page()

    def test_del_play_history_page_in_my_tab(self, global_player_page: GlobalPlayerPage):
        """
        15、测试清空播放历史
        :param global_player_page:
        :return:
        """
        xiaochang_fm_obj = global_player_page.switch_to_xiaochang_fm_tab()
        xiaochang_fm_obj.click_play_all_btn()
        global_player_my_page_obj = global_player_page.switch_to_my_tab()
        player_history_page_obj = global_player_my_page_obj.click_player_history_entrance()
        assert player_history_page_obj.in_player_history_page()

        player_history_page_obj.click_clean_btn().click_delete_btn()
        assert player_history_page_obj.empty_page()


if __name__ == "__main__":
    pytest.main(["-s", "test_global_player_page.py"])
