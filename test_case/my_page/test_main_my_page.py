"""
我的，个人主页-主态
"""
import time

import pytest

from page.my_page.main_my_page import MainMyPage


class TestMainMyPage:

    # def test_back_ground_img(self, main_my_page: MainMyPage):
    #     """
    #     点击主页背景图
    #     :param my_page:
    #     :return:
    #     """
    #     home_page_dress_page_obj = main_my_page.click_back_ground_img()
    #     assert home_page_dress_page_obj.in_home_page_dress_page() is True

    def test_click_coin_btn(self, main_my_page: MainMyPage):
        """
        点击金币/钻石按钮
        :param my_page:
        :return:
        """
        my_wallet_page_obj = main_my_page.click_coins_btn()
        assert my_wallet_page_obj.in_my_wallet_page() is True

    def test_click_global_player(self, main_my_page: MainMyPage):
        """
        点击全局播放器
        :param main_my_page:
        :return:
        """
        global_player_page_obj = main_my_page.click_glolal_palyer_btn()
        assert global_player_page_obj.in_gloabl_play_page() is True

    def test_daily_task_btn(self, main_my_page: MainMyPage):
        """
        点击任务中心
        :param my_page:
        :return:
        """
        task_center_page_obj = main_my_page.click_daily_task_btn()
        assert task_center_page_obj.page_title_displayed() is True

    def test_headphoto(self, main_my_page: MainMyPage):
        """
        点击用户头像-我的相册
        :param my_page:
        :return:
        """
        photo_album_page_obj = main_my_page.click_headphoto_btn()
        my_album_page_obj = photo_album_page_obj.click_my_album_btn()
        assert my_album_page_obj.in_photo_album_page() is True

    def test_click_edit_data_btn(self, main_my_page: MainMyPage):
        """
        点击编辑资料
        :param my_page:
        :return:
        """
        personal_information_page = main_my_page.click_edit_data_btn()
        assert personal_information_page

    def test_vip_grade_icon(self, main_my_page: MainMyPage):
        """
        点击vip等级icon
        :param main_my_page:
        :return:
        """
        if main_my_page.vip_grade_icon_displayed():
            vip_center_page_obj = main_my_page.click_vip_grade_icon()
            assert vip_center_page_obj.in_vip_center_page() is True

    def test_click_attention_number_btn(self, main_my_page: MainMyPage):
        """
        点击关注
        :param my_page:
        :return:
        """
        attention_page = main_my_page.click_attention_number_btn()
        assert attention_page.in_attention_page()

    def test_click_fans_btn(self, main_my_page: MainMyPage):
        """
        点击粉丝
        :param my_page:
        :return:
        """
        fans_page_obj = main_my_page.click_fans_number_btn()
        assert fans_page_obj.in_my_fans_page()

    def test_click_come_to_visit_btn(self, main_my_page: MainMyPage):
        """
        点击来访
        :param my_page:
        :return:
        """
        lately_visit_page = main_my_page.click_come_to_visit_btn()
        assert lately_visit_page.in_lately_visit_page()

    def test_click_list_icon(self, main_my_page: MainMyPage):
        """
        点击上榜icon
        :param my_page:
        :return:
        """
        list_record_page_obj = main_my_page.click_list_icon()
        assert list_record_page_obj.in_list_record_page()

    def test_click_singer_grade_icon(self, main_my_page: MainMyPage):
        """
        点击歌手等级icon
        :param my_page:
        :return:
        """
        singer_grade_page_obj = main_my_page.click_singer_grade()
        assert singer_grade_page_obj.in_singer_grade_page() is True

    def test_click_wealth_grade_icon(self, main_my_page: MainMyPage):
        """
        点击财富等级icon
        :param my_page:
        :return:
        """
        wealth_grade_page_obj = main_my_page.click_wealth_grade()
        assert wealth_grade_page_obj.in_wealth_grade_page() is True

    def test_click_play_count_icon(self, main_my_page: MainMyPage):
        """
        点击播放次数icon
        :param my_page:
        :return:
        """
        play_count_pop_obj = main_my_page.click_play_count_icon()
        assert play_count_pop_obj.play_count_pop_displayed() is True

    def test_click_gender_age_icon(self, main_my_page: MainMyPage):
        """
        点击性别年龄星座icon
        :param my_page:
        :return:
        """
        edit_personal_info_page_obj = main_my_page.click_gender_age_icon()
        assert edit_personal_info_page_obj.in_personal_information_page() is True

    def test_click_location_icon(self, main_my_page: MainMyPage):
        """
        点击现居地icon
        :param my_page:
        :return:
        """
        edit_personal_info_page_obj = main_my_page.click_location_icon()
        assert edit_personal_info_page_obj.in_personal_information_page() is True

    # def test_click_add_friend_btn(self,main_my_page:MainMyPage):
    #     """
    #     点击添加好友
    #     :param my_page:
    #     :return:
    #     """
    #     find_people_page = main_my_page.click_add_friend_btn()
    #     return find_people_page.in_find_people_page()

    def test_click_my_group_btn(self, main_my_page: MainMyPage):
        """
        点击我的群组
        :param my_page:
        :return:
        """
        my_group_page = main_my_page.click_my_group_btn()
        assert my_group_page.in_my_group_page()

    def test_click_my_room_btn(self, main_my_page: MainMyPage):
        """
        点击我的包房：如果绑定手机号title没有出现，走直接进包房逻辑，否则证明进入到绑定手机号页面，该条case通过。
        :return:
        """
        if main_my_page.my_room_is_displayed():
            bind_tel_page_obj = main_my_page.click_my_room_icon_no_room()
            if not bind_tel_page_obj.page_title_displayed():
                main_my_page.click_my_room_icon_have_room().close_btn_click().quit_room_btn_click()

    def test_click_local_record_btn(self, main_my_page: MainMyPage):
        """
        点击本地录音
        :param main_my_page:
        :return:
        """
        local_record_page = main_my_page.click_work().click_local_record_btn()
        assert local_record_page.in_local_record_page()

    def test_click_vip_center_btn(self, main_my_page: MainMyPage):
        """
        点击会员中心按钮
        :param main_my_page:
        :return:
        """
        vip_center_page_obj = main_my_page.click_vip_center_btn()
        assert vip_center_page_obj.in_vip_center_page() is True

    def test_click_my_song_list_btn(self, main_my_page: MainMyPage):
        """
        点击我的歌单
        :param main_my_page:
        :return:
        """
        song_list_page = main_my_page.click_work().click_my_song_list_btn()
        assert song_list_page.in_song_list_page() or song_list_page.create_song_list_is_show()

    def test_click_submit_work_btn(self, main_my_page: MainMyPage):
        """
        点击我的投稿
        :return:
        :rtype:
        """
        submit_work_page_obj = main_my_page.click_submit_work_btn()
        assert submit_work_page_obj.title() == "选择作品"
    def test_click_data_tab_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab
        :param click_data_tab_btn:
        :return:
        """
        main_my_page.click_data_tab_btn()
        assert main_my_page.data_tab_show()

    def test_click_photo_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab下的相册
        :param main_my_page:
        :return:
        """
        photo_album = main_my_page.click_photo_btn()
        assert photo_album.in_photo_album_page()

    def test_click_my_information_btn(self, main_my_page: MainMyPage):
        """
        点击资料下的我的信息
        :param main_my_page:
        :return:
        """
        main_my_page.click_data_tab_btn()
        time.sleep(1)
        main_my_page.appium_driver.swipe_up(500)
        information_page = main_my_page.click_my_information_btn()
        assert information_page.in_personal_information_page()

    def test_click_my_achievement_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-我的成就
        :return:
        """
        my_achievement_page_obj = main_my_page.click_my_achievement_btn()
        assert my_achievement_page_obj.in_achievement_page() is True

    def test_click_i_liked_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-我赞过的
        :return:
        """
        if main_my_page.liked_btn_displayed():
            i_liked_page_obj = main_my_page.click_liked_btn()
            assert i_liked_page_obj.in_i_liked_page() is True

    def test_click_forward_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-我转发的
        :return:
        """
        if main_my_page.forward_btn_displayed():
            forward_page_obj = main_my_page.click_forward_btn()
            assert forward_page_obj.in_my_forward_works_page() is True

    def test_click_data_my_group_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-我的群组
        :return:
        """
        if main_my_page.group_btn_displayed():
            my_group_page_obj = main_my_page.click_group_btn()
            assert my_group_page_obj.in_my_group_page() or my_group_page_obj.in_my_group_page_one() is True

    def test_click_data_my_room_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-我的包房
        :return:
        """
        if main_my_page.room_btn_displayed():
            my_room_page_obj = main_my_page.click_room_btn()
            assert my_room_page_obj.more_btn_displayed() is True
            my_room_page_obj.close_btn_click().quit_room_btn_click()

    def test_click_my_live_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-我的直播
        :return:
        """
        if main_my_page.live_btn_displayed():
            my_live_page_obj = main_my_page.click_live_btn()
            assert my_live_page_obj.in_my_live_page() is True

    def test_click_qr_code_btn(self, main_my_page: MainMyPage):
        """
        点击资料tab-二维码
        :return:
        """
        qr_code_page_obj = main_my_page.click_qr_code_btn()
        assert qr_code_page_obj.in_qr_code_page() is True

    def test_click_dynamic_tab_btn(self, main_my_page: MainMyPage):
        """
        点击动态tab
        :param main_my_page:
        :return:
        """
        main_my_page.click_dynamic_tab_btn()
        assert main_my_page.dynamic_cell_show() or main_my_page.send_dynamic_btn_show()

    def test_click_music_tab_btn(self, main_my_page: MainMyPage):
        """
        点击音乐tab
        :return:
        """
        if main_my_page.music_tab_show():
            main_my_page.click_music_tab_btn()
            assert main_my_page.music_cell_show()

    def test_click_footprint_tab_btn(self, main_my_page: MainMyPage):
        """
        点击足迹tab
        :param main_my_page:
        :return:
        """
        main_my_page.click_footprint_tab_btn()
        assert main_my_page.footprint_tab_show()


if __name__ == "__main__":
    pytest.main(["-s", "test_main_my_page.py"])
    # pytest.main(['-vs', './test_case/test_0616.py::TestLogin::test_02'])
