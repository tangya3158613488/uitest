from common.driver.appium_driver import AppiumDriver
from common.driver.platform_selector import PlatformSelector
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage
from page.liveroom_page.buy_vipseat_alert_page import BuyVipSeatAlertPage
from page.liveroom_page.tool_box_page import ToolBoxPage
from page.liveroom_page.liveroom_more_page import LiveRoomMorePage
from page.liveroom_page.liveroom_rank_page import LiveRoomRankPage
from page.liveroom_page.wheat_down_alert_page import WheatDownAlertPage
from page.objects_controller import ObjectsController
from page.liveroom_page import base_liveroom_page


class AuctionLiveRoomPage(BaseLiveRoomPage):
# class AuctionLiveRoomPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        # super().__init__()
        self.appium_driver = appium_driver

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def auctionlive_host_name(self):
        """
        获取主持席name
        :return:

        """
        return self.appium_driver.find_element(self.get_object("auction_live_host_seat_name")).text



    def auction_live_host_seat_click(self):
        """
        点击"主持席"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("auction_live_host_seat")))
        return AuctionLiveRoomPage(self.appium_driver)

    def down_host_seat_click(self):
        """
        再次点击"主持席"
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("auction_live_host_seat")))
        return WheatDownAlertPage(self.appium_driver)

    def vip_seat_click(self):
        """
        点击"贵宾席"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("vip_seat")))
        return BuyVipSeatAlertPage(self.appium_driver)




    def auction_boolbox_click(self):
        """
        点击"工具箱"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("toolbox_btn_id")))
        return ToolBoxPage(self.appium_driver)

