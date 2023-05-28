from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.home_page.work_rank_page.fans_gift_list_page import FansGiftListPage
from page.home_page.work_rank_page.region_rank_page import RegionRankPage

from page.player_page.player_page import PlayerPage
from page.home_page.work_rank_page.good_voice_page import GoodVoicePage
from page.home_page.work_rank_page.national_gold_rank_page import GoldRankPage
from page.home_page.work_rank_page.total_rank_page import TotalRankPage
from common.driver.platform_selector import PlatformSelector


class WorkRankPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def work_rank_title_text_displayed(self):
        """
        各模tab文案元素可见
        workrank_tab_text: national_tab、region_tab、voice_tab、national_gold_tab
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("workrank_tab_text"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def in_rank_page(self):
        """
        有总榜推断为榜单首页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("total_rank_btn"))

    def work_rank_banner_displayed(self):
        """
        全国榜顶部 "跑马灯" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("banner_tab"))

    def work_rank_update_time_displayed(self):
        """
        全国榜更新时间可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("update_time_text"))

    def work_rank_rule_displayed(self):
        """
        获取全国榜 "规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_btn"))

    def work_rank_rule_click(self):
        """
        点击 "规则" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rule_btn")))

    def work_rank_rule_title_displayed(self):
        """
        获取全国榜 "规则标题" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_title"))

    def work_rank_rule_i_know_displayed(self):
        """
        获取规则弹框 "我知道了" btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("i_know_btn"))

    def work_rank_rule_i_know_click(self):
        """
        点击 规则弹框 "我知道了" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_know_btn")))

    def work_rank_protect_head_displayed(self):
        """
        守护者头像可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("protect_head"))

    def work_rank_protect_head_click(self):
        """
        点击 守护者头像
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            self.appium_driver.press_location(self.appium_driver.device_width()-88, 440)  # iOS
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("protect_head")))
        return FansGiftListPage(self.appium_driver)

    def black_btn_click(self):
        """
        点击礼物列表的返回按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_btn")))

    def work_card_displayed(self):
        """
        作品card可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("work_card"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def work_card_click(self):
        """
        作品card 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("work_card")))
        return PlayerPage(self.appium_driver)

    def work_rank_ranking_displayed(self):
        """
        作品前三名标识可见
        :return:
        """
        # print(self.appium_driver.get_page_source())
        return self.appium_driver.element_displayed(self.get_object("ranking"))

    def work_rank_like_displayed(self):
        """
        作品 点赞 标识可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("like"))

    def work_rank_work_name_displayed(self):
        """
        作品 名称 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("work_name"))

    def work_rank_user_name_displayed(self):
        """
        作品 用户名称 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_name"))

    def work_rank_member_level_displayed(self):
        """
        作品 会员等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("member_level"))

    def work_rank_singer_level_displayed(self):
        """
        作品 歌手等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("singer_level"))

    def work_rank_wealth_level_displayed(self):
        """
        作品 财富等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("wealth_level"))

    def work_rank_v_logo_displayed(self):
        """
        用户 大V  可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("v_logo"))

    def work_rank_up_icon_displayed(self):
        """
        作品 排名上升标识 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("up_icon"))

    def work_rank_swipe_up(self, t):
        """
        屏幕滑动
        :return:
        """

        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.swipe(device_width * 0.5, device_height * 0.75, device_width * 0.5, device_height * 0.25, t)

    def work_rank_mv_icon_displayed(self):
        """
        MV作品 角标 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("mv_icon"))

    def region_rank_title_displayed(self):
        """
        地区榜title可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('region_tab'))

    def region_rank_title_click(self):
        """
        地区榜title 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("region_tab")))
        return RegionRankPage(self.appium_driver)

    def good_voice_tab_click(self):
        """
        好声音tab 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("voice_tab")))
        return GoodVoicePage(self.appium_driver)

    def national_gold_rank_title_displayed(self):
        """
        全国金榜icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('national_gold_tab'))

    def voice_rank_title_displayed(self):
        """
        好声音榜icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('voice_tab'))

    def national_gold_rank_title_click(self):
        """
        全国金榜title 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("national_gold_tab")))
        return GoldRankPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def total_rank_tab_displayed(self):
        """
        总榜icon 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('total_tab'))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def total_rank_tab_click(self):
        """
        总榜icon 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("total_tab")))
        return TotalRankPage(self.appium_driver)
