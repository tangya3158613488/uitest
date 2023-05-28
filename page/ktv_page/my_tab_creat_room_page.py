import time

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage
from page.objects_controller import ObjectsController


class MyTabCreateRoomPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def create_room_alert_displayed(self):
        """
        创建房间弹窗可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("edit_room_name_text"))

    def create_room_queren_btn_click(self):
        """
        创建房间-确认按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("queren_btn")))
        return BaseLiveRoomPage(self.appium_driver)

    def create_room_cancel_btn_click(self):
        """
        创建房间-取消按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_btn")))
        return BaseLiveRoomPage(self.appium_driver)

    def create_auction_room_click(self):
        """
        选择“竞拍”玩法模式，并创建房间
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_playmode_auction")))
        time.sleep(0.2)
        return self.create_room_queren_btn_click()

    def create_mcgame_room_click(self):
        """
        选择“游戏”玩法模式，并创建房间
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            self.appium_driver.press_location(self.appium_driver.device_width()-100, 445)  # iOS"游戏"btn坐标
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_playmode_mc")))
        time.sleep(0.2)
        return self.create_room_queren_btn_click()

    def create_multiclaw_room_click(self):
        """
        选择“唱聊”玩法模式，并创建房间
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_playmode_claw")))
        time.sleep(0.2)
        return self.create_room_queren_btn_click()


    def is_ktv_room(self):
        return self.appium_driver.element_displayed(self.get_object("ktv"))

    def quit_ktv_room(self):
        self.appium_driver.back()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("quit")))

    def create_ktv_room_click(self):
        """
        选择“KTV”玩法模式，并创建房间
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_playmode_ktv")))
        time.sleep(0.2)
        return self.create_room_queren_btn_click()

    def create_grabsing_room_click(self):
        """
        选择“抢唱”玩法模式，并创建房间
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_playmode_grab_sing")))
        time.sleep(0.2)
        return self.create_room_queren_btn_click()
