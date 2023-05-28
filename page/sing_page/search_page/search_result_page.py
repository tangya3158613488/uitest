from time import sleep

from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.public_page.navigationbar_page import NavigationBarPage
from page.sing_page.search_page import search_result_page_objects
from page.sing_page.search_page.all_version_page import AllVersionPage
from page.sing_page.search_page.feedback_page import FeedbackPage


class SearchResultPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def back_to_sing_page(self):
        """
        从搜索结果页返回至点歌台
        :return:
        """
        # NavigationBarPage(self.appium_driver).back_btn_click()
        from page.public_page.client_utils_page import ClientUtilsPage
        ClientUtilsPage(self.appium_driver).go_to_tab_bar_master().sing_tab_click()

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def judge_search_result_by_keyword(self):
        """
        判断通过歌曲名搜索的结果
        """
        song_name = self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("song_name_id")),
                                                     "text")
        except_song_name = search_result_page_objects.song_name_except_result
        singer_name = self.appium_driver.get_attribute(
            self.appium_driver.find_element(self.get_object("singer_name_id")),
            "text")
        except_singer_name = search_result_page_objects.singer_name_except_result
        return (song_name == except_song_name) and (except_singer_name in singer_name)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def get_search_result_by_redirt(self):
        """
        获取直接点击搜索按钮后搜索结果页的歌曲名称
        """
        sleep(1)
        if AppiumDriver.get_platform() == PlatformSelector.ANDROID:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("song_name_id")),
                                                    "text")
        else:
            return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("song_name_id")),
                                                    "label")

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def acc_tab_displayed(self):
        """
        伴奏tab是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("acc_tab"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def chorus_tab_displayed(self):
        """
        合唱tab是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("chorus_tab"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def feedback_now_btn_displayed(self):
        """
        立即反馈按钮是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("down_feedback_now_btn"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def click_feedback_now_btn(self):
        """
        点击立即反馈按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("down_feedback_now_btn")))
        return FeedbackPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def more_version_btn_displayed(self):
        """
        更多版本是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("more_version_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_more_version_btn(self):
        """
        点击更多版本
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_version_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_view_all_version_btn(self):
        """
        点击全部版本
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("view_all_version_btn")))
        return AllVersionPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def no_result_acc_page_show(self):
        """
        搜索无结果伴奏页面展示
        :return:
        """
        sleep(1)
        return self.appium_driver.element_displayed(self.get_object("no_result_show_text"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def illegal_acc_page_show(self):
        """
        搜索违禁词违规词伴奏页面展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("search_illegal_word_show"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_search_frame_word(self):
        """
        获取搜索框中搜索关键字
        """
        return self.appium_driver.get_el_text(self.appium_driver.find_element(self.get_object("search_frame_id")),
                                              'text')

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_page_song_name(self):
        """
        获取页面内第一个cell 歌曲名称
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("song_name_id")),
                                                "text")

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def get_page_singer_name(self):
        """
        获取页面内第一个cell 歌手名称
        """
        return self.appium_driver.get_attribute(self.appium_driver.find_element(self.get_object("singer_name_id")),
            "text")

    def click_chrous_tab(self):
        """
        点击合唱tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("chorus_tab")))
        return self

    def click_chrous_btn(self):
        """
        点击合唱btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("chorus_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def only_show_video_chrous_txt_display(self):
        """
        仅显示视频合唱 txt是否展示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("only_show_video_chrous_txt"))


    def click_only_show_video_chrous_btn(self):
        """
        点击仅显示视频合唱
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("open_only_show_video_chrous")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def judge_is_click_only_show_video_chrous(self):
        """
        判断是否点击了仅显示视频合唱
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("chorus_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def click_mv_chrous_btn(self):
        """
        点击mv合唱
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("mv_chorus_btn")))