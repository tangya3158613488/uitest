from page.global_player_page.global_player_page import GlobalPlayerPage
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class HottestWorkRankPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        self.Month = "月榜"
        self.Total = "总榜"

    def hottest_rank_title_displayed(self):
        """
        北京最火作品榜title可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("hottest_rank_title"))

    def hottest_rank_rule_displayed(self):
        """
        获取最火作品榜 "规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_btn"))

    def hottest_rank_rule_click(self):
        """
        点击 "规则" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rule_btn")))

    def hottest_rank_rule_title_displayed(self):
        """
        获取规则弹窗 "规则标题" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_title"))

    def hottest_rank_rule_rank_reward_displayed(self):
        """
        获取规则弹框 "上榜奖励"  可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rank_reward"))

    def hottest_rank_rule_rank_rule_displayed(self):
        """
        获取规则弹框 "上榜规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rank_rule"))

    def hottest_rank_rule_i_know_displayed(self):
        """
        获取规则弹框 "我知道了" btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("i_know_btn"))

    def hottest_rank_rule_i_know_click(self):
        """
        点击 规则弹框 "我知道了" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_know_btn")))

    def hottest_rank_player_icon_displayed(self):
        # 全局播放器
        return self.appium_driver.element_displayed(self.get_object('player_btn'))

    def hottest_rank_player_icon_click(self):
        # 全局播放器
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("player_btn")))
        return GlobalPlayerPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def hottest_rank_month_btn_displayed(self):
        # 月榜btn
        print(self.appium_driver.get_page_source())
        return self.appium_driver.element_displayed(self.get_object("month_btn"))

    def hottest_rank_month_btn_text(self):
        # 月榜text
        return self.appium_driver.find_element(self.get_object("month_btn")).text

    def hottest_rank_month_btn_click(self):
        # 月榜btn click
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("month_btn")))

    def hottest_rank_total_btn_displayed(self):
        # 总榜btn
        return self.appium_driver.element_displayed(self.get_object("total_btn"))

    def hottest_rank_total_btn_text(self):
        # 总榜text
        return self.appium_driver.find_element(self.get_object("total_btn")).text

    def hottest_rank_total_btn_click(self):
        # 总榜btn click
        return self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("total_btn")))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def hottest_rank_current_btn_text(self):
        #获取当btn名称
        return self.appium_driver.find_element(self.get_object("current_btn")).text
        # return self.appium_driver.find_element(self.get_object("new_region")).text

    def hottest_rank_work_card_displayed(self):
        # 作品card
        return self.appium_driver.element_displayed(self.get_object('work_card'))

    def hottest_rank_work_rank_first_icon_displayed(self):
        # 作品排名1
        return self.appium_driver.element_displayed(self.get_object('rank_icon_first'))

    def hottest_rank_work_rank_sec_icon_displayed(self):
        # 作品排名2
        return self.appium_driver.element_displayed(self.get_object('rank_icon_sec'))

    def hottest_rank_work_rank_thr_icon_displayed(self):
        # 作品排名3
        return self.appium_driver.element_displayed(self.get_object('rank_icon_thr'))

