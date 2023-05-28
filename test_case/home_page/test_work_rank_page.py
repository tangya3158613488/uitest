import pytest
from page.home_page.hot_page import HomePage
from page.home_page.work_rank_page.work_rank_page import WorkRankPage
from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector


class TestWorkRankPage:
    def test_work_rank_tab_check(self, home_page: HomePage):
        """
         校验榜单顶部各项tab，存在
         :return:
         """
        work_rank_obj = home_page.work_rank_click()
        assert work_rank_obj.region_rank_title_displayed() is True
        assert work_rank_obj.national_gold_rank_title_displayed() is True
        assert work_rank_obj.voice_rank_title_displayed() is True
        assert work_rank_obj.total_rank_tab_displayed() is True
        work_rank_obj.black_btn_click()

    def test_national_tab_banner_check(self, home_page: HomePage):
        """
        校验全国榜跑马灯更新时间，存在
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        assert work_rank_obj.work_rank_banner_displayed() is True
        assert work_rank_obj.work_rank_update_time_displayed() is True
        work_rank_obj.black_btn_click()

    def test_national_tab_rule(self, home_page: HomePage):
        """
        检查规则正常可查看
        :param work_rank_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.work_rank_rule_displayed():
            work_rank_obj.work_rank_rule_click()
            work_rank_obj.work_rank_rule_i_know_click()
            work_rank_obj.black_btn_click()
            if work_rank_obj.work_rank_rule_title_displayed():
                work_rank_obj.work_rank_rule_i_know_click()
                assert work_rank_obj.work_rank_rule_title_displayed() is False

    @pytest.mark.skipif(AppiumDriver.get_platform() == PlatformSelector.IOS, reason='ios')
    def test_national_tab_work_card_check(self, home_page: HomePage):
        """
        检查 作品card区域元素
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        assert work_rank_obj.work_card_displayed() is True
        assert work_rank_obj.work_rank_protect_head_displayed() is True
        assert work_rank_obj.work_rank_ranking_displayed() is True
        assert work_rank_obj.work_rank_like_displayed() is False
        assert work_rank_obj.work_rank_work_name_displayed() is True
        assert work_rank_obj.work_rank_user_name_displayed() is True
        assert work_rank_obj.work_rank_member_level_displayed() is True
        assert work_rank_obj.work_rank_singer_level_displayed() is True
        assert work_rank_obj.work_rank_wealth_level_displayed() is True

        while work_rank_obj.work_rank_up_icon_displayed() is False:
            work_rank_obj.work_rank_swipe_up(1000)

        while work_rank_obj.work_rank_mv_icon_displayed() is False:
            work_rank_obj.work_rank_swipe_up(1000)

    def test_national_tab_work_cell_check(self, home_page: HomePage):
        """
        检查 全国榜作品cell
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        assert work_rank_obj.work_card_displayed() is True
        # assert work_rank_obj.work_rank_ranking_displayed() is True
        work_rank_obj.black_btn_click()

    def test_national_tab_fans_contribute(self, home_page: HomePage):
        """
        检查粉丝贡献榜
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        fans_contribute = work_rank_obj.work_rank_protect_head_click()
        if fans_contribute.fans_contribute_title_displayed():
            assert fans_contribute.head_photo_displayed() is True
            assert fans_contribute.user_name_displayed() is True
            assert fans_contribute.leverl_wealth_displayed() is True
            assert fans_contribute.contribute_coin_count_displayed() is True
            assert fans_contribute.gift_icon_displayed() is True
            fans_contribute.black_btn_click()
            work_rank_obj.black_btn_click()
            assert work_rank_obj.work_rank_protect_head_displayed() is False


    def test_national_tab_receive_gift_list(self, home_page: HomePage):
        """
        作品收到礼物列表
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        fans_contribute = work_rank_obj.work_rank_protect_head_click()
        if fans_contribute.gift_box_btn_displayed():
            fans_contribute.gift_box_click()
            assert fans_contribute.receive_gift_title_displayed() is True
            assert fans_contribute.gift_image_displayed() is True
            fans_contribute.black_btn_click()
            fans_contribute.black_btn_click()
            work_rank_obj.black_btn_click()
            assert work_rank_obj.work_rank_protect_head_displayed() is False

    @pytest.mark.skipif(AppiumDriver.get_platform() == PlatformSelector.IOS, reason='ios')
    def test_national_tab_work_player_check(self, home_page: HomePage):
        """
        全国榜 作品播放
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        assert work_rank_obj.work_card_displayed() is True
        player_obj = work_rank_obj.work_card_click()
        if player_obj.mp4_close_btn_displayed():
            pass
        else:
            assert player_obj.details_tab() is True

    def test_region_rank_title_check(self, home_page: HomePage):
        """
        地区榜 定位地区校验
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.region_rank_title_displayed():
            region_rank_obj = work_rank_obj.region_rank_title_click()
            assert region_rank_obj.region_rank_region_icon_displayed() is True

    def test_region_rank_choose_region(self, home_page: HomePage):
        """
        地区榜 地区选择
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.region_rank_title_displayed():
            region_rank_obj = work_rank_obj.region_rank_title_click()
            if region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.DongCheng:
                work_rank_obj.region_rank_title_click()
                assert region_rank_obj.region_rank_old_region_displayed() is True
                region_rank_obj.region_rank_beijing_click()
                region_rank_obj.region_rank_chaoyang_click()
                region_rank_obj.region_rank_complete_click()
                assert region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.ChaoYang
                assert region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.ChaoYang
                work_rank_obj.black_btn_click()

            elif region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.ChaoYang:
                work_rank_obj.region_rank_title_click()
                assert region_rank_obj.region_rank_old_region_displayed() is True
                region_rank_obj.region_rank_beijing_click()
                region_rank_obj.region_rank_dongcheng_click()
                region_rank_obj.region_rank_complete_click()
                assert region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.DongCheng

            else:
                work_rank_obj.region_rank_title_click()
                assert region_rank_obj.region_rank_old_region_displayed() is True
                region_rank_obj.region_rank_beijing_click()
                region_rank_obj.region_rank_chaoyang_click()
                region_rank_obj.region_rank_complete_click()
                assert region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.DongCheng
                assert region_rank_obj.region_rank_title_update_text() == region_rank_obj.BeiJing
                work_rank_obj.black_btn_click()

    def test_region_rank_choose_gps_region_check(self, home_page: HomePage):
        """
        地区榜 选择GPS定位-北京 todo
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        region_rank_obj = work_rank_obj.region_rank_title_click()
        work_rank_obj.region_rank_title_click()
        # 选择GPS定位-北京
        assert region_rank_obj.region_rank_gps_area_displayed() is True
        region_rank_obj.region_rank_gps_area_click()
        region_rank_obj.region_rank_complete_click()
        assert region_rank_obj.region_rank_get_region_icon_text() == region_rank_obj.BeiJing
        work_rank_obj.black_btn_click()
        if work_rank_obj.region_rank_title_displayed():
            region_rank_obj = work_rank_obj.region_rank_title_click()
            region_rank_obj.region_rank_time_role_click()
            if work_rank_obj.work_rank_rule_title_displayed():
                work_rank_obj.work_rank_rule_i_know_click()
                assert work_rank_obj.work_rank_rule_title_displayed() is False
            assert region_rank_obj.region_rank_time_role_displayed() is True
            # assert region_rank_obj.region_rank_rule_btn_displayed() is True
            work_rank_obj.black_btn_click()

    def test_region_rank_update_region_check(self, home_page: HomePage):
        """
        地区榜重新选择地区 北京-朝阳
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        region_rank_obj = work_rank_obj.region_rank_title_click()
        work_rank_obj.region_rank_title_click()

        # 选择北京-东城
        assert region_rank_obj.region_rank_gps_area_displayed() is True
        region_rank_obj.region_rank_beijing_click()
        region_rank_obj.region_rank_dongcheng_click()
        region_rank_obj.region_rank_complete_click()
        assert region_rank_obj.region_rank_new_selected_area_text() == region_rank_obj.DongCheng

        # 选择北京-朝阳
        work_rank_obj.region_rank_title_click()
        assert region_rank_obj.region_rank_gps_area_displayed() is True
        region_rank_obj.region_rank_beijing_click()
        region_rank_obj.region_rank_chaoyang_click()
        region_rank_obj.region_rank_complete_click()
        assert region_rank_obj.region_rank_old_selected_area_text() == region_rank_obj.ChaoYang
        work_rank_obj.black_btn_click()

    def test_region_rank_time_role(self, home_page: HomePage):
        """
        地区榜规则正常展示
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        assert work_rank_obj.region_rank_title_displayed() is True
        work_rank_obj.region_rank_title_click()
        assert work_rank_obj.work_card_displayed() is True
        assert work_rank_obj.work_rank_ranking_displayed() is True
        assert work_rank_obj.work_rank_work_name_displayed() is True
        assert work_rank_obj.work_rank_user_name_displayed() is True
        assert work_rank_obj.work_rank_member_level_displayed() is True
        assert work_rank_obj.work_rank_singer_level_displayed() is True

    def test_region_rank_work_player_check(self, home_page: HomePage):
        """
        地区榜 作品播放
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.region_rank_title_displayed():
             work_rank_obj.region_rank_title_click()
             assert work_rank_obj.work_card_displayed() is True
             player_obj = work_rank_obj.work_card_click()
             if player_obj.mp4_close_btn_displayed():
                 pass
             else:
                 assert player_obj.details_tab() is True

    def test_good_voice_into(self, home_page: HomePage):
        """
        好声音 检查作品卡元素
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.region_rank_title_displayed():
            region_rank_obj = work_rank_obj.region_rank_title_click()
            assert region_rank_obj.region_rank_card_displayed() is True
            # assert region_rank_obj.region_rank_hottest_icon_first_displayed() is True
            # assert region_rank_obj.region_rank_hottest_icon_sec_displayed() is True
            # assert region_rank_obj.region_rank_hottest_icon_three_displayed() is True
            work_rank_obj.black_btn_click()
        good_voice_page = work_rank_obj.good_voice_tab_click()
        assert good_voice_page.good_voice_time_role_displayed() is True

    def test_good_voice_rule(self,home_page: HomePage):
        """
        好声音 规则可查看
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        good_voice_page = work_rank_obj.good_voice_tab_click()
        assert good_voice_page.good_voice_time_role_displayed() is True
        good_voice_page.good_voice_role_click()
        if work_rank_obj.work_rank_rule_title_displayed():
            work_rank_obj.work_rank_rule_i_know_click()
            assert work_rank_obj.work_rank_rule_title_displayed() is False

    def test_good_voice_work_card_check(self, home_page: HomePage):
        """
        检查 作品card区域元素
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        good_voice_page = work_rank_obj.good_voice_tab_click()
        assert good_voice_page.good_voice_time_role_displayed() is True
        assert work_rank_obj.work_card_displayed() is True
        assert work_rank_obj.work_rank_ranking_displayed() is True
        assert work_rank_obj.work_rank_work_name_displayed() is True
        assert work_rank_obj.work_rank_user_name_displayed() is True

        while work_rank_obj.work_rank_wealth_level_displayed() is False:
            work_rank_obj.work_rank_swipe_up(1000)

        # while work_rank_obj.work_rank_v_logo_displayed() is False:
        #     work_rank_obj.work_rank_swipe_up(1000)

        while work_rank_obj.work_rank_member_level_displayed() is False:
            work_rank_obj.work_rank_swipe_up(1000)

        while work_rank_obj.work_rank_singer_level_displayed() is False:
            work_rank_obj.work_rank_swipe_up(1000)

    def test_good_voice_work_player_check(self, home_page: HomePage):
        """
        地区榜 作品播放
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        good_voice_page = work_rank_obj.good_voice_tab_click()
        assert good_voice_page.good_voice_time_role_displayed() is True
        assert work_rank_obj.work_card_displayed() is True
        player_obj = work_rank_obj.work_card_click()
        if player_obj.mp4_close_btn_displayed():
            pass
        else:
            assert player_obj.details_tab() is True

    # def test_region_rank_work_cell_check(self, home_page: HomePage):
    #     """
    #     地区榜 作品crad 信息检验
    #     :param home_page:
    #     :return:
    #     """
    #     work_rank_obj = home_page.work_rank_click()
    #     if work_rank_obj.region_rank_title_displayed():
    #         region_rank_obj = work_rank_obj.region_rank_title_click()
    #         assert region_rank_obj.region_rank_card_displayed() is True
    #         assert region_rank_obj.region_rank_hottest_icon_first_displayed() is True
    #         assert region_rank_obj.region_rank_hottest_icon_sec_displayed() is True
    #         assert region_rank_obj.region_rank_hottest_icon_three_displayed() is True
    #         work_rank_obj.black_btn_click()

    def test_national_gold_rank_title_check(self, home_page: HomePage):
        """
        全国金榜 刷新时间和规则 校验
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.national_gold_rank_title_displayed():
            gold_rank_obj = work_rank_obj.national_gold_rank_title_click()
            assert gold_rank_obj.gold_rank_time_role_displayed() is True
            assert gold_rank_obj.gold_rank_rule_btn_displayed() is True

    def test_national_gold_rank_card_check(self, home_page: HomePage):
        """
        全国金榜 card 信息校验
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.national_gold_rank_title_displayed():
            gold_rank_obj = work_rank_obj.national_gold_rank_title_click()
            assert gold_rank_obj.gold_rank_attention_icon_displayed() is True
            assert gold_rank_obj.gold_rank_feed_icon_play_displayed() is True
            assert gold_rank_obj.gold_rank_feed_head_rank_displayed() is True
            assert gold_rank_obj.gold_rank_feed_head_portrait_displayed() is True
            assert gold_rank_obj.gold_rank_feed_head_vip_icon_displayed() is True
            assert gold_rank_obj.gold_rank_user_name_text_tv_displayed() is True
            assert gold_rank_obj.gold_rank_user_vip_imageview_displayed() is True
            assert gold_rank_obj.gold_rank_user_singer_imageview_displayed() is True
            assert gold_rank_obj.gold_rank_user_wealth_imageview_displayed() is True

    def test_national_gold_rank_work_play_check(self, home_page: HomePage):
        """
        全国金榜 作品播放
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.national_gold_rank_title_displayed():
            gold_rank_obj = work_rank_obj.national_gold_rank_title_click()
            assert gold_rank_obj.gold_rank_feed_icon_play_displayed() is True
            player_obj = gold_rank_obj.gold_rank_work_card_chick()
            if player_obj.mp4_close_btn_displayed():
                pass
            else:
                assert player_obj.details_tab() is True

    def test_total_rank_tab_check(self, home_page: HomePage):
        """
        校验总榜顶部各项tab，存在
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        if work_rank_obj.national_gold_rank_title_displayed():
            total_rank_obj = work_rank_obj.total_rank_tab_click()
            if total_rank_obj.player_btn_displayed():
                assert total_rank_obj.singer_rank_tab_displayed() is True
                assert total_rank_obj.wealth_rank_tab_displayed() is True
                assert total_rank_obj.player_btn_displayed() is True

    def test_works_list_rank_title_check(self, home_page: HomePage):
        """
        作品榜 子榜name校验
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        assert total_rank_obj.capable_work_rank_title_displayed() is True
        assert total_rank_obj.hottest_work_rank_title_displayed() is True
        assert total_rank_obj.nation_capable_work_rank_title_displayed() is True
        assert total_rank_obj.nation_hottest_work_rank_title_displayed() is True
        assert total_rank_obj.newer_capable_work_rank_title_displayed() is True
        assert total_rank_obj.newer_hottest_work_rank_title_displayed() is True
        assert total_rank_obj.hottest_mv_work_rank_title_displayed() is True
        assert total_rank_obj.popular_work_rank_title_displayed() is True
        assert total_rank_obj.interest_work_rank_title_displayed() is True
        work_rank_obj.black_btn_click()

    def test_works_list_rank_work_card_check(self, home_page: HomePage):
        """
        作品榜 card区域元素校验
        :param home_page:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        if total_rank_obj.works_list_rank_tab_displayed():
            assert total_rank_obj.details_rank_work_cell_displayed() is True
            assert total_rank_obj.details_rank_work_song_name_displayed() is True
            assert total_rank_obj.details_rank_work_nickname_displayed() is True

    def test_details_rank_area_check(self, home_page: HomePage):
        """
        作品榜-继承地区校验
        :param home_page:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        if total_rank_obj.works_list_rank_tab_displayed():
            assert total_rank_obj.capable_work_rank_title_text() == total_rank_obj.CapableBeiJing
            assert total_rank_obj.hottest_work_rank_title_text() == total_rank_obj.HottestBeiJing

    def test_interest_work_detail_title_check(self, home_page: HomePage):
        """
        作品榜-兴趣榜子榜name校验
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        assert total_rank_obj.young_work_rank_title_displayed() is True
        assert total_rank_obj.folk_work_rank_title_displayed() is True
        assert total_rank_obj.rock_work_rank_title_displayed() is True
        assert total_rank_obj.old_work_rank_title_displayed() is True
        assert total_rank_obj.minik_work_rank_title_displayed() is True
        assert total_rank_obj.red_song_work_rank_title_displayed() is True
        work_rank_obj.black_btn_click()

    def test_capable_work_rank_check(self, home_page: HomePage):
        """
        北京实力作品榜 作品校验
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        capable_work_rank_obj = total_rank_obj.capable_work_rank_title_click()
        assert capable_work_rank_obj.capable_rank_work_card_displayed() is True
        assert capable_work_rank_obj.capable_rank_work_rank_first_icon_displayed() is True
        assert capable_work_rank_obj.capable_rank_work_rank_sec_icon_displayed() is True
        assert capable_work_rank_obj.capable_rank_work_rank_thr_icon_displayed() is True
        work_rank_obj.black_btn_click()

    def test_capable_work_rank_rule_check(self, home_page: HomePage):
        """
        北京实力作品榜 规则弹窗 正常
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        capable_work_rank_obj = total_rank_obj.capable_work_rank_title_click()
        if capable_work_rank_obj.capable_rank_rule_displayed():
            total_rank_obj.details_rank_rule_click()
            assert total_rank_obj.details_rank_rule_title_displayed() is True
            assert total_rank_obj.details_rank_rule_rank_reward_displayed() is True
            assert total_rank_obj.details_rank_rule_rank_rule_displayed() is True
            assert total_rank_obj.details_rank_rule_i_know_displayed() is True
            total_rank_obj.details_rank_rule_i_know_click()
            assert total_rank_obj.details_rank_rule_rank_rule_displayed() is False

    def test_hottest_work_rank_check(self, home_page: HomePage):
        """
        北京最火作品榜 作品校验
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        hottest_work_rank_obj = total_rank_obj.hottest_work_rank_title_click()
        assert hottest_work_rank_obj.hottest_rank_work_card_displayed() is True
        assert hottest_work_rank_obj.hottest_rank_work_rank_first_icon_displayed() is True
        assert hottest_work_rank_obj.hottest_rank_work_rank_sec_icon_displayed() is True
        assert hottest_work_rank_obj.hottest_rank_work_rank_thr_icon_displayed() is True

    def test_hottest_work_rank_rule_check(self, home_page: HomePage):
        """
        北京最火作品榜 规则弹窗 正常
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        hottest_work_rank_obj = total_rank_obj.hottest_work_rank_title_click()
        if hottest_work_rank_obj.hottest_rank_rule_displayed():
            hottest_work_rank_obj.hottest_rank_rule_click()
            assert hottest_work_rank_obj.hottest_rank_rule_title_displayed() is True
            assert hottest_work_rank_obj.hottest_rank_rule_rank_reward_displayed() is True
            assert hottest_work_rank_obj.hottest_rank_rule_rank_rule_displayed() is True
            assert hottest_work_rank_obj.hottest_rank_rule_i_know_displayed() is True
            hottest_work_rank_obj.hottest_rank_rule_i_know_click()
            assert hottest_work_rank_obj.hottest_rank_rule_rank_rule_displayed() is False

    def test_hottest_work_rank_current_btn_check(self, home_page: HomePage):
        """
        北京最火作品榜 月榜/总榜btn 切换正常
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        hottest_work_rank_obj = total_rank_obj.hottest_work_rank_title_click()
        if hottest_work_rank_obj.hottest_rank_total_btn_displayed():
            hottest_work_rank_obj.hottest_rank_total_btn_click()
            assert hottest_work_rank_obj.hottest_rank_month_btn_displayed() is True
            if hottest_work_rank_obj.hottest_rank_total_btn_displayed():
                hottest_work_rank_obj.hottest_rank_month_btn_click()
                assert hottest_work_rank_obj.hottest_rank_total_btn_displayed() is True

    def test_singer_rank_detail_title_check(self, home_page: HomePage):
        """
        歌手榜 子榜名称check
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        assert singer_rank_obj.capable_singer_rank_title_displayed() is True
        assert singer_rank_obj.hottest_singer_rank_title_displayed()  is True
        assert singer_rank_obj.nation_capable_singer_rank_title_displayed() is True
        assert singer_rank_obj.nation_hottest_singer_rank_title_displayed() is True
        assert singer_rank_obj.newer_singer_rank_title_displayed() is True

    def test_singer_rank_title_area_check(self, home_page: HomePage):
        """
        歌手榜 继承地区check
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        assert singer_rank_obj.capable_singer_rank_title_text() == singer_rank_obj.CapableBeiJing
        assert singer_rank_obj.hottest_singer_rank_title_text() == singer_rank_obj.HottestBeiJing

    def test_singer_rank_detail_card_check(self, home_page: HomePage):
        """
        歌手榜 card信息check
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        assert singer_rank_obj.singer_rank_work_cell_displayed() is True
        assert singer_rank_obj.singer_rank_work_singer_name_displayed() is True

    def test_capable_singer_rank_singer_card_check(self, home_page: HomePage):
        """
        北京实力歌手榜 歌手card信息 todo
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        capable_singer_rank_obj = singer_rank_obj.capable_singer_rank_title_click()
        assert capable_singer_rank_obj.capable_singer_rank_nickname_displayed() is True
        assert capable_singer_rank_obj.capable_singer_rank_card_displayed() is True
        assert capable_singer_rank_obj.capable_singer_rank_rank_icon_first_displayed() is True
        assert capable_singer_rank_obj.capable_singer_rank_rank_icon_sec_displayed() is True
        assert capable_singer_rank_obj.capable_singer_rank_rank_icon_three_displayed() is True


    def test_capable_singer_rank_rule_check(self, home_page: HomePage):
        """
        北京实力歌手榜 规则弹窗
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        capable_singer_rank_obj = singer_rank_obj.capable_singer_rank_title_click()
        if capable_singer_rank_obj.capable_singer_rank_rule_displayed():
            capable_singer_rank_obj.capable_singer_rank_rule_click()
            assert total_rank_obj.details_rank_rule_title_displayed() is True
            assert total_rank_obj.details_rank_rule_rank_reward_displayed() is True
            assert total_rank_obj.details_rank_rule_i_know_displayed() is True
            total_rank_obj.details_rank_rule_i_know_click()
            assert total_rank_obj.details_rank_rule_rank_reward_displayed() is False

    def test_capable_singer_rank_attention_btn_check(self, home_page: HomePage):
        """
        北京实力歌手榜 关注 按钮正常
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        capable_singer_rank_obj = singer_rank_obj.capable_singer_rank_title_click()
        assert capable_singer_rank_obj.capable_singer_rank_attention_icon_displayed() is True

        # 未关注状态/点击关注
        if capable_singer_rank_obj.capable_singer_rank_attention_state_text() == capable_singer_rank_obj.noattention:
            capable_singer_rank_obj.capable_singer_rank_attention_icon_click()
            assert capable_singer_rank_obj.capable_singer_rank_attention_state_text() == capable_singer_rank_obj.attention is True

    def test_capable_singer_rank_cancel_attention_check(self, home_page: HomePage):
        """
            北京实力歌手榜 取消关注 按钮正常
            :param home_page:
            :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        singer_rank_obj = total_rank_obj.singer_rank_tab_click()
        capable_singer_rank_obj = singer_rank_obj.capable_singer_rank_title_click()
        assert capable_singer_rank_obj.capable_singer_rank_attention_icon_displayed() is True
        # 已关注状态-取消关注
        if capable_singer_rank_obj.capable_singer_rank_attention_state_text() == capable_singer_rank_obj.attention:
            capable_singer_rank_obj.capable_singer_rank_attention_icon_click()
            assert capable_singer_rank_obj.capable_singer_rank_attention_sheet_displayed() is True
            assert capable_singer_rank_obj.capable_singer_rank_sure_btn_displayed() is True
            assert capable_singer_rank_obj.capable_singer_rank_cancel_btn_displayed() is True
            capable_singer_rank_obj.capable_singer_rank_cancel_btn_click()
            assert capable_singer_rank_obj.capable_singer_rank_attention_sheet_displayed() is False
            capable_singer_rank_obj.capable_singer_rank_attention_icon_click()
            capable_singer_rank_obj.capable_singer_rank_sure_btn_click()
            assert capable_singer_rank_obj.capable_singer_rank_attention_state_text() == capable_singer_rank_obj.noattention is True

    def test_wealth_rank_detail_title_check(self, home_page: HomePage):
        """
        歌手榜 子榜名称check
        :param home_page:
        :return:
        """
        work_rank_obj = home_page.work_rank_click()
        total_rank_obj = work_rank_obj.total_rank_tab_click()
        wealth_rank_obj = total_rank_obj.wealth_rank_tab_click()
        assert wealth_rank_obj.music_wealth_rank_title_displayed() is True
        assert wealth_rank_obj.room_wealth_rank_title_displayed() is True
        assert wealth_rank_obj.nation_music_wealth_rank_title_displayed() is True
        assert wealth_rank_obj.nation_room_wealth_rank_title_displayed() is True
        assert wealth_rank_obj.nation_live_wealth_rank_title_displayed() is True

if __name__ == "__main__":
    pytest.main(["-s", "-k", "test_national_tab_work_cell_check", "test_work_rank_page.py"])