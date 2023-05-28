from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.liveroom_page.liveroom_rank_page import LiveRoomRankPage

class GiftPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def free_flowers_btn_click(self):
        """
        "免费鲜花送出
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("free_flowers_btn_id")))
        return GiftPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=30, need_catch=False)
    def wait_for_gift_message(self, giftmessage):
        """
        "判断公聊区送礼信息
        :return:
        """
        gift_message = self.appium_driver.find_element(self.get_object("gift_message_id")).text
        return gift_message == giftmessage

    def wealth_level_page_click(self):
        """
        "财富等级页面点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("wealth_level_page_btn_id")))
        return LiveRoomRankPage(self.appium_driver)

