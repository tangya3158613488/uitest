from common.driver.appium_driver import AppiumDriver
from page.liveroom_page.auction_liveroom_page import AuctionLiveRoomPage
from page.ktv_page.my_tab_creat_room_page import MyTabCreateRoomPage
from page.liveroom_page.base_liveroom_page import BaseLiveRoomPage
from page.objects_controller import ObjectsController


class MyTabPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def room_text_displayed(self, model_room_text):
        """
        各模块房间文案元素可见
        model_room_text: collect_room_text、guard_room_text、history_room_text
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object(model_room_text))

    def expend_more_collect_room_text_displayed(self):
        """
        收藏房间-“展开更多”按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("expend_more_collect_room"))

    def expend_more_collect_room_btn_click(self):
        """
        点击收藏房间模块的"展开更多"按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("expend_more_collect_room")))

    def swipe_my_tab_page_to_expend_more_btn(self):
        """
        滑动我的tab页面直到找到收藏房间模块的"展开更多"按钮
        :return:
        """
        for i in range(10):
            self.my_tab_swipe_up(2)
            print("第 {} 次滑动完成，正在找【展开更多】...".format(i + 1))
            if self.expend_more_collect_room_text_displayed():
                self.expend_more_collect_room_btn_click()
                return self.expend_more_collect_room_text_displayed()

    def stow_btn_click(self):
        """
        点击不同房间模块的"收起"按钮（从上到下依次为收藏、守护、历史）
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("stow_btn")))
        return self.expend_btn_lable()

    def expend_btn_click(self, num):
        """
        点击不同房间模块的"展开"按钮：0、1、2分别为收藏、守护、历史
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_elements(self.get_object("expend_btn"))[num])
        return self.stow_btn_label()

    def stow_btn_label(self):
        """
        获取收起按钮的label
        :return:
        """
        stow_btn = self.appium_driver.find_element(self.get_object("stow_btn"))
        return self.appium_driver.get_attribute(stow_btn, "label")

    def expend_btn_lable(self):
        """
        获取展开按钮的label
        :return:
        """
        expend_btn = self.appium_driver.find_element(self.get_object("expend_btn"))
        return self.appium_driver.get_attribute(expend_btn, "label")

    def my_tab_swipe_up(self, t):
        """
        上滑页面 t 秒
        :return:
        """
        self.appium_driver.swipe(100, 700, 100, 10, 2000)

    # def my_room_click(self):
    #     """
    #     房间有人时，直接进入房间
    #     :return:
    #     """
    #     self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("creat_room_virify")))
    #     return AuctionLiveRoomPage(self.appium_driver)
    #     center_width = self.appium_driver.device_width() * 0.5
    #     start_height = self.appium_driver.device_height() * 0.8
    #     end_height = self.appium_driver.device_height() * 0.2
    #     self.appium_driver.swipe(center_width, start_height, center_width, end_height, t*1000)

    def my_room_click(self):
        """
        房间有人时，直接进入房间
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("creat_room_virify")))
        return AuctionLiveRoomPage(self.appium_driver)

    # def my_room_click(self):
    #     """
    #     房间有人时，直接进入房间
    #     :return:
    #     """
    #     self.appium_driver.press_element(
    #         self.appium_driver.find_element(self.get_object("creat_room_virify")))
    #     return BaseLiveRoomPage(self.appium_driver)

    def create_room_text_displayed(self):
        """
        “创建房间”文案可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("create_room"))

    def create_room_btn_click(self):
        """
        点击“创建房间”
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("create_room")))
        return MyTabCreateRoomPage(self.appium_driver)

    def my_room_cell_click(self):
        """
        点击"我的房间"cell
        :return:
        """
        self.appium_driver.press_element(
            self.appium_driver.find_element(self.get_object("my_room_cell")))
        return BaseLiveRoomPage(self.appium_driver)

    def wait_for_myroom_cell_displayed(self):
        """
        等待"我的房间"卡片可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("my_room_tag"))

    def get_myroom_owner(self):
        """
        获取"我的房间"中的房主昵称
        :return:
        """
        owner_el = self.appium_driver.find_element(self.get_object("my_room_tag"))
        owner_name = self.appium_driver.get_attribute(owner_el, "label")
        print("owner_el", owner_el)
        print("owner_name", owner_name)
        return owner_name
