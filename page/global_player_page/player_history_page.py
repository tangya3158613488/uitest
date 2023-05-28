from common.driver.appium_driver import AppiumDriver

from page.objects_controller import ObjectsController
from page.player_page.player_page import PlayerPage


class PlayerHisotryPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_player_history_page(self):
        return self.appium_driver.element_displayed(self.get_object("title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def get_songname_by_index(self, index=0):
        """
        获取歌名
        :return:
        """
        el = self.appium_driver.find_elements(self.get_object("song_name_list"))[index]
        songname = el.get_attribute("label")
        return songname

    def click_workcell_by_index(self, index=0):
        """
        点击作品
        :return:
        """
        el = self.appium_driver.find_elements(self.get_object("cell_list"))[index]
        self.appium_driver.press_element(el)
        return PlayerPage(self.appium_driver)

    def click_clean_btn(self):
        """
        点击清空作品
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clean_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_delete_btn(self):
        """
        点击删除
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("delete_btn")))
        return self

    def empty_page(self):
        return self.appium_driver.element_displayed(self.get_object("empty_text"))
