from common.driver.appium_driver import AppiumDriver
from page.home_page.home_search_page.home_search_result_page import HomeSearchResultPage
from page.home_page.topic_detail_page.topic_detail_page import TopicDetailPage
from page.home_page.topic_detail_page.topic_square_page import TopicSquarePage
from page.objects_controller import ObjectsController
from page.webview_page.webview_page import WebViewPage


class HomeSearchPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def in_home_search_song_page(self):
        """
        是否在首页搜索页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("hot_search_tab"))

    def click_hot_search_tab(self):
        """
        点击全站热搜tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_search_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def click_hot_search_word(self, index=0):
        """
        点击全站热搜tab-热搜词,第一个热搜词
        :return:
        """
        el = self.appium_driver.find_elements(self.get_object("hot_search_word"))
        if len(el):
            self.appium_driver.press_element(el[index])
            return HomeSearchResultPage(self.appium_driver)
        return None

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def get_hot_search_word_list_len(self):
        """
        点击全站热搜tab-热搜词,第一个热搜词
        :return:
        """
        search_word_list_len = len(self.appium_driver.find_elements(self.get_object("hot_search_word")))
        return search_word_list_len

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def get_hot_search_word(self, index=0):
        """
        获取全站热搜tab-热搜词
        :return:
        """
        hot_search_word = self.appium_driver.find_elements(self.get_object("hot_search_word"))[index]
        return self.appium_driver.get_attribute(hot_search_word, "label")

    def click_hot_activity_tab(self):
        """
        点击精彩活动tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_activity_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def get_hot_activity_list_len(self):
        """
        点击全站热搜tab-热搜词,第一个热搜词
        :return:
        """
        activity_list_len = len(self.appium_driver.find_elements(self.get_object("hot_activity_cell")))
        return activity_list_len

    def click_hot_activity_cell(self, index=0):
        """
        点击精彩活动推荐活动
        :return:
        """
        el = self.appium_driver.find_elements(self.get_object("hot_activity_cell"))[index]
        self.appium_driver.press_element(el)
        return WebViewPage(self.appium_driver)

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

    def click_hot_activity_more(self):
        """
        点击精彩活动-更多
        :return:
        """
        self.swipe_down()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_activity_more")))
        return WebViewPage(self.appium_driver)

    def click_hot_topic_tab(self):
        """
        点击话题tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_topic_tab")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def get_hot_topic_list_len(self):
        """
        点击全站热搜tab-热搜词,第一个热搜词
        :return:
        """
        topic_list_len = len(self.appium_driver.find_elements(self.get_object("hot_topic_cell")))
        return topic_list_len

    def click_hot_topic_cell(self, index):
        """
        点击话题tab-单个话题cell
        :return:
        """
        els = self.appium_driver.find_elements(self.get_object("hot_topic_cell"))
        self.appium_driver.press_element(els[index])
        return TopicDetailPage(self.appium_driver)

    def click_hot_topic_more(self):
        """
        点击话题tab-查看更多
        :return:
        """
        self.swipe_down()
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hot_topic_more")))
        return TopicSquarePage(self.appium_driver)

    def click_hum_song_btn(self):
        """
        点击哼唱搜搜按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("hum_song_btn")))
        return self

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def hum_song_window_displayed(self):
        """
        哼唱搜搜弹窗是否显示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("start_hum_song_btn"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def recommend_title_displayed(self):
        """
        搜索页下方的推荐是否显示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("recommend_title"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=False)
    def search_song_by_keyword(self, keyword):
        """
        通过搜索歌曲名搜索歌曲
        :return:
        """
        print("通过搜索歌曲名搜索歌曲")
        self.appium_driver.enter_text(self.appium_driver.find_element(self.get_object("search_frame")),
                                      keyword)
        self.click_search_btn()
        return HomeSearchResultPage(self.appium_driver)

    def click_search_btn(self):
        """
        点击搜索按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_btn")))

    def click_del_history_btn(self):
        """
        点击删除历史搜索按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("del_history_btn")))
        self.appium_driver.accept_alert()
        return self

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def search_history_displayed(self):
        """
        搜索结果是否显示
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("history_search_list"))

    def click_search_history(self, index=0):
        """
        点击搜素历史记录
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("history_search_list"))[index])
        return HomeSearchResultPage(self.appium_driver)
