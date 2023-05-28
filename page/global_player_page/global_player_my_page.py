from common.driver.appium_driver import AppiumDriver
from page.global_player_page.my_collect_page import MyCollectPage
from page.global_player_page.my_playlist_page import MyPlayListPage
from page.global_player_page.player_history_page import PlayerHisotryPage
from page.objects_controller import ObjectsController


class GlobalPlayerMyPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def click_play_all_btn(self):
        """
        点击播放全部
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_all_btn")))
        return self

    def click_player_history_entrance(self):
        """
        点击播放历史
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("player_history_entrance")))
        return PlayerHisotryPage(self.appium_driver)

    def click_my_playlist_entrance(self):
        """
        点击歌单
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("song_sheet_entrance")))
        return MyPlayListPage(self.appium_driver)

    def click_collect_entrance(self):
        """
        点击收藏
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("collect_entrance")))
        return MyCollectPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def work_playing_by_index(self, index=0):
        """
        作品是否正在播放
        :return:
        """
        work_cell_list = self.appium_driver.find_elements(self.get_object("work_cell_list"))
        label = work_cell_list[index].get_attribute("label")
        return label.startswith("正在播放")
