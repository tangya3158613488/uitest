"""
我的 主态
"""

import time
from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.home_page.submit_work_page import SubmitWorkPage
from page.message_page.find_people_page import FindPeoplePage
from page.my_page.home_page_dress_page import HomePageDressPage
from page.my_page.lately_visit_page import LatelyVisitPage
from page.my_page.my_page import MyPage
from page.my_page.my_wallet_page import MyWalletPage
from page.my_page.personal_information_page import PersonalInformationPage
from page.my_page.photo_album_page import PhotoAlbumPage
from page.my_page.song_list_page import SongListPage
from page.record_page.local_record_page import LocalRecordPage
from page.sing_page.task_center_page import TaskCenterPage


class MainMyPage(MyPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def swipe_down_page(self):
        time.sleep(2)
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.swipe(device_width * 0.5, device_height * 0.2, device_width * 0.5, device_height * 0.8)
        return self

    def click_menu_btn(self):
        """
        点击左上角菜单栏
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("menu_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def setting_btn_displayed(self):
        """
        判断设置按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("menu_setting_btn"))

    def click_coins_btn(self):
        """
        点击钻石/金币按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("coins_btn")))
        return MyWalletPage(self.appium_driver)

    def click_daily_task_btn(self):
        """
        点击任务中心
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("daily_task_btn")))
        return TaskCenterPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_back_ground_img(self):
        """
        点击背景图
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_ground_img")))
        return HomePageDressPage(self.appium_driver)

    def click_edit_data_btn(self):
        """
        点击编辑资料
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("edit_data_btn")))
        return PersonalInformationPage(self.appium_driver)

    def click_headphoto_btn(self):
        """
        点击用户头像
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("head_btn")))
        return self

    def click_headphoto_dress_btn(self):
        """
        点击用户头像-头像装扮按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("headphoto_dress_btn")))
        return PhotoAlbumPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_my_album_btn(self):
        """
        点击用户头像-我的相册按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("headphoto_my_album_btn")))
        return PhotoAlbumPage(self.appium_driver)

    def click_come_to_visit_btn(self):
        """
        点击最近来访
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("come_to_visit_btn")))
        return LatelyVisitPage(self.appium_driver)

    def click_gender_age_icon(self):
        """
        点击性别年龄星座icon
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("GenderAgeArea_icon")))
        return PersonalInformationPage(self.appium_driver)

    def click_location_icon(self):
        """
        点击现居地icon
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("local_icon")))
        return PersonalInformationPage(self.appium_driver)

    def click_add_friend_btn(self):
        """
        点击添加好友
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return FindPeoplePage(self.appium_driver)
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("add_friend_btn")))
            return FindPeoplePage(self.appium_driver)

    def click_local_record_btn(self):
        """
        点击本地录音
        :return:
        """
        # if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
        #     self.android_swipe_page()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("local_record_btn")))
        return LocalRecordPage(self.appium_driver)

    def click_work(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("work_list")))
        return self

    def click_my_song_list_btn(self):
        """
        点击我的歌单
        :return:
        """
        # if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
        #     self.android_swipe_page()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_song_list_btn")))
        return SongListPage(self.appium_driver)

    def click_submit_work_btn(self):
        """
        点击我的投稿
        :return:
        :rtype:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("submit_work_btn")))
        return SubmitWorkPage(self.appium_driver)
    def click_my_information_btn(self):
        """
        点击资料tab-我的信息
        :return: 
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_information_btn")))
        return PersonalInformationPage(self.appium_driver)

    def click_footprint_tab_btn(self):
        """
        点击足迹
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("footprint_tab_btn")))

    def footprint_tab_show(self):
        """
        查看足迹tab下展示是否正常
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return True
        else:
            self.click_footprint_tab_btn()
            return self.appium_driver.element_displayed(self.get_object("topic_btn"))

    # def android_swipe_page(self):
    #     time.sleep(2)
    #     device_width = self.appium_driver.device_width()
    #     device_height = self.appium_driver.device_height()
    #     self.appium_driver.swipe(device_width * 0.5, device_height * 0.8, device_width * 0.5, device_height * 0.6)
