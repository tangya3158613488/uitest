from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.player_page.player_page import PlayerPage
from page.player_page.semi_chrous_player_page import SemiChrousPlayerPage
from page.record_page.audio_record_prepare_page import RecordPreparePage
from page.sing_page.song_details_page import SongDetailsPage


class SingerDetailsPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def judge_enter_page(self):
        """
        判断是否进入歌手页面
        :return:
        """
        return (self.appium_driver.element_displayed(self.get_object("acc_tab"))
                and self.appium_driver.element_displayed(self.get_object("chrous_tab"))
                and self.appium_driver.element_displayed(self.get_object("sing_tab")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_page_singer_name(self):
        """
        获取页面内歌手名
        :return:
        """
        el = self.appium_driver.find_element(self.get_object("singer_name"))
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.get_attribute(el, 'text')
        else:
            return self.appium_driver.get_attribute(el, 'label')

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_acc_tab(self):
        """
        点击伴奏tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("acc_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_work_tab(self):
        """
        点击作品tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("work_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_chrous_tab(self):
        """
        点击合唱tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("chrous_tab")))
        return self

    def judge_acc_tab_selected(self):
        """
        伴奏tab是否被选中
        :return:
        """
        return self.appium_driver.find_element(self.get_object("acc_tab")).is_selected()

    def judge_work_tab_selected(self):
        """
        作品tab是否被选中
        :return:
        """
        return self.appium_driver.find_element(self.get_object("work_tab")).is_selected()

    def judge_chrous_tab_selected(self):
        """
        合唱tab是否被选中
        :return:
        """
        return self.appium_driver.find_element(self.get_object("chrous_tab")).is_selected()

    def click_acc_single_cell(self):
        """
        点击伴奏tab下单个cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("acc_cell"))[0])
        return SongDetailsPage(self.appium_driver)

    def click_acc_tab_sing_btn(self):
        """
        点击伴奏tab下演唱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("acc_sing_btn"))[0])
        return RecordPreparePage(self.appium_driver)

    def get_acc_tab_singer_name(self):
        """
        获取伴奏tab下歌手名
        :return:
        """
        singer_name = self.appium_driver.get_attribute(
            self.appium_driver.find_elements(self.get_object("acc_tab_singer_name"))[0],
            "text")
        print("伴奏tab下点击的歌手名为：", singer_name)
        return singer_name

    def get_acc_tab_song_name(self):
        """
        获取伴奏tab下歌曲名
        :return:
        """
        song_name = self.appium_driver.get_attribute(
            self.appium_driver.find_elements(self.get_object("acc_tab_song_name"))[0],
            "text")
        print("伴奏tab下点击的歌曲名为：", song_name)
        return song_name

    def click_work_tab_user_photo(self):
        """
        点击作品tab用户头像
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("work_user_headphoto"))[0])

    def click_work_tab_user_nickname(self):
        """
        点击作品tab用户昵称
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("work_user_nickname"))[0])

    def click_work_tab_work_content(self):
        """
        点击作品tab作品描述
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("work_work_content"))[0])
        return PlayerPage(self.appium_driver)

    def click_work_tab_work_cell(self):
        """
        点击作品tab作品cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("work_cell"))[0])
        return PlayerPage(self.appium_driver)

    def click_chrous_tab_open_video_btn(self):
        """
        点击合唱tab仅显示合唱视频btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("only_show_video_chrous_btn"))[0])
        return self

    def click_chrous_tab_user_photo(self):
        """
        点击合唱tab用户头像
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("chrous_user_headphoto"))[0])

    def click_chrous_tab_work_cell(self):
        """
        点击合唱tab作品cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("chrous_work_cell"))[0])
        return SemiChrousPlayerPage(self.appium_driver)

    def click_chrous_tab_chrous_btn(self):
        """
        点击合唱tab合唱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("chrous_btn"))[0])

    def click_chrous_tab_mv_chrous_btn(self):
        """
        点击合唱tab MV合唱 按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("chrous_mv_chrous_btn"))[0])
