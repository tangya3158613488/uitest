from time import sleep

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.record_page.audio_record_prepare_page import RecordPreparePage
from page.sing_page.search_page import search_page_objects
from page.sing_page.search_page.search_result_page import SearchResultPage
from page.public_page.navigationbar_page import NavigationBarPage
from page.sing_page.search_page.more_hot_search_rank_page import MoreHotSearchRankPage
from page.sing_page.singer_page.singer_details_page import SingerDetailsPage
from page.sing_page.song_details_page import SongDetailsPage


class SearchPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def close_input_frame(self):
        """
        关闭输入框
        :return:
        """
        # NavigationBarPage(self.appium_driver).back_btn_click()
        self.swipe_down()
        return self

    def swipe_down(self):
        """
        下滑隐藏键盘
        :return:
        """
        device_height = self.appium_driver.device_height()
        device_width = self.appium_driver.device_width()
        start_height = device_height * 0.2
        end_height = device_height * 0.8
        self.appium_driver.swipe(device_width / 2, start_height, device_width / 2, end_height, 500)
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def history_title_displayed(self):
        """
        历史搜索title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("history_search_title_text"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def hot_search_rank_title_displayed(self):
        """
        热搜榜title是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("hot_search_list_title_text"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def search_song_by_keyword(self, search_txt_text):
        """
        通过搜索歌曲名搜索歌曲
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_txt_text)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn_text")))
        return SearchResultPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def search_illegal_song(self):
        """
        搜索违规歌曲
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_page_objects.normal_acc)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn_text")))
        return SearchResultPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def get_search_frame_song_name(self):
        """
        获取搜索框中默认歌曲名
        :return:
        """
        sleep(1)
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.get_attribute(
                self.appium_driver.find_element(self.get_object("search_frame_id")), "text")
        else:
            return self.appium_driver.get_attribute(
                self.appium_driver.find_element(self.get_object("search_frame_id")), "value")

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def direct_search_song(self):
        """
        通过直接点击搜索按钮搜索歌曲
        :return:
        """
        device_width = self.appium_driver.device_width()
        device_height = self.appium_driver.device_height()
        self.appium_driver.press_location(device_width * 0.92, device_height * 0.91)
        return SearchResultPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_clear_history_search_btn(self):
        """
        点击清除历史搜索按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clear_history_search_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_confirm_clear_history_btn(self):
        """
        点击确认清除历史搜索按钮
        :return:
        """
        if self.appium_driver.element_displayed(self.get_object("confirm_clear_popup_text")):
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm_clear_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_hot_search_more_btn(self):
        """
        点击热搜榜更多按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_search_more_btn")))
        return MoreHotSearchRankPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_hot_search_cell(self):
        """
        点击热搜榜单个cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_search_cell")))
        return SearchResultPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_click_songlist_name(self):
        """
        获取热搜榜第一个 热搜词 经典老歌
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.get_attribute(
                self.appium_driver.find_element(self.get_object("hot_search_cell")), "text")
        else:
            # label="1, 经典老歌, 32.5万次"
            label_value = self.appium_driver.get_attribute(
                self.appium_driver.find_element(self.get_object("hot_search_cell")), "label")
            return label_value.split(",")[1].strip()

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_best_acc_cell(self, search_txt_text):
        """
        输入搜索关键词后，点击搜索页最佳伴奏cell
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_txt_text)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("best_acc_cell_song_name")))
        return SongDetailsPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_best_acc_sing_btn(self, search_txt_text):
        """
        输入搜索关键词后，点击搜索页最佳伴奏演唱按钮
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_txt_text)
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("best_acc_sing_btn")))
        return RecordPreparePage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_song_associate_word_cell(self, search_txt_text):
        """
        输入搜索歌曲关键词后，点击搜索页联想词cell
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_txt_text)
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("associate_word_cell"))[0])
        return SearchResultPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_singer_associate_word_cell(self, search_txt_text):
        """
        输入搜索歌手关键词后，点击搜索页联想词cell
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_txt_text)
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("associate_word_cell"))[0])
        return SingerDetailsPage(self.appium_driver)

    def get_associate_word_txt(self, search_txt_text):
        """
        输入搜索关键词后，获取第一行联想词文案
        :param search_txt_text:
        :return:
        """
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                      search_txt_text)
        return self.appium_driver.get_attribute(
            self.appium_driver.find_elements(self.get_object("associate_word_text"))[0], 'text')