from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.liveroom_page.liveroom_more_page import LiveRoomMorePage
from page.liveroom_page.liveroom_rank_page import LiveRoomRankPage
from page.objects_controller import ObjectsController
from page.liveroom_page.singchatmode_page import SingChatModePage
from page.liveroom_page.gift_page import GiftPage
from page.liveroom_page.public_chat_page import PublicChatPage
from page.liveroom_page.tool_box_page import ToolBoxPage


class BaseLiveRoomPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def more_btn_displayed(self):
        """
        "更多"btn是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("more_btn_id"))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def refuse_btn_displayed(self):
        """
        "拒绝"btn是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("refuse_btn_id"))

    def refuse_btn_click(self):
        """
        点击"拒绝"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("refuse_btn_id")))
        return self

    def more_btn_click(self):
        """
        点击"更多"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("more_btn_id")))
        return LiveRoomMorePage(self.appium_driver)

    def close_btn_click(self):
        """
        点击"关闭"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_btn_id")))
        return LiveRoomMorePage(self.appium_driver)

    def cc(self):
        return self.appium_driver

    def find_close_btn(self):
        """
        关闭按钮是否可见
        :return:
        :rtype:
        """
        self.appium_driver.element_displayed(self.get_object("close_btn_id"))
        return self

    def rank_btn_click(self):
        """
        点击"排行榜"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rank_btn_id")))
        return LiveRoomRankPage(self.appium_driver)

    def get_room_id(self):
        """
        获取房间id
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.appium_driver.find_element(self.get_object("room_id_text")).text.split(":")[1]
        return self.appium_driver.find_element(self.get_object("room_id_text")).text.split("：")[1]

    def tool_box_btn_click(self):
        """
        "点击工具箱按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("toolbox_btn_id")))
        return ToolBoxPage(self.appium_driver)

    def sign_in_btn_click(self):
        """
        点击"签到"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("sign_in_btn_id")))
        return LiveRoomRankPage(self.appium_driver)

    def go_to_singchatmode(self):
        """
        "去唱聊
        :return:
        """
        return SingChatModePage(self.appium_driver)

    def gift_box_btn_click(self):
        """
        点击"礼物箱"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("gift_box_btn_id")))
        return GiftPage(self.appium_driver)

    def public_chat_btn_click(self):
        """
        点击"公聊"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("public_chat_btn_id")))
        return PublicChatPage(self.appium_driver)
