from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.home_page.home_base_element_page import HomeBaseElementPage


class WealthRankPage(HomeBaseElementPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.CapableBeiJing = '北京音乐财富排行'
        self.HottestBeiJing = '北京包房财富排行'

    def wealth_rank_work_cell_displayed(self):
        # 子榜作品cell
        return self.appium_driver.element_displayed(self.get_object('singer_rank_work_cell'))

    def wealth_rank_work_singer_name_displayed(self):
        # 子榜歌手昵称
        return self.appium_driver.element_displayed(self.get_object('work_singer_name'))

    def music_wealth_rank_title_displayed(self):
        # 音乐财富排行
        return self.appium_driver.element_displayed(self.get_object('music_wealth_rank_title'))

    def music_wealth_rank_title_text(self):
        # 音乐财富排行title text
        return self.appium_driver.find_element(self.get_object('music_wealth_rank_title')).text

    def music_wealth_rank_title_click(self):
        # 点击进入 音乐财富排行
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("music_wealth_rank_btn")))
        return CapableSingerRankPage(self.appium_driver)

    def room_wealth_rank_title_displayed(self):
        # 包房财富排行
        return self.appium_driver.element_displayed(self.get_object('room_wealth_rank_title'))

    def hottest_singer_rank_title_text(self):
        # 包房财富排行榜title  text
        return self.appium_driver.find_element(self.get_object('room_wealth_rank_title')).text

    def room_wealth_rank_title_click(self):
        # 进入包房财富排行
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_wealth_rank_btn")))
        # return HottestSingerRankPage(self.appium_driver)

    def nation_music_wealth_rank_title_displayed(self):
        # 全国音乐财富排行
        return self.appium_driver.element_displayed(self.get_object('nation_music_wealth_rank_title'))

    def nation_room_wealth_rank_title_displayed(self):
        # 全国包房财富
        return self.appium_driver.element_displayed(self.get_object('nation_room_wealth_rank_title'))

    def nation_live_wealth_rank_title_displayed(self):
        # 全国直播财富
        self.find_els("nation_live_wealth_rank_title")
        return self.appium_driver.element_displayed(self.get_object('nation_live_wealth_rank_title'))

    def music_forbes_rank_title_displayed(self):
        # 音乐福布斯
        self.find_els("music_forbes_rank_title")
        return self.appium_driver.element_displayed(self.get_object('music_forbes_rank_title'))

    def compete_rank_icon_displayed(self):
        # 完整榜单
        return self.appium_driver.element_displayed(self.get_object('compete_rank_icon'))
