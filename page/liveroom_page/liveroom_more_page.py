import time

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.liveroom_page.liveroom_quit_alert_page import LiveRoomQuitAlertPage
from page.objects_controller import ObjectsController
from page.liveroom_page.liveroom_room_info_page import LiveRoomRoomInfoPage


class LiveRoomMorePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def quit_room_btn_click(self):
        """
        点击"退出房间"btn
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            # 去别人房间，更多面板只展示“操作”模块（建议用超管账号调试case）
            # self.appium_driver.press_location(self.appium_driver.device_width() - 30, 50)  # iOS"退出房间"btn坐标

            # 去自己房间，更多面板展示“房间模式”和“操作”模块
            self.appium_driver.press_location(self.appium_driver.device_width()/6*5,
                                              self.appium_driver.device_height()/3)  # iOS"退出房间"btn坐标
        else:
            time.sleep(2)
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("quit_btn")))
        return LiveRoomQuitAlertPage(self.appium_driver)

    def room_info_btn_click(self):
        """
        "房间信息按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_info_btn")))
        return LiveRoomRoomInfoPage(self.appium_driver)
