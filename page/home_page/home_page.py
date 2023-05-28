from common.driver.appium_driver import AppiumDriver
from page.global_player_page.global_player_page import GlobalPlayerPage
from page.home_page.home_search_page.home_search_page import HomeSearchPage
from page.home_page.work_rank_page.work_rank_page import WorkRankPage
from page.objects_controller import ObjectsController
from page.home_page.attention_page.attention_all_page import AttentionAllPage
from page.home_page.attention_page.attention_work_page import AttentionWorkPage
from page.home_page.attention_page.attention_dynamic_page import AttentionDynamicPage


class HomePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def work_rank_click(self):
        """
        点击 关注页，榜单btn
        :return:
        """

        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object('rank_btn')))
        return WorkRankPage(self.appium_driver)

    def attention_tab_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attetion_btn")))

    def attention_all_click(self):
        self.attention_tab_click()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attention_all_btn")))
        return AttentionAllPage(self.appium_driver)

    def attention_work_click(self):
        self.attention_tab_click()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attention_work_btn")))
        return AttentionWorkPage(self.appium_driver)

    def attention_dynamic_click(self):
        self.attention_tab_click()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attention_dynamic_btn")))
        return AttentionDynamicPage(self.appium_driver)

    def city_click(self):
        self.attention_tab_click()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("city_btn")))
        return AttentionDynamicPage(self.appium_driver)

    def hot_tab_click(self):
        from page.home_page.hot_page import HotPage
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_btn")))
        return HotPage(self.appium_driver)

    def global_player_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("global_player_btn")))
        return GlobalPlayerPage(self.appium_driver)

    def click_rank_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rank_btn")))
        return WorkRankPage(self.appium_driver)

    def click_search_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))
        return HomeSearchPage(self.appium_driver)

