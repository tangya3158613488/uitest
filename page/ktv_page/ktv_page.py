from common.driver.appium_driver import AppiumDriver
from page.ktv_page.my_tab_page import MyTabPage
from page.ktv_page.nav_search_tab_page import NavSearchTabPage
from page.ktv_page.recommend_tab_page import RecommendTabPage
from page.objects_controller import ObjectsController
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage


class KtvPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def nav_search_tab_click(self):
        """
        搜索按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("nav_search_tab")))
        return NavSearchTabPage(self.appium_driver)

    def recommend_tab_click(self):
        """
        推荐 tab 点击（注意：打开隐私开关这个就叫“全部”了）
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("recommend_tab")))
        return RecommendTabPage(self.appium_driver)

    def my_tab_click(self):
        """
        我的 tab 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_tab")))
        return MyTabPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def my_tab_displayed(self):
        """
        我的 tab 出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_tab"))

    def mytab_click(self):
        """
        点击"房间"cell
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("my_tab")))
        return KtvPage(self.appium_driver)

    def create_room(self):
        """
        创建房间
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("my_room")))
        return BaseLiveRoomPage(self.appium_driver)

    def create_room(self):
        """
        创建房间
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("my_room")))
        return BaseLiveRoomPage(self.appium_driver)
