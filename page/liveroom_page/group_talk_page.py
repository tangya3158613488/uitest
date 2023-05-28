from common.driver.appium_driver import AppiumDriver
from page.public_page.navigationbar_page import NavigationBarPage


class GroupTalkPage(NavigationBarPage):
    def __init__(self, appium_driver: AppiumDriver):
        super().__init__(appium_driver)
        self.appium_driver = appium_driver

    def group_title_call_displayed(self):
        """
        歌房群聊title元素可见
        model_room_text: collect_room_text、guard_room_text、history_room_text
        :return:
        """
        return self.appium_driver.element_displayed(self.get_object("group_title"))

