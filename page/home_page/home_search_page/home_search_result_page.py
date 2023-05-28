from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class HomeSearchResultPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def in_home_search_result_page(self):
        """
        是否在首页搜索页
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("comprehensive_search_tab"))

    def click_comprehensive_search_tab(self):
        """
        点击综合tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("comprehensive_search_tab")))
        return self

    def click_accompaniment_search_tab(self):
        """
        点击伴奏tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("accompaniment_search_tab")))
        return self

    def click_group_search_tab(self):
        """
        点击-群组tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("group_search_tab")))
        return self

    def click_user_search_tab(self):
        """
        点击-用户tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("user_search_tab")))
        return self

    def click_work_search_tab(self):
        """
        点击-作品tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("work_search_tab")))
        return self

    def click_duet_search_tab(self):
        """
        点击-合唱tab
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("duet_search_tab")))
        return self

    def click_sing_btn(self):
        """
        点击-演唱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sing_btn")))
        return self

    def click_accompaniment_cell(self):
        """
        点击-伴奏cell
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("accompaniment_cell")))
        return self

    def click_accompaniment_cell_add_song_btn(self):
        """
        点击-伴奏cell添加到已点按钮
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("accompaniment_cell_add_song_btn")))
        return self

    def click_more_accompaniment_btn(self):
        """
        点击-伴奏tab-更多版本按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_accompaniment_btn")))
        return self

    def click_group_join_btn(self):
        """
        点击-群组tab-加入按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("group_join_btn")))
        return self

    def click_clear_text_btn(self):
        """
        点击删除搜索框内容按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("clear_text")))
        from page.home_page.home_search_page.home_search_page import HomeSearchPage
        return HomeSearchPage(self.appium_driver)

    def click_back_btn(self):
        """
        点击返回按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_btn")))
        from page.home_page.home_search_page.home_search_page import HomeSearchPage
        return HomeSearchPage(self.appium_driver)

    def click_search_work_card(self):
        """
        搜索结果页，作品tab，点击作品封面
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("search_work_card")))
        from page.player_page.i_want_sing.i_want_sing_page import IWantSing
        print(IWantSing(self.appium_driver))
        return IWantSing(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def get_user_nickname(self, index=0):
        """
        用户tab下获取用户昵称
        type="XCUIElementTypeStaticText" value="xiaofan772" name="nickName" label="xiaofan772"
        :param index:
        :return:
        """
        els = self.appium_driver.find_elements(self.get_object("user_nick_name"))
        return els[index].get_attribute("label")

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def get_duet_song_name(self, index=0):
        """
        合唱tab下获取合唱歌名
        value="告白气球" name="songName" label="告白气球"
        :param index:
        :return:
        """
        els = self.appium_driver.find_elements(self.get_object("duet_song_name"))
        return els[index].get_attribute("label")


