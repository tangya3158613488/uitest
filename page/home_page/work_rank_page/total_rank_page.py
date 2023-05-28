from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.global_player_page.global_player_page import GlobalPlayerPage

from page.home_page.work_rank_page.singer_rank_page import SingerRankPage
from page.home_page.work_rank_page.wealth_rank_page import WealthRankPage
from page.home_page.work_rank_page.capable_work_rank_page import CapableWorkRankPage
from page.home_page.work_rank_page.hottest_work_rank_page import HottestWorkRankPage
from page.home_page.home_base_element_page import HomeBaseElementPage


class TotalRankPage(HomeBaseElementPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.CapableBeiJing = '北京实力作品榜'
        self.HottestBeiJing = '北京最火作品榜'


    def works_list_rank_tab_displayed(self):
        """
        作品榜tab可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('works_list_tab'))

    def works_list_rank_tab_click(self):
        """
        作品榜tab点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("works_list_tab")))
        return WorksListRankPage(self.appium_driver)

    def singer_rank_tab_displayed(self):
        """
        歌手榜tab可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('singer_tab'))

    def singer_rank_tab_click(self):
        """
        歌手榜tab 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("singer_tab")))
        return SingerRankPage(self.appium_driver)

    def wealth_rank_tab_displayed(self):
        """
        财富榜tab可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('wealth_tab'))

    def wealth_rank_tab_click(self):
        """
        财富榜tab 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("wealth_tab")))
        return WealthRankPage(self.appium_driver)

    def player_btn_displayed(self):
        """
        全局播放器可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('global_player_btn'))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def player_btn_click(self):
        """
        全局播放器 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("global_player_btn")))
        return GlobalPlayerPage(self.appium_driver)


    def details_rank_rule_displayed(self):
        """
        获取作品榜 "规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_btn"))

    def details_rank_rule_click(self):
        """
        点击 "规则" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rule_btn")))

    def details_rank_rule_title_displayed(self):
        """
        获取规则弹窗 "规则标题" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_title"))

    def details_rank_rule_rank_reward_displayed(self):
        """
        获取规则弹框 "上榜奖励"  可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rank_reward"))

    def details_rank_rule_rank_rule_displayed(self):
        """
        获取规则弹框 "上榜规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rank_rule"))

    def details_rank_rule_i_know_displayed(self):
        """
        获取规则弹框 "我知道了" btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("i_know_btn"))

    def details_rank_rule_i_know_click(self):
        """
        点击 规则弹框 "我知道了" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_know_btn")))

    def details_rank_work_cell_displayed(self):
        # 子榜作品cell
        return self.appium_driver.element_displayed(self.get_object('details_rank_work_cell'))

    def details_rank_work_song_name_displayed(self):
        # 子榜歌曲名称
        return self.appium_driver.element_displayed(self.get_object('work_song_name'))

    def details_rank_work_nickname_displayed(self):
        # 子榜用户昵称
        return self.appium_driver.element_displayed(self.get_object('user_nickname'))


    def capable_work_rank_title_displayed(self):
        # 实力作品榜
        return self.appium_driver.element_displayed(self.get_object('capable_work_rank_title'))

    def capable_work_rank_title_text(self):
        # 实力作品榜title text
        return self.appium_driver.find_element(self.get_object('capable_work_rank_title')).text

    def capable_work_rank_title_click(self):
        # 点击进入 实力作品榜
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("capable_work_rank_btn")))
        return CapableWorkRankPage(self.appium_driver)

    def hottest_work_rank_title_displayed(self):
        # 最火实力作品
        return self.appium_driver.element_displayed(self.get_object('hottest_work_rank_title'))

    def hottest_work_rank_title_text(self):
        # 最火实力作品
        return self.appium_driver.find_element(self.get_object('hottest_work_rank_title')).text

    def hottest_work_rank_title_click(self):
        # 进入最火实力作品
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("hottest_work_rank_btn")))
        return HottestWorkRankPage(self.appium_driver)

    def nation_hottest_work_rank_title_displayed(self):
        # 全国最火作品榜
        return self.appium_driver.element_displayed(self.get_object('nation_hottest_work_rank_title'))

    def nation_capable_work_rank_title_displayed(self):
        # 全国实力作品榜cell
        return self.appium_driver.element_displayed(self.get_object('nation_capable_work_rank_title'))

    def newer_capable_work_rank_title_displayed(self):
        # 新人实力作品榜
        self.find_els("newer_capable_work_rank_title")
        return self.appium_driver.element_displayed(self.get_object('newer_capable_work_rank_title'))

    def newer_hottest_work_rank_title_displayed(self):
        # 新人最火作品榜
        self.find_els("newer_hottest_work_rank_title")
        return self.appium_driver.element_displayed(self.get_object('newer_hottest_work_rank_title'))

    def hottest_mv_work_rank_title_displayed(self):
        # 最火mv榜cell
        self.find_els("hottest_mv_work_rank_title")
        return self.appium_driver.element_displayed(self.get_object('hottest_mv_work_rank_title'))

    def popular_work_rank_title_displayed(self):
        # 人气榜cell title
        return self.appium_driver.element_displayed(self.get_object('popular_work_rank_title'))

    def interest_work_rank_title_displayed(self):
        # 兴趣榜 cell title
        self.find_els("interest_work_rank_title")
        return self.appium_driver.element_displayed(self.get_object('interest_work_rank_title'))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def young_work_rank_title_displayed(self):
        # 鲜肉榜
        self.find_els("young_work_rank_title")
        return self.appium_driver.element_displayed(self.get_object('young_work_rank_title'))

    def folk_work_rank_title_displayed(self):
        # 民谣榜
        return self.appium_driver.element_displayed(self.get_object('folk_work_rank_title'))

    def rock_work_rank_title_displayed(self):
        # 摇滚榜
        return self.appium_driver.element_displayed(self.get_object('rock_work_rank_title'))

    def old_work_rank_title_displayed(self):
        # 古风榜
        return self.appium_driver.element_displayed(self.get_object('old_work_rank_title'))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def find_eles(self, els):
        """
        滑动子榜模块
        :return:
        """
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        for i in range(3):
            if self.appium_driver.element_displayed(self.get_object(els)):
                break
            else:
                self.appium_driver.swipe(device_width * 0.85, device_height * 0.9, device_width * 0.2, device_height * 0.9, 1000)


    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def cantonese_work_rank_title_displayed(self):
        # 粤语榜
        self.find_eles('cantonese_work_rank_title')
        return self.appium_driver.element_displayed(self.get_object('cantonese_work_rank_title'))

    def comic_work_rank_title_displayed(self):
        # 动漫榜
        return self.appium_driver.element_displayed(self.get_object('comic_work_rank_title'))

    def r_b_work_rank_title_displayed(self):
        # R&B榜
        return self.appium_driver.element_displayed(self.get_object('r_b_work_rank_title'))

    def language_work_rank_title_displayed(self):
        # 外语榜
        self.find_eles('language_work_rank_title')
        return self.appium_driver.element_displayed(self.get_object('language_work_rank_title'))

    def red_song_work_rank_title_displayed(self):
        # 红歌
        return self.appium_driver.element_displayed(self.get_object('red_song_work_rank_title'))

    def minik_work_rank_title_displayed(self):
        # 咪哒唱吧minik
        self.find_eles('minik_work_rank_title')
        return self.appium_driver.element_displayed(self.get_object('minik_work_rank_title'))

    def compete_rank_icon_displayed(self):
        # 完整榜单
        return self.appium_driver.element_displayed(self.get_object('compete_rank_icon'))
