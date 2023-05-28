import time

import pytest

from page.sing_page.search_page import search_page_objects
from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.sing_page.sing_page import SingPage
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage


class TestSingPage:

    def test_into_task_center(self, sing_page: SingPage):
        """
        进入任务中心二级页面
        :return:
        """
        task_center_page_obj = sing_page.task_center_click()
        assert task_center_page_obj.page_title_displayed() is True

    def test_search_song_by_keyword(self, sing_page: SingPage):
        """
        通过输入歌曲名搜索歌曲
        todo ios获取不到歌曲名
        :param sing_page:
        :return:
        """
        search_page_obj = sing_page.search_frame_click()
        assert search_page_obj.search_song_by_keyword(
            search_page_objects.normal_acc).judge_search_result_by_keyword() is True

    # def test_direct_search_song(self, sing_page: SingPage):
    #     """
    #     通过直接点击搜索按钮搜索歌曲名
    #     :return:
    #     todo
    #     """
    #     search_page_obj = sing_page.search_frame_click()
    #     except_song_name = search_page_obj.get_search_frame_song_name()
    #     search_result_page_song_name = search_page_obj.direct_search_song().get_search_result_by_redirt()
    #     assert (except_song_name == search_result_page_song_name) is True

    def test_recog_hum_song(self, sing_page: SingPage):
        """
        识别哼唱歌曲
        :param sing_page:
        :return:
        """
        sing_page.hum_song_btn_click().start_hum_song_btn_click()
        assert sing_page.give_up_recog_displayed() or sing_page.re_recog_btn_displayed() is True
        # hum_song_pop_obj.close_recog_hum_song_pop()

    def test_small_train_cell_click(self, sing_page_need_into_ktv: SingPage):
        """
        点击小火车cell进入包房
        todo ios找不到小火车
        :param sing_page:
        :return:
        """
        live_room_obj = sing_page_need_into_ktv.small_train_cell_click()
        while not live_room_obj.more_btn_displayed():
            sing_page_need_into_ktv.back_btn_click()
        # if live_room_obj.refuse_btn_displayed():
        #     live_room_obj.refuse_btn_click()
        live_room_obj.close_btn_click().quit_room_btn_click()

    def test_into_grab_sing_page(self, sing_page: SingPage):
        """
        进入劲爆抢唱二级页面
        :param sing_page:
        :return:
        """
        grab_sing_page_obj = sing_page.grab_sing_icon_click()
        # if grab_sing_page_obj.new_user_guide_displayed():
        #     grab_sing_page_obj.click_new_user_guide()
        live = sing_page.binded_tel_open_live_room_icon_click()
        if grab_sing_page_obj.stop_match_btn() is True:
            grab_sing_page_obj.click_stop_match_btn()
        # grab_sing_page_obj.click_back_image()

    def test_into_real_time_chrous_page(self, sing_page: SingPage):
        """
        进入实时合唱二级页面
        :param sing_page:
        :return:
        """
        real_time_chrous_page_obj = sing_page.real_time_chrous_icon_click()
        assert real_time_chrous_page_obj.page_title_displayed() is True

    def test_into_ordered_page(self, sing_page: SingPage):
        """
        进入已点二级页面
        :param sing_page:
        :return:
        """
        ordered_page_obj = sing_page.ordered_btn_click()
        assert ordered_page_obj.page_title_displayed() is True

    def test_into_singer_page(self, sing_page: SingPage):
        """
        进入歌手二级页面
        :param sing_page:
        :return:
        """
        singer_page_obj = sing_page.singer_btn_click()
        assert singer_page_obj.page_title_displayed() is True

    def test_into_classify_page(self, sing_page: SingPage):
        """
        进入分类二级页面
        :param sing_page:
        :return:
        """
        classify_page_obj = sing_page.classify_btn_click()
        assert classify_page_obj.page_title_displayed() is True

    def test_into_mall_page(self, sing_page: SingPage):
        """
        进入商城二级页面
        :param sing_page:
        :return:
        """
        mall_page_obj = sing_page.mall_btn_click()
        assert mall_page_obj.page_title_displayed() is True

    def test_open_live_room_icon_click(self, sing_page: SingPage):
        """
        开歌房icon点击：点击开歌房icon，如果绑定手机号title没有出现，走直接进包房逻辑，否则证明进入到绑定手机号页面，该条case通过。
        :return:
        """
        bind_tel_page_obj = sing_page.open_live_room_icon_click()
        if not bind_tel_page_obj.page_title_displayed():
            sing_page.binded_tel_open_live_room_icon_click().close_btn_click().quit_room_btn_click()

    def test_into_only_sing_page(self, sing_page: SingPage):
        """
        进入清唱二级页面
        :param sing_page:
        :return:
        """
        only_sing_page_obj = sing_page.only_sing_icon_click()
        assert only_sing_page_obj.page_title_displayed() is True

    def test_into_import_page(self, sing_page: SingPage):
        """
        进入导入音视频二级页面
        :param sing_page:
        :return:
        """
        import_page_obj = sing_page.import_icon_click()
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            import_page_obj = sing_page.import_local_video_click()
        assert import_page_obj.page_title_displayed() is True

    def test_live_room_sing_icon_click(self, sing_page: SingPage):
        """
        直播唱icon点击：点击直播唱icon，如果主播实名认证title没有出现，走直接进直播准备页逻辑，否则证明进入到主播实名认证页面，该条case通过。
        :return:
        """
        real_time_page_obj = sing_page.real_name_live_room_sing_icon_click()
        if not real_time_page_obj.page_title_displayed():
            assert sing_page.live_room_sing_icon_click().select_background_txt_displayed() is True

    def test_into_drifting_bottle_page(self, sing_page: SingPage):
        """
        进入漂流瓶二级页面
        :param sing_page:
        :return:
        """
        drifting_bottle_page_obj = sing_page.drifting_bottle_icon_click()
        assert drifting_bottle_page_obj.page_title_displayed() is True

    # 到这儿了
    # def test_into_meet_by_sounds_page(self, sing_page: SingPage):
    #     """
    #     进入以声相遇二级页面
    #     :param sing_page:
    #     :return:
    #     """
    #     meet_by_sounds_page_obj = sing_page.meet_by_sounds_icon_click()
    #     assert meet_by_sounds_page_obj.page_title_displayed() is True

    def test_into_wish_wall_page(self, sing_page: SingPage):
        """
        进入心愿墙二级页面
        :param sing_page:
        :return:
        """
        wish_wall_page_obj = sing_page.wish_wall_icon_click()
        assert wish_wall_page_obj.page_title_displayed() is True

    def test_into_song_details_page(self, sing_page: SingPage):
        """
        进入歌曲详情页二级页面 判断歌曲名称是否与点歌台点击的一致
        todo ios获取不到歌曲名称
        :param sing_page:
        :return:
        """
        song_details_page = sing_page.song_cell_click()
        sing_page_song_name = sing_page.get_click_song_cell_song_name().strip()
        song_details_page_song_name = song_details_page.get_song_name()
        assert (sing_page_song_name == song_details_page_song_name) is True


if __name__ == "__main__":
    pytest.main(["-s", "test_sing_page.py"])
