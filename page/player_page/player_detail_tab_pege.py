from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.objects_controller import ObjectsController
from page.me_page import PersonPage
from page.player_page import PlayerCommentTabPage
from page.player_page import ListenersPage
from page.message_page.message_page import MessagePage



class PlayerDetailTabPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def player_detail_tab_displayed(self):
        """
        详情tab文案可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("player_detail_tab"))

    def player_comment_tab_displayed(self):
        """
        评论tab文案可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("player_comment_tab"))

    def player_comment_tab_click(self):
        """
        评论tab点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("player_comment_tab")))
        return PlayerCommentTabPage(self.appium_driver)

    def user_head_click(self):
        """
        评论tab点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("user_head")))
        return PersonPage(self.appium_driver)

    def user_head_displayed(self):
        """
        用户头像可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_head"))

    def user_head_click(self):
        """
        用户头像点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("user_head")))
        return PersonPage(self.appium_driver)

    def author_info_displayed(self):
        """
        作者信息
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("author_info"))

    def attention_button_displayed(self):
        """
        关注按钮
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("attention_button"))

    def attention_button_click(self):
        """
        关注按钮
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attention_button")))

    def chat_button_displayed(self):
        """
        聊天按钮
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("chat_button"))

    def chat_button_click(self):
        """
        聊天按钮点击 进入聊天页
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("chat_button")))
        return MessagePage(self.appium_driver)

    def song_name_displayed(self):
        """
        作品名称
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("song_name"))

    def latest_listeners_displayed(self):
        """
        最近听众
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("latest_listeners"))

    def latest_listeners_click(self):
        """
        最近听众点击进入最近听众页面
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("latest_listeners")))
        return ListenersPage(self.appium_driver)


