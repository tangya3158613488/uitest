from common.driver.appium_driver import AppiumDriver
from page.home_page.home_base_element_page import HomeBaseElementPage
from page.home_page.home_page import HomePage
from page.home_page.home_search_page.home_search_page import HomeSearchPage
from page.home_page.submit_work_page import SubmitWorkPage
from page.player_page.player_page import PlayerPage


class HotPage(HomeBaseElementPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def submit_work_btn_click(self):
        """
        点击投稿
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("submit_work_btn")))
        return SubmitWorkPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def train_card_displayed(self):
        """
        小火车是否显示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("train_card"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def work_card_click(self):
        """
        点击作品card
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("work_card")))
        return PlayerPage(self.appium_driver)

    def click_search_btn(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))
        return HomeSearchPage(self.appium_driver)


