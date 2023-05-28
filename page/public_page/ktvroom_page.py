import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from ..ktv_page.ktv_page import KtvPage
from common.driver.appium_driver import AppiumDriver
from .navigationbar_page import NavigationBarPage
from .tabbar_page import TabBarPage
from ..liveroom_page.base_liveroom_page import BaseLiveRoomPage
from ..liveroom_page.liveroom_quit_alert_page import LiveRoomQuitAlertPage


class KtvRoomPage:

    def __init__(self, appium_driver: AppiumDriver):
        self.appium_driver = appium_driver

    def my_tab_click(self):
        """
        mytab 点击
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("my_tab")))
        return KtvPage(self.appium_driver)


