#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.player_page.more_page.more_page import MorePage
from page.objects_controller import ObjectsController
from page.public_page.navigationbar_page import NavigationBarPage


class PlayerPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver
        self.comment = "评论"
        self.sharefriend = "朋友圈"
        self.sharechat = "微信"

    def giftbox_display(self):
        return self.appium_driver.element_displayed(self.get_object("gift_box"))

    def comment_window(self):
        if self.appium_driver.element_displayed(self.get_object("comment_tab")):
            text = self.appium_driver.find_element(self.get_object("comment")).text
        else:
            self.back_btn_click()
            text = self.appium_driver.find_element(self.get_object("comment")).text
        return self.comment in text

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def share_window(self):
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.appium_driver.element_displayed(self.get_object("share"))
        share = self.appium_driver.find_element(self.get_object("share")).text
        return self.sharefriend in share or self.sharechat in share

    def details_tab(self):
        """
        播放页 详情tab 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("details_tab"))

    def mp4_close_btn_displayed(self):
        """
        mp4 关闭按钮 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("close_btn"))

    def mp4_close_btn_click(self):
        """
        mp4 关闭按钮 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_btn")))

    def mp4_clone_tips_displayed(self):
        """
        mp4 关闭提示语 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("clone_mp4_tips"))

    def confirm_btn_click(self):
        """
        确认 btn 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm_btn")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def live_head_photo_displayed(self):
        """
        直播倒流icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("live_head_photo"))

    @AppiumDriver.wait_for(timeout_sec=20, need_catch=True)
    def lyric_text_displayed(self):
        """
        播放页歌词可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("lyric"))

    def more_btn_click(self):
        """
        更多 btn 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn")))
        return MorePage(self.appium_driver)


    def sendgift_window_display(self):
        return self.appium_driver.element_displayed(self.get_object("longpress_sendgift_window"))

    def sendgift_window_click(self):
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("longpress_sendgift_window")))

    def song_name(self):
        if self.appium_driver.element_displayed(self.get_object("work_name")):
            return self.appium_driver.find_element(self.get_object("work_name")).text
        else:
            self.swipe_up(1000)
            return self.appium_driver.find_element(self.get_object("work_name")).text

    def swipe_up(self, t):
        device_height = self.appium_driver.device_height()
        end_height = device_height * 0.3
        start_height = device_height * 0.7
        width = self.appium_driver.device_width() * 0.5
        return self.appium_driver.swipe(width, start_height, width, end_height, t)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def in_player_page(self):
        """
        根据详情按钮 判断是否进入播放页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("detail_tab"))
