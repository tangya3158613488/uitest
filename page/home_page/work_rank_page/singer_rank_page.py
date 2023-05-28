from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.home_page.work_rank_page.capable_singer_rank_page import CapableSingerRankPage
from page.home_page.home_base_element_page import HomeBaseElementPage


class SingerRankPage(HomeBaseElementPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.CapableBeiJing = '北京实力歌手榜'
        self.HottestBeiJing = '北京最火歌手榜'

    def singer_rank_work_cell_displayed(self):
        # 子榜作品cell
        return self.appium_driver.element_displayed(self.get_object('singer_rank_work_cell'))

    def singer_rank_work_singer_name_displayed(self):
        # 子榜歌手昵称
        return self.appium_driver.element_displayed(self.get_object('work_singer_name'))

    def capable_singer_rank_title_displayed(self):
        # 实力歌手榜
        return self.appium_driver.element_displayed(self.get_object('capable_singer_rank_btn'))

    def capable_singer_rank_title_text(self):
        # 实力歌手榜title text
        return self.appium_driver.find_element(self.get_object('capable_singer_rank_title')).text

    def capable_singer_rank_title_click(self):
        # 点击进入 实力歌手榜
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("capable_singer_rank_btn")))
        return CapableSingerRankPage(self.appium_driver)

    def hottest_singer_rank_title_displayed(self):
        # 最火歌手榜
        return self.appium_driver.element_displayed(self.get_object('hottest_singer_rank_btn'))

    def hottest_singer_rank_title_text(self):
        # 最火歌手榜title  text
        return self.appium_driver.find_element(self.get_object('hottest_singer_rank_title')).text

    def hottest_singer_rank_title_click(self):
        # 进入最火歌手榜
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hottest_singer_rank_btn")))
        # return HottestSingerRankPage(self.appium_driver)

    def nation_capable_singer_rank_title_displayed(self):
        # 全国实力歌手榜cell
        return self.appium_driver.element_displayed(self.get_object('nation_capable_singer_rank_title'))

    def nation_hottest_singer_rank_title_displayed(self):
        # 全国最火歌手榜
        return self.appium_driver.element_displayed(self.get_object('nation_hottest_singer_rank_title'))

    def newer_singer_rank_title_displayed(self):
        # 新人榜
        self.find_els("newer_singer_rank_title")
        return self.appium_driver.element_displayed(self.get_object('newer_singer_rank_title'))

    def compete_rank_icon_displayed(self):
        # 完整榜单
        return self.appium_driver.element_displayed(self.get_object('compete_rank_icon'))
