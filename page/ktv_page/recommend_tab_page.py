from common.driver.appium_driver import AppiumDriver
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage
from page.objects_controller import ObjectsController


class RecommendTabPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=True)
    def wait_for_real_time_chorus_text_displayed(self):
        """
        等待"实时合唱"文案可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("real_time_chorus_id"))

    def room_cell_click(self):
        """
        点击"房间"cell
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("room_cell")))
        return BaseLiveRoomPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=False)
    def wait_for_friends_view_displayed(self):
        """
        等待"好友列表"模块可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("friends_view"))

    def friends_view_playmode(self):
        """
        获取"好友列表"中模式
        :return:
        """
        playmode_el = self.appium_driver.find_element(self.get_object("first_friend_playmode"))
        playmode = self.appium_driver.get_attribute(playmode_el, "name").split("_tag_")[1]
        return playmode

    def first_friend_room_cell_click(self):
        """
        点击好友列表中第一个"好友房间"cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("first_friend_label")))
        return BaseLiveRoomPage(self.appium_driver)
