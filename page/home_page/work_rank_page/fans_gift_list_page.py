from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class FansGiftListPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def fans_contribute_title_displayed(self):
        """
        粉丝贡献榜title可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("fans_contribute_title"))

    def head_photo_displayed(self):
        """
        粉丝头像可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("head_photo"))

    def user_name_displayed(self):
        """
        粉丝昵称可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_name"))

    def leverl_wealth_displayed(self):
        """
        粉丝 财富等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("leverl_wealth"))

    def contribute_coin_count_displayed(self):
        """
        粉丝 送出礼物总额 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("contribute_coin_count"))

    def gift_icon_displayed(self):
        """
        粉丝贡献榜 礼物icon 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("gift_icon"))

    def board_attacker_displayed(self):
        """
        粉丝贡献榜 踢榜按钮 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("board_attacker"))

    def gift_box_btn_displayed(self):
        """
        粉丝贡献榜 礼物箱btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("gift_box_btn"))

    def receive_gift_title_displayed(self):
        """
        作品收到礼物列表的标题可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("work_receive_gift_title"))

    def gift_image_displayed(self):
        """
        收到礼物的icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("gift_image"))

    def gift_box_click(self):
        """
        点击 礼物箱btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("gift_box_btn")))

    def black_btn_click(self):
        """
        点击礼物列表的返回按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("back_btn")))
