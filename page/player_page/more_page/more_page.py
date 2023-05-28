import time

from page.objects_controller import ObjectsController
from common.driver.appium_driver import AppiumDriver


class MorePage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_song_displayed(self):
        """
        导出歌曲 按钮 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("export_song_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_song_btn_click(self):
        """
        导出歌曲 btn 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("export_song_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_mp3_btn_displayed(self):
        """
        导出mp3 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("export_mp3_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_mp3_btn_click(self):
        """
        导出歌曲 btn 点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("export_mp3_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_mp4_btn_displayed(self):
        """
        导出mp4 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("export_mp4_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_mp4_btn_click(self):
        """
        导出mp4 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("export_mp4_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def renewal_btn_displayed(self):
        """
        立即续费 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("renewal_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def renewal_btn_click(self):
        """
        立即续费 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("renewal_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def opening_member_btn_displayed(self):
        """
        确认协议并现在开通 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("Open_immediately"))

    def opening_member_btn_click(self):
        """
        开通会员 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("opening_member")))
        return self


    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def export_mp4_btn_displayed(self):
        """
        导出mp4 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("export_mp4_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def my_export_record_btn_displayed(self):
        """
        我的导出记录 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_export_record_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def my_export_record_btn_click(self):
        """
        我的导出记录 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_export_record_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def my_export_record_title_displayed(self):
        """
        我的导出记录列表 title 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_export_record_title"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def view_song_home_displayed(self):
        """
        查看歌曲主页 按钮 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("view_song_home"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def view_song_home_click(self):
        """
        查看歌曲主页 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("view_song_home")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def singing_btn_displayed(self):
        """
        我要演唱 按钮 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("singing_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def includ_playlist_btn_displayed(self):
        """
        收录至歌单 按钮 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("includ_playlist_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def includ_playlist_btn_click(self):
        """
        收录至歌单 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("includ_playlist_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def my_song_list_displayed(self):
        """
        歌单 歌曲数量标识 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_song_list"))

    @AppiumDriver.wait_for(timeout_sec=10,need_catch=True)
    def my_barrage_btn(self):
        """
        更多-弹幕
        :return:
        :rtype:
        """
        return self.appium_driver.element_displayed(self.get_object("barrage_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def my_song_list_click(self):
        """
        收录至歌单 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("my_song_list")))
        # includ_song_toast = self.appium_driver.get_android_toast()
        includ_song_toast = self.appium_driver.find_element(self.get_object("toast")).text
        if includ_song_toast == "已收录至歌单" or includ_song_toast == '该作品已存在':
            includ_song_status = True
        else:
            includ_song_status = False
        return includ_song_status

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def set_ringing_btn_displayed(self):
        """
        设置振铃 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("set_ringing_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def set_ringing_btn_click(self):
        """
        设置振铃 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("set_ringing_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def confirm_export_btn_displayed(self):
        """
        确定导出 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("confirm_export_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def confirm_export_btn_click(self):
        """
        确定导出 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm_export_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def set_local_ringing_btn_displayed(self):
        """
        设置本地铃声 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("set_local_ringing_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def set_local_ringing_btn_click(self):
        """
        设置本地铃声 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("set_local_ringing_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def skip_prelude_btn_displayed(self):
        """
        自动跳过前奏 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("skip_prelude_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def skip_prelude_btn_click(self):
        """
        自动跳过前奏 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("skip_prelude_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def cancel_skip_prelude_btn_displayed(self):
        """
        取消跳过前奏 按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("cancel_skip_prelude_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def cancel_skip_prelude_btn_click(self):
        """
        取消跳过前奏 按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_skip_prelude_btn")))
        return self









