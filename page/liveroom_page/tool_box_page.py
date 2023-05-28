from common.driver.appium_driver import AppiumDriver
from page.liveroom_page.find_broadcast_page import FindBroadcastPage
from page.liveroom_page.group_talk_page import GroupTalkPage
from page.public_page.navigationbar_page import NavigationBarPage
import time


class ToolBoxPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def songfriend_call_displayed(self):
        """
        好友召唤元素可见
        model_room_text: collect_room_text、guard_room_text、history_room_text
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("songfriend_call"))

    def songfriend_call_btn_click(self):
        """
        点击"歌友召唤"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("songfriend_call")))
        return ToolBoxPage(self.appium_driver)

    def find_broadcast_btn_click(self):
        """
        点击"寻人广播"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("find_broadcast")))
        return FindBroadcastPage(self.appium_driver)

    def close_special_effects_displayed(self):
        """
        关闭特效
        model_room_text: collect_room_text、guard_room_text、history_room_text
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("close_special_effects"))

    def close_special_effects_btn_click(self):
        """
        点击"关闭特效"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_special_effects")))

    def group_talk_btn_click(self):
        """
        点击"群组"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("group_talk")))
        return GroupTalkPage(self.appium_driver)


    def center_btn_click(self):
        """
        点击"权益中心"btn
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("center")))
        return ToolBoxPage(self.appium_driver)

    def center_btn_displayed(self):
        """
        "权益中心按钮是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("center"))

    def people_search_btn_displayed(self):
        """
        "寻人广播按钮是否可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("people_search_btn_display"))

    def open_singing_area_click(self):
        """
        点击打开演唱区按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("open_singing_area_btn")))
        return ToolBoxPage(self.appium_driver)

    def close_singing_area_click(self):
        """
        点击关闭演唱区按钮
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("close_singing_area_btn")))
        return ToolBoxPage(self.appium_driver)

    def singing_area_displayed(self):
        """
        "演唱区页面可见
        :return:
        """
        time.sleep(3)
        return self.appium_driver.element_displayed(self.get_object("singing_area_displayed_text"))

    def confirm_or_cancel_click(self, button_name):
        """
        "确认取消弹窗点击
        :return:
        """
        if button_name == 1:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("confirm_btn")))
            return ToolBoxPage(self.appium_driver)
        else:
            self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("cancel_btn")))
            return ToolBoxPage(self.appium_driver)

    def punishment_btn_click(self):
        """
        惩罚按钮点击
        :return:
        """
        self.appium_driver.press_element(self.appium_driver.find_element(self.get_object("punishment_btn")))
        return ToolBoxPage(self.appium_driver)

    def punishment_tool_displayed(self):
        """
        惩罚工具可见
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("punishment_tool_displayed"))