from common.driver.appium_driver import AppiumDriver
from page.objects_controller import ObjectsController
from common.driver.platform_selector import PlatformSelector


class RegionRankPage(ObjectsController):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__()
        self.appium_driver = appium_driver
        self.DongCheng = '北京-东城'
        self.ChaoYang = '北京-朝阳'
        self.BeiJing = '北京'
        self.HuoXing = '火星'

    def region_rank_region_icon_displayed(self):
        """
        地区榜定位icon可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('region_icon'))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def region_rank_get_region_icon_text(self):
        """
        获取 地区榜定位icon text
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            return self.appium_driver.find_element(self.get_object("region_icon")).text
        else:
            return self.appium_driver.find_element(self.get_object("region_icon")).text

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def region_rank_time_role_displayed(self):
        """
        地区榜 更新时间和规则icon 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('time_role'))

    def region_rank_rule_btn_displayed(self):
        """
        地区榜 规则icon 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('rule_btn'))

    def region_rank_rule_btn_click(self):
        """
        点击 规则icon
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("rule_btn")))

    def region_rank_i_know_displayed(self):
        """
        获取规则弹框 "我知道了" btn 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("i_know_btn"))

    def region_rank_rule_i_know_click(self):
        """
        点击 规则弹框 "我知道了" btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("i_know_btn")))

    def region_rank_beijing_displayed(self):
        """
        选择项 北京 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('beijing'))

    def region_rank_beijing_click(self):
        """
        点击 北京 选项
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("beijing")))

    def region_rank_chaoyang_displayed(self):
        """
        选择项 北京-朝阳 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('chaoyang'))

    def region_rank_chaoyang_click(self):
        """
        点击 朝阳 选项
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("chaoyang")))

    def region_rank_dongcheng_displayed(self):
        """
        选择项 北京-东城 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('dongcheng'))

    def region_rank_dongcheng_click(self):
        """
        点击 东城 选项
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("dongcheng")))

    def region_rank_complete_click(self):
        """
        点击 完成 btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("complete")))

    def region_rank_card_displayed(self):
        """
        作品card可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("work_card"))

    @AppiumDriver.wait_for(5,need_catch=False)
    def region_rank_hottest_icon_first_displayed(self):
        """
         排名icon 可见
         :return:
         """
        return self.appium_driver.element_displayed(self.get_object('hottest_icon_first'))

    def region_rank_hottest_icon_sec_displayed(self):
        """
         排名icon 可见
         :return:
         """
        return self.appium_driver.element_displayed(self.get_object('hottest_icon_sec'))

    def region_rank_hottest_icon_three_displayed(self):
        """
         排名icon 可见
         :return:
         """
        return self.appium_driver.element_displayed(self.get_object('hottest_icon_three'))

    def region_rank_old_region_click(self):
        """
        点击重新选择地区
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("old_region")))

    def region_rank_choose_title_displayed(self):
        """
        地区选择页面title 可见
        :return:
        """
        return self.appium_driver.find_element(self.get_object("area_title"))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def region_rank_gps_icon_displayed(self):
        """
        GPS地区icon可见
        :return:
        """
        self.appium_driver.element_displayed(self.get_object('gps_icon'))

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=False)
    def region_rank_gps_area_displayed(self):
        """
        GPS地区 可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object('gps_area'))

    def region_rank_gps_area_click(self):
        """
        选择GPS地区
        :return:
        """
        if AppiumDriver.get_platform() == PlatformSelector.IOS:
            self.appium_driver.press_element_by_location(self.appium_driver.find_element(self.get_object('gps_area_btn')))  # iOS
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object('gps_area_btn')))

    def region_rank_old_tabBtn_text(self):
        """
        初始地区榜title
        :return:
        """
        return self.appium_driver.find_element(self.get_object("old_tabBtn")).text

    def region_rank_new_tabBtn_text(self):
        """
        更新地区后的地区榜title
        :return:
        """
        return self.appium_driver.find_element(self.get_object("new_tabBtn")).text


    def region_rank_old_selected_area_text(self):
        """
        获取初始定位地区 text
        :return:
        """
        return self.appium_driver.find_element(self.get_object("old_region")).text

    @AppiumDriver.wait_for(timeout_sec=5, need_catch=True)
    def region_rank_new_selected_area_text(self):
        """
        更新地区后的展示定位地区 text
        :return:
        """
        return self.appium_driver.find_element(self.get_object("new_region")).text

