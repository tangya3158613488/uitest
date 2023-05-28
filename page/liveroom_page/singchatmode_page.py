from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
import time



class SingChatModePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def user_online_list_click(self):
        """
        "点击在线成员列表
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_users_info_id")))
        return SingChatModePage(self.appium_driver)

    def user_online_list_displayed(self):
        """
        "在线成员列表是否可见
        :return:
        """

        return self.appium_driver.element_displayed(self.get_object("room_users_info_title_display"))

    def one_seat_click(self):
        """
        "上1号麦
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("image_one_seat_id")))
        return SingChatModePage(self.appium_driver)

    def get_one_seat_username(self):
        """
        "获取1号麦用户名
        :return:
        """
        return self.appium_driver.find_element(self.get_object("image_one_seat_id")).text

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=False)
    def wait_for_song_name(self, username):
        """
        "判断座位上的用户名
        :return:
        """
        user_name = self.get_one_seat_username()
        return user_name == username

    def select_song_btn_click(self):
        """
        "点击点歌按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("select_song_btn_id")))
        return SingChatModePage(self.appium_driver)

    def select_first_song_click(self):
        """
        "点击点歌台第一首歌
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("first_song_btn_id")))
        if self.appium_driver.find_element(self.get_object("first_song_btn_id")) is True:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("first_song_btn_id")))
        else:
            pass
        return SingChatModePage(self.appium_driver)

    def singer_name_displayed(self):
        """
        "演唱者姓名是否展示
        :return:
        """
        time.sleep(10)
        return self.appium_driver.element_displayed(self.get_object("singer_name_displayed"))

    def song_setting_btn_click(self):
        """
        "演唱页面设置按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("song_setting_btn_id")))
        return SingChatModePage(self.appium_driver)

    def finish_song_btn_click(self):
        """
        "切歌按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("finish_song_btn_id")))
        return SingChatModePage(self.appium_driver)

    def singing_area_displayed(self):
        """
        "演唱区页面可见
        :return:
        """
        time.sleep(3)
        return self.appium_driver.element_displayed(self.get_object("singing_area_displayed_text"))