from page.global_player_page.global_player_page import GlobalPlayerPage
from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController


class CapableSingerRankPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        self.noattention = "关注"
        self.attention = "已关注"

    def capable_singer_title_displayed(self):
        """
        北京实力歌手榜title可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("capable_singer_rank_title"))

    def capable_singer_rank_rule_displayed(self):
        """
        获取实力歌手榜 "规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_btn"))

    def capable_singer_rank_rule_click(self):
        """
        点击 "规则" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rule_btn")))

    def capable_singer_rank_rule_title_displayed(self):
        """
        获取规则弹窗 "规则标题" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rule_title"))

    def capable_singer_rank_rule_rank_reward_displayed(self):
        """
        获取规则弹框 "上榜奖励"  可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rank_reward"))

    def capable_singer_rank_rule_rank_rule_displayed(self):
        """
        获取规则弹框 "上榜规则" 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("rank_rule"))

    def capable_singer_rank_rule_i_know_displayed(self):
        """
        获取规则弹框 "我知道了" btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("i_know_btn"))

    def capable_singer_rank_rule_i_know_click(self):
        """
        点击 规则弹框 "我知道了" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_know_btn")))

    def capable_singer_rank_player_btn_displayed(self):
        # 全局播放器
        return self.appium_driver.element_displayed(self.get_object('player_btn'))

    def capable_singer_rank_player_btn_click(self):
        # 全局播放器
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("player_btn")))
        return GlobalPlayerPage(self.appium_driver)

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def capable_singer_rank_nickname_displayed(self):
        # 歌手昵称
        # print(self.appium_driver.get_page_source())
        return self.appium_driver.element_displayed(self.get_object('nick_name'))

    def capable_singer_rank_rank_icon_first_displayed(self):
        # 歌手排名icon
        return self.appium_driver.element_displayed(self.get_object('rank_icon_first'))

    def capable_singer_rank_rank_icon_sec_displayed(self):
        # 歌手排名icon
        return self.appium_driver.element_displayed(self.get_object('rank_icon_sec'))

    def capable_singer_rank_rank_icon_three_displayed(self):
        # 歌手排名icon
        return self.appium_driver.element_displayed(self.get_object('rank_icon_three'))

    def capable_singer_rank_player_icon_displayed(self):
        # 播放按钮
        return self.appium_driver.element_displayed(self.get_object('player_icon'))

    def capable_singer_rank_note_icon_displayed(self):
        # 音符icon
        return self.appium_driver.element_displayed(self.get_object('note_icon'))

    def capable_singer_rank_attention_icon_displayed(self):
        # 关注icon
        return self.appium_driver.element_displayed(self.get_object('attention_icon'))

    def capable_singer_rank_attention_icon_click(self):
        # 点击关注icon
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object('attention_icon')))

    def capable_singer_rank_attention_state_text(self):
        # 获取关注按钮状态
        return self.appium_driver.find_element(self.get_object('attention_icon')).text
        # print(self.appium_driver.find_element(self.get_object('attention_icon')).text)

    def capable_singer_rank_attention_sheet_displayed(self):
        # 取消关注actionsheet可见
        return self.appium_driver.element_displayed(self.get_object('attention_sheet'))

    def capable_singer_rank_sure_btn_displayed(self):
        # 确定
        return self.appium_driver.element_displayed(self.get_object('sure_btn'))

    def capable_singer_rank_sure_btn_click(self):
        # 点击确定
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object('sure_btn')))

    def capable_singer_rank_cancel_btn_displayed(self):
        # 取消
        return self.appium_driver.element_displayed(self.get_object('cancel_btn'))

    def capable_singer_rank_cancel_btn_click(self):
        # 点击取消
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object('cancel_btn')))



