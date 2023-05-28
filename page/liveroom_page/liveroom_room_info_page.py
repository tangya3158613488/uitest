from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.liveroom_page.liveroom_rank_page import LiveRoomRankPage

class LiveRoomRoomInfoPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def vice_house_owner_btn_click(self,mode):
        """
        "副房主按钮点击
        :return:
        """
        if mode == "game":
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("vice_house_owner_btn1")))
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("vice_house_owner_btn")))
        return LiveRoomRankPage(self.appium_driver)

    def  administrator_btn_click(self,mode):
        """
        "管理员按钮点击
        :return:
        """
        if mode == "game":
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("administrator_btn1")))
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("administrator_btn")))
        return LiveRoomRankPage(self.appium_driver)

    def sign_anchor_btn_click(self,mode):
        """
        "签约主播按钮点击
        :return:
        """
        if mode == "game":
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sign_anchor_btn1")))
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sign_anchor_btn")))
        return LiveRoomRankPage(self.appium_driver)

    def room_exclusive_song_btn_click(self):
        """
        "定制房间专属歌曲按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_exclusive_song_btn")))
        return LiveRoomRoomInfoPage(self.appium_driver)

    #@AppiumDriver.wait_for(timeout_sec=10, need_catch=False)

    def judge_room_exclusive_song(self):
        """
        "判断房间专属歌曲是否有歌曲
        "0代表列表没有歌曲，1代表列表有歌曲
        :return:
        """

        if self.appium_driver.element_displayed(self.get_object("song_nane_id")) is True:
            return 1
        else:
            return 0


    def add_room_exclusive_song(self):
        """
        "添加房间专属歌曲
        :return:
        """

        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("add_room_exclusive_song_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("searchbar_input_box_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("searchbar_input_box_btn")).send_keys("我爱你中国"))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("searchbar_search_submit_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("add_song_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_search_btn")))
        return LiveRoomRoomInfoPage(self.appium_driver)

    def clear_all_room_exclusive_song(self):
        """
        "删除房间所有歌曲
        :return:
        """

        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_exclusive_edit_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_exclusive_choose_all_btn")))
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_exclusive_delete_btn")))
        return LiveRoomRoomInfoPage(self.appium_driver)

    def get_room_exclusive_song_name(self):
        """
        "获取歌曲列表第一首给的名字
        :return:
        """
        return self.appium_driver.find_element(self.get_object("song_nane_id")).text

    def room_exclusive_song_page_displayed(self):
        """
        "房间专属歌曲页面是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("room_exclusive_song_page_title"))

    def room_exclusive_song_list_displayed(self):
        """
        "房间专属歌曲页面歌曲list是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("song_nane_id"))

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=False)
    def wait_for_song_name(self, songname):
        """
        "判断歌曲名称是否一致
        :return:
        """
        song_name = self.appium_driver.find_element(self.get_object("song_nane_id")).text
        return song_name == songname




