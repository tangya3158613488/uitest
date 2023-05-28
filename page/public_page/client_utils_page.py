import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from .navigationbar_page import NavigationBarPage
from .tabbar_page import TabBarPage
from ..liveroom_page.base_liveroom_page import BaseLiveRoomPage
from ..liveroom_page.liveroom_quit_alert_page import LiveRoomQuitAlertPage
from ..objects_controller import ObjectsController
from ..record_page.audio_record_recording_page import RecordRecordingPage
from ..record_page.record_complete_page import RecordCompletePage
from ..record_page.record_publish_page import RecordPublishPage
from ..sing_page.sing_page import SingPage


class ClientUtilsPage(ObjectsController):

    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def go_to_tab_bar_master(self):
        """
        进入tab_bar页面
        :return:
        """
        tab_bar_obj = TabBarPage(self.appium_driver)
        navigation_bar_page = NavigationBarPage(self.appium_driver)
        start_time = time.time()
        while not tab_bar_obj.wait_ktv_tab_displayed():
            try:
                navigation_bar_page.back_btn_click()
            except NoSuchElementException:
                pass
            if time.time() - start_time > 30:
                raise TimeoutException("don't find the tabbar! timeout!")
        return tab_bar_obj

    def go_to_tab_bar(self):
        """
        进入tab_bar页面
        :return:
        """
        tab_bar_obj = TabBarPage(self.appium_driver)
        navigation_bar_page = NavigationBarPage(self.appium_driver)
        base_liveroom_page = BaseLiveRoomPage(self.appium_driver)
        liveroom_quit_alert_page = LiveRoomQuitAlertPage(self.appium_driver)
        start_time = time.time()
        while not tab_bar_obj.wait_ktv_tab_displayed():
            try:
                if base_liveroom_page.more_btn_displayed():
                    base_liveroom_page.more_btn_click().quit_room_btn_click()
                    if liveroom_quit_alert_page.quit_btn_displayed():
                        liveroom_quit_alert_page.quit_btn_click()
                else:
                    navigation_bar_page.back_btn_click()
                    if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
                        if navigation_bar_page.is_dialog_shown():
                            navigation_bar_page.click_dialog_confirm()
            except NoSuchElementException:
                pass
            if time.time() - start_time > 300:
                raise TimeoutException("don't find the tabbar! timeout!")
        return tab_bar_obj

    def teardown_liveroom_page(self):
        """
        返回房间页
        :return:
        """
        navigation_bar_page = NavigationBarPage(self.appium_driver)
        base_liveroom_page = BaseLiveRoomPage(self.appium_driver)
        start_time = time.time()
        while not base_liveroom_page.more_btn_displayed():
            try:
                navigation_bar_page.back_btn_click()
            except NoSuchElementException:
                pass
            if time.time() - start_time > 30:
                raise TimeoutException("go to liveroom page timeout!")
        return base_liveroom_page

    def teardown_record_prepare_page(self):
        navigation_bar_page = NavigationBarPage(self.appium_driver)
        tab_bar_page = TabBarPage(self.appium_driver)
        start_time = time.time()
        while not self.appium_driver.element_displayed(tab_bar_page.get_object("sing_tab")):
            try:
                navigation_bar_page.back_btn_click()
            except NoSuchElementException:
                pass
            if time.time() - start_time > 120:
                raise TimeoutException("totogo to song_board page timeout!")
        return SingPage(self.appium_driver)

    def teardown_record_recording_page(self):
        record_page = RecordRecordingPage(self.appium_driver)
        if record_page.is_exit_btn_shown():
            record_page.exit_recording()
        return SingPage(self.go_to_tab_bar().sing_tab_click().appium_driver)

    def teardown_record_complete_page(self):
        time.sleep(2)
        record_complete_page = RecordCompletePage(self.appium_driver)
        sing_page = SingPage(self.appium_driver)
        if sing_page.is_sing_page():
            return
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            record_complete_page.click_close_btn()
            record_complete_page.click_forgive_btn()
            while not sing_page.is_sing_page():
                NavigationBarPage(self.appium_driver).back_btn_click()
        else:
            if not record_complete_page.is_close_btn_shown():
                NavigationBarPage(self.appium_driver).back_btn_click()
            record_complete_page.click_close_btn()
            record_complete_page.click_forgive_btn()
        return SingPage(self.go_to_tab_bar().sing_tab_click().appium_driver)

    def teardown_record_publish_page(self):
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            record_publish_page = RecordPublishPage(self.appium_driver)
            NavigationBarPage(self.appium_driver).back_btn_click()
            if record_publish_page.is_save_and_exit_btn_shown():
                record_publish_page.click_save_and_exit_btn()

    def grant_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("grant_btn")))
        return self

    def i_see_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_see_btn")))
        return self

    def cannel_btn_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cannel_btn")))

    def try_to_cannel_popUpWindows(self):
        flag = False
        for i in range(3):
            try:
                self.i_see_btn_click()
                flag = True
            except Exception as e:
                pass
            try:
                self.grant_click()
                flag = True
            except Exception as e:
                pass
            try:
                self.cannel_btn_click()
                flag = True
            except Exception as e:
                pass
        return flag

