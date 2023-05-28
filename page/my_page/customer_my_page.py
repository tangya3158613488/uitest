"""
我的 客态
"""
from common.driver.appium_driver import AppiumDriver
from page.my_page.my_page import MyPage
from page.my_page.song_list_page import SongListPage


class CustomerMyPage(MyPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def in_customer_my_page(self):
        """
        判断是否为客态的个人主页
        若没有编辑资料btn，则为客态
        :return:
        """
        return not self.appium_driver.element_displayed(self.get_object("edit_data_btn"))

    def click_back_btn(self):
        """
        点击返回按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_btn")))

    @AppiumDriver.wait_for(timeout_sec=2, need_catch=True)
    def click_song_list_btn(self):
        # print(self.appium_driver.get_page_source())
        """
        点击歌单按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("song_list_btn")))
        return SongListPage(self.appium_driver)

    def click_more_btn(self):
        """
        点击更多按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn")))

    def more_cell_show(self):
        """
        点击更多，出现更多的弹框
        :return:
        """
        self.click_more_btn()
        return self.appium_driver.element_displayed(self.get_object("share_home_page_btn"))


