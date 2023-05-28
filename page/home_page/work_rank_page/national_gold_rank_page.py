from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from page.player_page.player_page import PlayerPage


class GoldRankPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver

    def gold_rank_gold_icon_displayed(self):
        """
        全国金榜icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('gold_rank_icon'))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def gold_rank_time_role_displayed(self):
        """
        全国金榜 更新时间和可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("time_role"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def gold_rank_rule_btn_displayed(self):
        """
        全国金榜 规则icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_btn"))

    def gold_rank_time_role_click(self):
        """
        点击更新时间和规则
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rule_btn")))

    @AppiumDriver.wait_for(timeout_sec=10, need_catch=True)
    def gold_rank_attention_icon_displayed(self):
        """
        关注icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("attention_icon"))

    def gold_rank_attention_icon_click(self):
        """
        点击关注按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("attention_icon")))
        # return

    def gold_rank_feed_icon_play_displayed(self):
        """
        作品播放按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("feed_icon_play"))

    def gold_rank_feed_icon_play_chick(self):
        """
        作品播放按钮可见
        :return:
        """
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("feed_icon_play")))

    def gold_rank_feed_head_rank_displayed(self):
        """
        作品排名按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("feed_head_rank"))

    def gold_rank_feed_head_portrait_displayed(self):
        """
        作品头像可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("feed_head_portrait"))

    def gold_rank_feed_head_vip_icon_displayed(self):
        """
        作品头像 v icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("feed_head_vip_icon"))

    def gold_rank_user_name_text_tv_displayed(self):
        """
        作品 用户昵称 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_name_text_tv"))

    def gold_rank_user_vip_imageview_displayed(self):
        """
        作品 昵称底部 vip 等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_vip_imageview"))

    def gold_rank_user_singer_imageview_displayed(self):
        """
        作品 昵称底部 歌手 等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_singer_imageview"))

    def gold_rank_user_wealth_imageview_displayed(self):
        """
        作品 昵称底部 财富 等级 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("user_wealth_imageview"))

    def gold_rank_work_card_chick(self):
        """
        点击作品card 进入播放页
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("national_rank_work_card")))
        return PlayerPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def gold_rank_approbation_icon_text(self):
        """
        获取点赞数量
        :return:
        """
        approbation_num = self.appium_driver.find_element(self.get_object("approbation_icon")).text
        return approbation_num

    def gold_rank_approbation_icon_click(self):
        """
        点击点赞按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("approbation_icon")))

    def gold_rank_gift_icon_displayed(self):
        """
        送礼按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("gift_icon"))

    def gold_rank_gift_icon_click(self):
        """
        点击送礼
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("gift_icon")))
        # return PlayerPage(self.appium_driver)

    def gold_rank_commention_icon_displayed(self):
        """
        评论按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("commention_icon"))

    def gold_rank_commention_icon_click(self):
        """
        点击评论
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("commention_icon")))
        # return PlayerPage(self.appium_driver)

    def gold_rank_share_icon_displayed(self):
        """
        评论按钮可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("share_icon"))

    def gold_rank_share_icon_click(self):
        """
        点击评论
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("share_icon")))
        # return PlayerPage(self.appium_driver)
