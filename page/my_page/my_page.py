#!/usr/bin/python
# coding=utf-8
# author:zhangjiao
"""
我的
"""
from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.global_player_page.global_player_page import GlobalPlayerPage
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage
from page.message_page.my_group_page import MyGroupPage
from page.my_page.achievement_page import AchievementPage
from page.my_page.attention_page import AttentionPage
from page.my_page.i_liked_page import ILikedPage
from page.my_page.list_record_page import ListRecordPage
from page.my_page.my_fans_page import MyFansPage
from page.my_page.my_forward_page import MyForwardWorksPage
from page.my_page.my_live_page import MyLivePage
from page.my_page.photo_album_page import PhotoAlbumPage
from page.my_page.qr_code_page import QrCodePage
from page.my_page.singer_grade_page import SingerGradePage
from page.my_page.vip_center_page import VipCenterPage
from page.my_page.wealth_grade_page import WealthGradePage
from page.objects_controller import ObjectsController
import time

from page.sing_page.bind_tel_page import BindTelPage


class MyPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def click_glolal_palyer_btn(self):
        # print(self.appium_driver.get_page_source())
        """
        点击全局播放器按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("global_player_btn")))
        return GlobalPlayerPage(self.appium_driver)

    def vip_grade_icon_displayed(self):
        """
        vip等级标识是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("vip_class_btn"))

    def click_vip_grade_icon(self):
        """
        点击vip等级标识
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("vip_class_btn")))
        return VipCenterPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_fans_number_btn(self):
        # print(self.appium_driver.get_page_source())
        """
        点击粉丝
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("fans_number_btn")))
        return MyFansPage(self.appium_driver)

    def click_attention_number_btn(self):
        """
        点击关注
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attention_number_btn")))
        return AttentionPage(self.appium_driver)

    def click_list_icon(self):
        """
        点击上榜icon
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("announcement_number_btn")))
        return ListRecordPage(self.appium_driver)

    def click_my_group_btn(self):
        """
        点击我的群组
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_group_btn")))
        return MyGroupPage(self.appium_driver)

    def my_room_is_displayed(self):
        """
        我的包房按钮是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_room_btn"))

    def click_my_room_icon_no_room(self):
        """
        点击我的包房 未创建包房时
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_room_btn")))
        return BindTelPage(self.appium_driver)

    def click_my_room_icon_have_room(self):
        """
        点击我的包房 创建包房时
        case中会先判断是否进入绑定手机号页面，如果是，那么证明没有绑定手机号，case直接通过。如果不是，此时已经进入包房了，所以此处只需要返回包房页面，不需要再次点击开歌房icon
        :return:
        """
        return BaseLiveRoomPage(self.appium_driver)

    def click_vip_center_btn(self):
        """
        点击会员中心
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("vip_center_btn")))
        return VipCenterPage(self.appium_driver)

    def click_singer_grade(self):
        """
        点击歌手等级
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("singer_level_icon")))
        return SingerGradePage(self.appium_driver)

    def click_wealth_grade(self):
        """
        点击财富等级
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rich_level_icon")))
        return WealthGradePage(self.appium_driver)

    def click_play_count_icon(self):
        """
        点击播放次数icon
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("play_count_icon")))
        return self

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def play_count_pop_displayed(self):
        """
        播放次数弹窗展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("play_icon_pop"))

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_data_tab_btn(self):
        """
        点击资料tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("data_tab_btn")))

    def data_tab_show(self):
        """
        展示资料下的内容
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
        return self.appium_driver.element_displayed(self.get_object("photo_btn"))

    def click_photo_btn(self):
        """
        点击资料tab，下的我的/Ta的相册
        :return:
        """
        self.click_data_tab_btn()
        time.sleep(1)
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("photo_btn")))
        return PhotoAlbumPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_my_achievement_btn(self):
        """
        点击资料tab-TA的/我的成就
        :return:
        """
        self.click_data_tab_btn()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            while self.appium_driver.element_displayed(self.get_object("achievement_btn")) is False:
                self.android_swipe_page()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("achievement_btn")))
        return AchievementPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def liked_btn_displayed(self):
        """
        我的/TA的点赞展示
        :return:
        """
        self.click_data_tab_btn()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
            self.android_swipe_page()
        return self.appium_driver.element_displayed(self.get_object("liked_btn"))

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_liked_btn(self):
        """
        点击资料tab-TA的/我的点赞
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("liked_btn")))
        return ILikedPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def forward_btn_displayed(self):
        """
        我的/TA的转发展示
        :return:
        """
        self.click_data_tab_btn()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
            self.android_swipe_page()
        return self.appium_driver.element_displayed(self.get_object("forward_btn"))

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_forward_btn(self):
        """
        点击资料tab-TA的/我的转发
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("forward_btn")))
        return MyForwardWorksPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def group_btn_displayed(self):
        """
        我的/TA的群组展示
        :return:
        """
        self.click_data_tab_btn()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
            self.android_swipe_page()
        return self.appium_driver.element_displayed(self.get_object("groups_btn"))

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_group_btn(self):
        """
        点击资料tab-TA/我的群组
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("groups_btn")))
        return MyGroupPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def room_btn_displayed(self):
        """
        我的/TA的包房展示
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
            self.android_swipe_page()
        self.click_data_tab_btn()
        return self.appium_driver.element_displayed(self.get_object("room_btn"))

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_room_btn(self):
        """
        点击资料tab-TA/我的包房
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("room_btn")))
        return BaseLiveRoomPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def live_btn_displayed(self):
        """
        我的直播展示
        :return:
        """
        self.click_data_tab_btn()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
            self.android_swipe_page()
        return self.appium_driver.element_displayed(self.get_object("live_btn"))

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_live_btn(self):
        """
        点击资料tab-我的直播
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("live_btn")))
        return MyLivePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_qr_code_btn(self):
        """
        点击资料tab-二维码
        :return:
        """
        self.click_data_tab_btn()
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            while self.appium_driver.element_displayed(self.get_object("qr_code_btn")) is False:
                self.android_swipe_page()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("qr_code_btn")))
        return QrCodePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=3, need_catch=True)
    def click_dynamic_tab_btn(self):
        """
        点击动态tab
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dynamic_tab_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def send_dynamic_btn_show(self):
        """
        无动态时，展示发动态按钮
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            self.android_swipe_page()
        return self.appium_driver.element_displayed(self.get_object("send_dynamic_btn"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def dynamic_cell_show(self):
        """
        有动态时，展示动态列表
        :return:
        """
        dynamic_list = self.appium_driver.find_elements(self.get_object("dynamic_say_btn"))
        return len(dynamic_list)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def music_tab_show(self):
        """
        音乐tab是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("music_tab_btn"))

    def click_music_tab_btn(self):
        """
        点击音乐tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("music_tab_btn")))

    def music_cell_show(self):
        """
        展示音乐下的列表
        :return:
        """
        self.click_music_tab_btn()
        time.sleep(1)
        music_list = self.appium_driver.find_elements(self.get_object("music_play_btn"))
        return len(music_list)

    def android_swipe_page(self):
        time.sleep(2)
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.swipe(device_width * 0.5, device_height * 0.8, device_width * 0.5, device_height * 0.6)
