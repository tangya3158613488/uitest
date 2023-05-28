"""
歌单
"""
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class SongListPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def in_song_list_page(self):
        # print(self.appium_driver.get_page_source())
        """
        判断是否在歌单页
        :return: 
        """
        return self.appium_driver.element_displayed(self.get_object("song_list_title"))

    def create_song_list_is_show(self):
        """
        判断新建歌单弹窗是否出现
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("create_song_list_pop_title"))